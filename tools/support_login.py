#!/usr/bin/env python3
"""Robust interactive login wrapper for the NeoLabs Support client.

The Access Code is never echoed, logged, persisted, or passed on the command line.
This wrapper only makes the hidden prompt resilient to an empty/missed paste and
then delegates authentication to the existing server-authoritative client.
"""
from __future__ import annotations

import argparse
import getpass
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLIENT = ROOT / "tools" / "neolabs.py"
ACCESS_CODE_RE = re.compile(r"^[A-Za-z0-9._-]{12,128}$")

# Capture the real console prompt before temporarily replacing the imported
# client's getpass function. Python modules are shared objects; without this
# stable reference, replacing client.getpass.getpass also replaces this
# module's getpass.getpass and prompt_access_code recursively calls itself.
_SYSTEM_GETPASS = getpass.getpass


def fail(message: str) -> "NoReturn":
    raise SystemExit(f"ERROR: {message}")


def prompt_access_code(prompt: str = "NeoLabs Access Code: ") -> str:
    for attempt in range(1, 4):
        try:
            value = _SYSTEM_GETPASS(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            fail("Access Code entry was cancelled; run `.\\neolabs.cmd login` again")
        if not value:
            if attempt < 3:
                print("No Access Code was detected. Paste it at the hidden prompt and press Enter.", file=sys.stderr)
                continue
            break
        if ACCESS_CODE_RE.fullmatch(value):
            return value
        if attempt < 3:
            print("That entry does not match the NeoLabs Access Code format. Paste the code exactly, with no spaces.", file=sys.stderr)
    fail("could not read a valid NeoLabs Access Code after 3 attempts")


def load_client():
    spec = importlib.util.spec_from_file_location("neolabs_support_client", CLIENT)
    if not spec or not spec.loader:
        fail("NeoLabs Support client is missing")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="NeoLabs IT Security Support login")
    p.add_argument("--pod")
    p.add_argument("--base-url", default=None)
    return p


def main() -> int:
    args = parser().parse_args()
    client = load_client()
    original_getpass = client.getpass.getpass
    client.getpass.getpass = prompt_access_code
    try:
        client.login(args)
    finally:
        client.getpass.getpass = original_getpass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
