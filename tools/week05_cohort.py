"""Week 05 *standalone cohort* SSH automation (separate from authoritative W04 broker).

Opt-in one-time setup pins the mentor-verified server ED25519 host key, per-student
restricted SSH account, and local private key. Afterwards "bash neolabs connect"
opens the localhost-only W05 Pod01 tunnel without querying the W04 broker.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROLE = "SUPPORT"
USER_PATTERN = r"nlw05sup_[0-9a-f]{12}"
BASE = Path.home() / ".neolabs" / "support"
PROFILE = BASE / "w05-cohort-profile.json"
KEY = BASE / "w05-tunnel-ed25519"
KNOWN = BASE / "w05-known-hosts"
EXPIRY = datetime.fromisoformat("2026-11-16T06:00:00+00:00")


def stop(reason):
    raise ValueError(reason)


def private_write(path: Path, body: str, mode=0o600):
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.is_symlink():
        stop("Refusing symlinked private profile/known-hosts file")
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=".w05-")
    try:
        os.fchmod(fd, mode)
        with os.fdopen(fd, "w") as out:
            out.write(body)
            out.flush()
            os.fsync(out.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def keygen(_args=None):
    BASE.mkdir(mode=0o700, parents=True, exist_ok=True)
    os.chmod(BASE, 0o700)
    pub = Path(str(KEY)+".pub")
    if KEY.is_symlink() or pub.is_symlink():
        stop("Refusing symlinked SSH key")
    if not KEY.exists() and not pub.exists():
        sshgen = shutil.which("ssh-keygen")
        if not sshgen:
            stop("OpenSSH ssh-keygen is required")
        subprocess.run([sshgen, "-q", "-t", "ed25519", "-N", "", "-f", str(KEY),
                        "-C", "neolabs-w05-support"], check=True)
        os.chmod(KEY, 0o600)
    if not KEY.is_file() or not pub.is_file() or KEY.stat().st_mode & 0o077:
        stop("Invalid W05 SSH keypair; private key must be 0600")
    print("Week05 SSH public key (give ONLY this .pub content to the mentor):")
    print(pub.read_text().strip())
    print("Never send the private key or an administrator .pem file.")


def profile():
    if not PROFILE.exists():
        return None
    if PROFILE.is_symlink() or PROFILE.stat().st_mode & 0o077:
        stop("Week05 cohort profile must be private (0600)")
    try:
        info = json.loads(PROFILE.read_text())
    except (ValueError, OSError):
        stop("Invalid Week05 cohort profile")
    if (not isinstance(info, dict) or info.get("role") != ROLE
            or info.get("pod_id") != "pod-01"
            or info.get("expires_at") != "2026-11-16T06:00:00Z"
            or info.get("port") != 22
            or not re.fullmatch(USER_PATTERN, str(info.get("username", "")))
            or not re.fullmatch(r"[a-zA-Z0-9.-]{1,253}", str(info.get("host", "")))
            or not re.fullmatch(r"SHA256:[A-Za-z0-9+/]{43}", str(info.get("fingerprint", "")))):
        stop("Invalid or mismatched W05 cohort profile")
    if datetime.now(timezone.utc) >= EXPIRY:
        stop("Week05 cohort access expired; do not continue forwarding")
    if not KNOWN.is_file() or KNOWN.is_symlink() or KNOWN.stat().st_mode & 0o077:
        stop("Missing protected pinned SSH host key")
    if not KEY.is_file() or KEY.is_symlink() or KEY.stat().st_mode & 0o077:
        stop("Missing protected W05 private SSH key")
    return info


def configure(args):
    host = args.host
    user = args.username
    fingerprint = args.fingerprint
    if not re.fullmatch(r"[A-Za-z0-9.-]{1,253}", host) or ".." in host or host.startswith("-"):
        stop("Host must be an approved hostname or IPv4 address (no URLs/ports)")
    if not re.fullmatch(USER_PATTERN, user):
        stop("Restricted Week05 SSH username does not match track")
    if not re.fullmatch(r"SHA256:[A-Za-z0-9+/]{43}", fingerprint):
        stop("Provide verified ED25519 host fingerprint, SHA256:...")
    if datetime.now(timezone.utc) >= EXPIRY:
        stop("Week05 cohort expiry already passed")
    if profile() is not None:
        stop("A W05 profile is already installed; remove it explicitly with 'neolabs week05 clear' before changing host or user")
    keygen()
    scan = shutil.which("ssh-keyscan")
    keyhash = shutil.which("ssh-keygen")
    if not scan or not keyhash:
        stop("Both ssh-keyscan and ssh-keygen are required")
    response = subprocess.run([scan, "-T", "5", "-p", "22", "-t", "ed25519", host],
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                              text=True, timeout=12, check=False)
    keys = [line for line in response.stdout.splitlines() if
            line and not line.startswith("#") and
            len(line.split()) == 3 and line.split()[1] == "ssh-ed25519"]
    if len(keys) != 1:
        stop("Expected one ED25519 SSH host key from the approved server")
    check = subprocess.run([keyhash, "-lf", "-", "-E", "sha256"],
                           input=keys[0]+"\n", stdout=subprocess.PIPE,
                           stderr=subprocess.DEVNULL, text=True, check=True)
    if fingerprint not in check.stdout.split():
        stop("STOP: SSH host key does not match the mentor-verified fingerprint")
    private_write(KNOWN, keys[0]+"\n")
    private_write(PROFILE,json.dumps({
        "role":ROLE, "pod_id":"pod-01", "host":host, "username":user, "port":22,
        "fingerprint":fingerprint, "expires_at":"2026-11-16T06:00:00Z"
    }, indent=2)+"\n")
    print("✓ Authorized Week05 Pod01 SUPPORT tunnel profile saved locally.")
    print("✓ SSH host key verified and pinned; this computer's private key stays local.")
    print("Next: bash neolabs connect")


def connect():
    info = profile()
    if info is None:
        return False
    ssh=shutil.which("ssh")
    if not ssh:
        stop("OpenSSH client not installed")
    args=[ssh, "-i", str(KEY), "-o", "IdentitiesOnly=yes",
          "-o", "BatchMode=yes", "-o", "PasswordAuthentication=no",
          "-o", "StrictHostKeyChecking=yes",
          "-o", f"UserKnownHostsFile={KNOWN}", "-o", "GlobalKnownHostsFile=/dev/null",
          "-o", "ExitOnForwardFailure=yes", "-o", "ServerAliveInterval=30",
          "-o", "ServerAliveCountMax=3", "-N",
          "-L", "127.0.0.1:18080:127.0.0.1:18600", "-p", "22",
          f"{info['username']}@{info['host']}"]
    print("✓ Week05 Pod01 SUPPORT tunnel opening at http://127.0.0.1:18080/support")
    print("Keep this terminal open; in another run: bash neolabs incident dashboard")
    print("Use your separately provided Week05 SUPPORT cohort code in the browser.")
    try:
        subprocess.run(args,check=True)
    except KeyboardInterrupt:
        print("Week05 Support SSH tunnel closed.")
    return True


def clear(_args):
    if PROFILE.is_symlink():
        stop("Refusing symlinked Week05 cohort profile")
    PROFILE.unlink(missing_ok=True)
    print("Week05 cohort routing disabled. Your W04 access flow is unchanged.")
    print("Existing SSH private key and pinned host entry were retained.")


def add_commands(sub):
    root=sub.add_parser("week05",help="Standalone Week05 Pod01 cohort SSH enrolment and connection")
    nested=root.add_subparsers(dest="week05_command",required=True)
    p=nested.add_parser("keygen",help="Generate/show ONLY the Week05 SSH public key")
    p.set_defaults(func=keygen)
    p=nested.add_parser("configure",help="Pin mentor-verified Week05 host and approved restricted username")
    p.add_argument("--host",required=True)
    p.add_argument("--username",required=True)
    p.add_argument("--fingerprint",required=True,help="Mentor verified SSH ED25519 SHA256 fingerprint")
    p.set_defaults(func=configure)
    p=nested.add_parser("clear",help="Stop using standalone cohort profile; W04 flow is restored")
    p.set_defaults(func=clear)
