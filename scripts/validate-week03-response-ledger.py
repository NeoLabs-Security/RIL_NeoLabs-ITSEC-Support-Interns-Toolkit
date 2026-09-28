#!/usr/bin/env python3
"""Validate a Week 3 response ledger without contacting AWS or the arena."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

HEADERS = ["change_id", "account_id", "soc_alert_or_event_id", "requested_time_utc", "approved_by", "action", "original_state", "completed_time_utc", "response_event_or_rule_id", "validation_result", "rollback_owner", "responder", "notes"]
ACCOUNT = re.compile(r"^syn-credential-storm-pod-01-(?:0[1-9]|1[0-5])$")
UTC = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2})?Z$")
ALLOWED_ACTIONS = {"contain-account", "block-ip"}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != HEADERS:
            return ["header does not match the Week 3 response ledger template"]
        for line, row in enumerate(reader, 2):
            if not ACCOUNT.fullmatch(row["account_id"]):
                errors.append(f"line {line}: invalid account_id")
            if not row["soc_alert_or_event_id"].strip():
                errors.append(f"line {line}: SOC alert/event ID is required")
            if row["action"] not in ALLOWED_ACTIONS:
                errors.append(f"line {line}: action must be contain-account or block-ip")
            for field in ("requested_time_utc", "completed_time_utc"):
                if not UTC.fullmatch(row[field]):
                    errors.append(f"line {line}: {field} must be ISO 8601 UTC ending in Z")
            for field in ("approved_by", "original_state", "response_event_or_rule_id", "validation_result", "rollback_owner"):
                if not row[field].strip():
                    errors.append(f"line {line}: {field} is required")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate-week03-response-ledger.py LEDGER.csv", file=sys.stderr)
        return 2
    errors = validate(Path(sys.argv[1]))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Week 3 response ledger structure is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
