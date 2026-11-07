#!/usr/bin/env python3
"""Authorized Week 05 quarantine client: one review or one explicit containment.

Mentor preview only; normal student release requires NeoLabs broker-issued scope.
"""
from __future__ import annotations
import argparse
import getpass
import json
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


def localhost_url(value: str) -> str:
    u = urlparse(value)
    if u.scheme != "http" or u.hostname not in {"localhost", "127.0.0.1"} or u.port not in {18080, *range(18601, 18606)} or u.username or u.password or u.path not in {"", "/"} or u.query or u.fragment:
        raise ValueError("Only current authorized localhost tunnel or mentor loopback is permitted")
    return f"http://{u.hostname}:{u.port}"


def json_request(req):
    try:
        with urlopen(req, timeout=8) as resp:
            return resp.status, json.load(resp)
    except HTTPError as error:
        return error.code, json.load(error)


def perform(url: str, pod: str, role_token: str, upload_id: str | None, confirmation: bool, incident_id: str | None = None) -> dict:
    base = localhost_url(url)
    if pod not in {f"pod-{i:02d}" for i in range(1, 6)}:
        raise ValueError("Invalid authorized pod")
    _, health = json_request(Request(base + "/health", method="GET"))
    if health.get("scenario_id") != "w05-poisoned-upload" or health.get("pod_id") != pod:
        raise RuntimeError("Wrong scenario or pod; stop and escalate")
    headers = {"Authorization": "Bearer " + role_token}
    if upload_id is None:
        code, data = json_request(Request(base + "/api/admin/uploads", headers=headers))
        if code != 200:
            raise RuntimeError(f"List refused: HTTP {code}")
        return {"scenario_id": "w05-poisoned-upload", "pod_id": pod, "uploads": data.get("uploads", [])}
    if not re.fullmatch("[a-f0-9]{32}", upload_id):
        raise ValueError("Upload ID must be server-issued 32-char lowercase hex")
    if not confirmation:
        raise ValueError("Quarantine is a state-changing action and requires --confirm")
    if not incident_id or not re.fullmatch(r"INC-W05-[A-Za-z0-9-]{1,32}", incident_id):
        raise ValueError("Quarantine requires approved Week 05 incident ID")
    headers["X-Incident-ID"] = incident_id
    code, data = json_request(Request(
        base + "/api/admin/uploads/" + upload_id + "/quarantine",
        data=b"", method="POST", headers=headers))
    if code != 200:
        raise RuntimeError(f"Quarantine refused: HTTP {code}")
    return {"scenario_id": "w05-poisoned-upload", "pod_id": pod,
            "upload_id": upload_id, "state": data.get("state"),
            "event_id": data.get("event_id"), "request_id": data.get("request_id")}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--url", required=True)
    p.add_argument("--expected-pod", required=True)
    p.add_argument("--upload-id", help="Specific uploaded synthetic artifact to quarantine")
    p.add_argument("--incident", help="Mentor-issued incident ID for change-record evidence")
    p.add_argument("--confirm", action="store_true", help="Required for quarantine")
    args = p.parse_args()
    if args.upload_id and (not args.incident or not re.fullmatch(r"INC-W05-[A-Za-z0-9-]{1,32}", args.incident)):
        p.error("A mentor-issued incident reference such as INC-W05-001 is required for quarantine")
    token = getpass.getpass("Mentor-issued W05 Support token (not echoed): ")
    try:
        result = perform(args.url, args.expected_pod, token, args.upload_id, args.confirm, args.incident)
    except (RuntimeError, ValueError, TimeoutError, URLError) as error:
        raise SystemExit(f"STOP: {error}") from None
    if args.incident:
        result["incident_id"] = args.incident
    print(json.dumps(result, indent=2))
