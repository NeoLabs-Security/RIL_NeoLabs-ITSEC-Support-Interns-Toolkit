#!/usr/bin/env python3
"""NeoLabs IT Security Support pod access client.

The always-available NeoLabs gateway controls pod, scenario and support resources.
Interactive endpoints are shown only while an approved live surface exists. During
replay windows, Support can download only pod-scoped synthetic telemetry/evidence
for ticket analysis, escalation and documentation.
"""
from __future__ import annotations

import argparse
import getpass
import hashlib
import json
import os
import re
import secrets
import ssl
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

TRACK = "SUPPORT"
POD_RE = re.compile(r"^pod-[0-9]{2}$")
INTERACTIVE_STATES = {"LIVE", "CLOUD_LIVE", "ENDPOINT_LIVE"}
ROOT = Path(__file__).resolve().parents[1]
RUNTIME_DIR = ROOT / "runtime"
RUNTIME_MANIFEST = RUNTIME_DIR / "access-manifest.json"
EVIDENCE_DIR = RUNTIME_DIR / "evidence"
REPLAY_DIR = RUNTIME_DIR / "replay"
HOME_STATE = Path.home() / ".neolabs" / "support"
SESSION_FILE = HOME_STATE / "session.json"
INSTALLATION_FILE = HOME_STATE / "installation-id"
MAX_DOWNLOAD_BYTES = 25 * 1024 * 1024


def fail(message: str) -> "NoReturn":
    raise SystemExit(f"ERROR: {message}")


def atomic_write(path: Path, text: str, mode: int = 0o600) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as temp:
        temp.write(text)
        temp.flush()
        os.fsync(temp.fileno())
        tmp = Path(temp.name)
    try:
        os.chmod(tmp, mode)
    except OSError:
        pass
    tmp.replace(path)


def normalize_pod(value: str) -> str:
    raw = value.strip().lower()
    if raw.startswith("pod-"):
        pod = raw
    elif raw.isdigit():
        pod = f"pod-{int(raw):02d}"
    else:
        fail("pod must be a number such as 3/03 or an identifier such as pod-03")
    if not POD_RE.fullmatch(pod):
        fail("pod must use the pod-XX format")
    return pod


def validate_base_url(value: str) -> str:
    parsed = urllib.parse.urlsplit(value.strip())
    if parsed.scheme != "https" or not parsed.netloc:
        fail("NEOLABS_LAB_BASE_URL must be an absolute HTTPS URL")
    if parsed.username or parsed.password or parsed.fragment:
        fail("lab base URL must not contain embedded credentials or a fragment")
    return value.rstrip("/")


def ssl_context() -> ssl.SSLContext:
    context = ssl.create_default_context()
    ca_file = os.environ.get("NEOLABS_CA_FILE", "").strip()
    if ca_file:
        path = Path(ca_file).expanduser()
        if not path.is_file():
            fail(f"NEOLABS_CA_FILE does not exist: {path}")
        context.load_verify_locations(cafile=str(path))
    return context


def request_json(base_url: str, path: str, *, method: str = "GET", payload: dict[str, Any] | None = None, token: str | None = None) -> dict[str, Any]:
    endpoint = urllib.parse.urljoin(base_url.rstrip("/") + "/", path.lstrip("/"))
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {"Accept": "application/json", "User-Agent": "NeoLabs-ITSEC-Support-Toolkit/1.1"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(endpoint, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(request, context=ssl_context(), timeout=25) as response:
            body = response.read(2 * 1024 * 1024 + 1)
    except urllib.error.HTTPError as exc:
        detail = exc.read(4096).decode("utf-8", errors="replace")
        if exc.code in (401, 403):
            fail("authentication or pod/track authorization was rejected; verify your access code and assigned pod")
        if exc.code == 503:
            fail("the NeoLabs lab access service is not enabled for this environment")
        fail(f"lab access service returned HTTP {exc.code}: {detail}")
    except (urllib.error.URLError, TimeoutError, ssl.SSLError):
        fail("could not establish a verified HTTPS connection to the NeoLabs lab service")
    if len(body) > 2 * 1024 * 1024:
        fail("lab access response exceeded the allowed size")
    try:
        result = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        fail("lab access service returned invalid JSON")
    if not isinstance(result, dict):
        fail("lab access response must be a JSON object")
    return result


def download_bytes(url: str) -> bytes:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
        fail("replay gateway returned an invalid download URL")
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "NeoLabs-Support-Replay/1.1"}), context=ssl_context(), timeout=45) as response:
            body = response.read(MAX_DOWNLOAD_BYTES + 1)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ssl.SSLError):
        fail("could not download an authorised replay object")
    if len(body) > MAX_DOWNLOAD_BYTES:
        fail("replay object exceeded the allowed download size")
    return body


def installation_id() -> str:
    if INSTALLATION_FILE.is_file():
        value = INSTALLATION_FILE.read_text(encoding="utf-8").strip()
        if re.fullmatch(r"[0-9a-f]{32}", value):
            return value
    value = secrets.token_hex(16)
    atomic_write(INSTALLATION_FILE, value + "\n")
    return value


def read_session() -> dict[str, Any]:
    if not SESSION_FILE.is_file():
        fail("no NeoLabs session found; run `neolabs login` first")
    try:
        value = json.loads(SESSION_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        fail("local NeoLabs session is unreadable; run `neolabs login` again")
    if not isinstance(value, dict) or not isinstance(value.get("session_token"), str):
        fail("local NeoLabs session is incomplete; run `neolabs login` again")
    return value


def manifest_from(value: dict[str, Any]) -> dict[str, Any]:
    manifest = value.get("manifest")
    if not isinstance(manifest, dict) or manifest.get("track") != TRACK:
        fail("server returned an invalid or wrong-track access manifest")
    pod = manifest.get("pod_id")
    if not isinstance(pod, str) or not POD_RE.fullmatch(pod):
        fail("server returned an invalid pod identifier")
    if not isinstance(manifest.get("resources"), dict):
        fail("server returned invalid track resources")
    return manifest


def save_runtime(manifest: dict[str, Any]) -> None:
    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
    atomic_write(RUNTIME_MANIFEST, json.dumps(manifest, indent=2, sort_keys=True) + "\n")


def refresh(session: dict[str, Any]) -> dict[str, Any]:
    base_url = validate_base_url(str(session.get("base_url", "")))
    response = request_json(base_url, "/api/v1/lab-access/manifest", token=str(session["session_token"]))
    manifest = manifest_from(response)
    session["manifest"] = manifest
    if isinstance(response.get("expires_at"), str):
        session["expires_at"] = response["expires_at"]
    atomic_write(SESSION_FILE, json.dumps(session, indent=2, sort_keys=True) + "\n")
    save_runtime(manifest)
    return manifest


def login(args: argparse.Namespace) -> None:
    base_url = validate_base_url(args.base_url or os.environ.get("NEOLABS_LAB_BASE_URL", ""))
    pod = normalize_pod(args.pod or input("Pod number: "))
    access_code = getpass.getpass("NeoLabs Access Code: ").strip()
    if len(access_code) < 12 or any(ch.isspace() for ch in access_code):
        fail("access code has an unexpected format")
    response = request_json(base_url, "/api/v1/lab-access/login", method="POST", payload={"access_code": access_code, "pod_number": pod, "track": TRACK, "installation_id": installation_id()})
    token = response.get("session_token")
    if not isinstance(token, str) or not token:
        fail("server did not return a lab session")
    manifest = manifest_from(response)
    state = {"base_url": base_url, "session_token": token, "expires_at": response.get("expires_at"), "manifest": manifest}
    atomic_write(SESSION_FILE, json.dumps(state, indent=2, sort_keys=True) + "\n")
    save_runtime(manifest)
    print("✓ Authentication successful")
    print(f"✓ Assigned pod: {manifest['pod_id']}")
    print("✓ Track: IT Security Support")
    print(f"✓ Lab state: {manifest.get('lab_state', 'LIVE')}")
    print("Next: run `neolabs connect`, `neolabs targets`, or `neolabs replay` as directed by the current task.")


def connect(_: argparse.Namespace) -> None:
    manifest = refresh(read_session())
    state = str(manifest.get("lab_state") or "LIVE")
    if state not in INTERACTIVE_STATES:
        print(f"NeoLabs state: {state}. No interactive Support endpoint is required/available in this window.")
        print("Use `neolabs replay` for archived telemetry and `neolabs evidence` for approved ticket/cloud/endpoint evidence.")
        return
    resources = manifest["resources"]
    endpoints = resources.get("endpoints", [])
    print(f"✓ {state} context refreshed for {manifest['pod_id']}.")
    print(f"✓ {len(endpoints) if isinstance(endpoints, list) else 0} authorised support endpoint(s) available.")
    print("Use only the resources displayed by `neolabs targets`.")


def status(_: argparse.Namespace) -> None:
    session = read_session()
    manifest = refresh(session)
    print("NEOLABS SECURITY LAB")
    print(f"State:    {manifest.get('lab_state') or 'LIVE'}")
    print(f"Mode:     {manifest.get('runtime_mode') or 'live-control-plane'}")
    print(f"Track:    {manifest['track']}")
    print(f"Pod:      {manifest['pod_id']}")
    print(f"Scenario: {manifest.get('scenario_id') or 'not published'}")
    print(f"Session:  expires {session.get('expires_at') or 'unknown'}")


def pod_info(_: argparse.Namespace) -> None:
    manifest = refresh(read_session())
    print("NEOLABS SECURITY LAB")
    print(f"Pod:      {manifest['pod_id']}")
    print(f"Track:    {manifest['track']}")
    print(f"Scenario: {manifest.get('scenario_id') or 'not published'}")
    print(f"State:    {manifest.get('lab_state') or 'LIVE'}")
    print("The pod is assigned server-side and cannot be changed from this client.")


def scope(_: argparse.Namespace) -> None:
    manifest = refresh(read_session())
    print(f"Authorised pod: {manifest['pod_id']}")
    print("IT Security Support uses resource-level authorization. Run `neolabs targets` for live resources or `neolabs replay` for archived material.")


def display_resource(item: Any) -> str:
    if not isinstance(item, dict):
        return str(item)
    label = str(item.get("label", "resource"))
    values = [item.get("url"), item.get("hostname"), item.get("ip")]
    address = " / ".join(str(value) for value in values if value)
    return f"{label}: {address or '(no address published)'}"


def targets(_: argparse.Namespace) -> None:
    manifest = refresh(read_session())
    state = str(manifest.get("lab_state") or "LIVE")
    resources = manifest["resources"]
    print("AUTHORISED SUPPORT RESOURCES")
    if state not in INTERACTIVE_STATES:
        print(f"  - no interactive endpoints: current state is {state}")
    endpoints = resources.get("endpoints", [])
    assets = resources.get("assets", [])
    if state in INTERACTIVE_STATES and isinstance(endpoints, list):
        for endpoint in endpoints:
            print(f"  - {display_resource(endpoint)}")
    if isinstance(assets, list):
        for asset in assets:
            print(f"  - asset: {asset}")


def local_path(directory: Path, key: str) -> Path:
    name = Path(key).name or "replay.bin"
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", name)[:120]
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()[:10]
    return directory / f"{digest}-{safe}"


def download_collection(kind: str) -> None:
    session = read_session()
    manifest = refresh(session)
    response = request_json(validate_base_url(str(session["base_url"])), "/api/v1/lab-access/replay", token=str(session["session_token"]))
    source_key = "telemetry_packs" if kind == "telemetry" else "evidence"
    directory = REPLAY_DIR if kind == "telemetry" else EVIDENCE_DIR
    items = response.get(source_key, [])
    if not isinstance(items, list):
        fail(f"replay gateway returned an invalid {source_key} list")
    directory.mkdir(parents=True, exist_ok=True)
    downloaded = 0
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("key"), str) or not isinstance(item.get("url"), str):
            continue
        destination = local_path(directory, item["key"])
        if destination.is_file():
            continue
        destination.write_bytes(download_bytes(item["url"]))
        try:
            os.chmod(destination, 0o600)
        except OSError:
            pass
        downloaded += 1
    print(f"✓ Downloaded {downloaded} new {kind} file(s) for {manifest['pod_id']} to {directory}.")


def replay(_: argparse.Namespace) -> None:
    download_collection("telemetry")


def evidence(_: argparse.Namespace) -> None:
    download_collection("evidence")


def disconnect(_: argparse.Namespace) -> None:
    for path in (SESSION_FILE, RUNTIME_MANIFEST):
        try:
            path.unlink()
        except FileNotFoundError:
            pass
    print("✓ Local NeoLabs session disconnected.")


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="NeoLabs IT Security Support pod access client")
    sub = p.add_subparsers(dest="command", required=True)
    x = sub.add_parser("login"); x.add_argument("--pod"); x.add_argument("--base-url", default=None); x.set_defaults(func=login)
    x = sub.add_parser("connect"); x.set_defaults(func=connect)
    x = sub.add_parser("status"); x.set_defaults(func=status)
    x = sub.add_parser("scope"); x.set_defaults(func=scope)
    x = sub.add_parser("targets"); x.set_defaults(func=targets)
    x = sub.add_parser("replay"); x.set_defaults(func=replay)
    x = sub.add_parser("evidence"); x.set_defaults(func=evidence)
    x = sub.add_parser("pod"); nested = x.add_subparsers(dest="pod_command", required=True); y = nested.add_parser("info"); y.set_defaults(func=pod_info)
    x = sub.add_parser("disconnect"); x.set_defaults(func=disconnect)
    return p


def main() -> int:
    args = parser().parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
