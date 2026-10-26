#!/usr/bin/env python3
"""Display the current pod-scoped NeoLabs Support ticket queue.

This helper deliberately reuses the existing authenticated Support client. It
refreshes the server-authoritative manifest first, then displays only the
student-safe tickets published inside that manifest. There is no pod selector.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CLIENT = ROOT / "tools" / "neolabs.py"
RUNTIME_MANIFEST = ROOT / "runtime" / "access-manifest.json"
SESSION_FILE = Path.home() / ".neolabs" / "support" / "session.json"
POD_RE = re.compile(r"^pod-[0-9]{2}$")
SYNTHETIC_FIXTURE_RE = re.compile(r"^syn-user-p(?P<pod>[0-9]{2})-[A-Za-z0-9._-]+$")


def fail(message: str) -> "NoReturn":
    raise SystemExit(f"ERROR: {message}")


def refresh_manifest() -> None:
    if not CLIENT.is_file():
        fail("NeoLabs Support client is missing from this toolkit")
    result = subprocess.run(
        [sys.executable, str(CLIENT), "status"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        detail = (result.stderr or "").strip()
        clean = detail.removeprefix("ERROR: ")
        if "authentication or pod/track authorization was rejected" in clean:
            try:
                SESSION_FILE.unlink()
            except FileNotFoundError:
                pass
            fail("saved NeoLabs session was rejected or is stale; run `.\\neolabs.cmd login` again to create a fresh session")
        fail(clean if clean else "could not refresh the authenticated Support manifest")


def account_matches_pod(account: str, pod: str) -> bool:
    if pod in account:
        return True
    fixture = SYNTHETIC_FIXTURE_RE.fullmatch(account)
    return bool(fixture and f"pod-{fixture.group('pod')}" == pod)


def read_ticket_resource(*, refresh: bool = True) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    if refresh:
        refresh_manifest()
    if not RUNTIME_MANIFEST.is_file():
        fail("no current Support manifest found; run `.\\neolabs.cmd login` first")
    try:
        manifest = json.loads(RUNTIME_MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        fail("current Support manifest is unreadable; run `.\\neolabs.cmd status` and retry")
    if not isinstance(manifest, dict) or manifest.get("track") != "SUPPORT":
        fail("the current NeoLabs manifest is not an IT Security Support assignment")
    pod = manifest.get("pod_id")
    if not isinstance(pod, str) or not POD_RE.fullmatch(pod):
        fail("the current manifest has an invalid server-issued pod")
    resources = manifest.get("resources")
    if not isinstance(resources, dict):
        fail("the current Support resource manifest is invalid")
    queue = resources.get("support_ticket_queue")
    if queue is None:
        fail("the authenticated manifest is missing the current versioned Support queue; contact a mentor so the assignment can be republished")
    if not isinstance(queue, list):
        fail("the server returned an invalid Support ticket queue")
    validated: list[dict[str, Any]] = []
    for item in queue:
        if not isinstance(item, dict):
            fail("the server returned a malformed Support ticket")
        account = item.get("account_reference")
        if not isinstance(account, str) or not account_matches_pod(account, pod):
            fail("a Support ticket failed the assigned-pod isolation check; stop and contact a mentor")
        if manifest.get('scenario_id') == 'w04-broken-gate':
            safe_fields = ('ticket_id', 'queue_position', 'severity', 'queue', 'reporter', 'account_reference',
                           'reported_time_hint', 'user_remembers_login', 'current_access', 'user_statement',
                           'support_action_authority', 'soc_escalation_guidance')
            safe = {key: item[key] for key in safe_fields if key in item}
            device = item.get('device_context')
            if isinstance(device, dict):
                safe['device_context'] = {key: device[key] for key in ('asset', 'os', 'browser') if key in device}
            if 'course_access' in item:
                safe['course_access'] = validate_course_evidence(manifest, item)
            item = safe
        validated.append(item)
    return manifest, validated


def format_device(value: Any) -> str:
    if not isinstance(value, dict):
        return "not supplied"
    parts = [value.get("asset"), value.get("os"), value.get("browser")]
    return " / ".join(str(item) for item in parts if item) or "not supplied"


def print_ticket(ticket: dict[str, Any]) -> None:
    position = ticket.get("queue_position", "?")
    ticket_id = ticket.get("ticket_id", "unknown")
    severity = str(ticket.get("severity", "needs-triage")).upper()
    print(f"\n[{position}] {ticket_id}  [{severity}]")
    print(f"Queue:             {ticket.get('queue', 'Identity & Access')}")
    print(f"Reporter:          {ticket.get('reporter', 'synthetic user')}")
    print(f"Account reference: {ticket.get('account_reference', 'not supplied')}")
    print(f"Reported window:   {ticket.get('reported_time_hint', 'not supplied')}")
    print(f"Remembers login:   {ticket.get('user_remembers_login', 'uncertain')}")
    print(f"Device/context:    {format_device(ticket.get('device_context'))}")
    print(f"Current access:    {ticket.get('current_access', 'not supplied')}")
    print("User statement:")
    print(f"  {ticket.get('user_statement', 'No statement supplied.')}")
    actions = ticket.get("support_action_authority", [])
    print("Authorised Support actions:")
    if isinstance(actions, list) and actions:
        for action in actions:
            print(f"  - {action}")
    else:
        print("  - no change authority published; preserve evidence and ask a mentor")
    guidance = ticket.get("soc_escalation_guidance")
    if guidance:
        print("SOC handoff guidance:")
        print(f"  {guidance}")


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Display the current server-issued NeoLabs Support ticket queue")
    result.add_argument("--ticket", help="show one published ticket ID")
    result.add_argument("--json", action="store_true", help="print the student-safe queue as JSON")
    result.add_argument("--no-refresh", action="store_true", help=argparse.SUPPRESS)
    return result


def main() -> int:
    args = parser().parse_args()
    return run(args)


def run(args: argparse.Namespace) -> int:
    manifest, tickets = read_ticket_resource(refresh=not args.no_refresh)
    pod = str(manifest["pod_id"])
    resources = manifest["resources"]
    if args.ticket:
        tickets = [ticket for ticket in tickets if str(ticket.get("ticket_id", "")).lower() == args.ticket.lower()]
        if not tickets:
            fail("that ticket ID is not in your current server-issued queue")
    if args.json:
        print(json.dumps({"pod_id": pod, "scenario_id": manifest.get("scenario_id"), "tickets": tickets}, indent=2, sort_keys=True))
        return 0

    print("NEOLABS SUPPORT DESK — CURRENT ASSIGNMENT")
    print(f"Assigned pod: {pod}")
    print(f"Scenario:     {manifest.get('scenario_id') or resources.get('scenario_id') or 'not published'}")
    print(f"Queue run:    {resources.get('queue_run_id', 'not published')}")
    print(f"Cases:        {len(tickets)}")
    notice = resources.get("student_notice")
    if notice:
        print(f"Notice:       {notice}")
    for ticket in tickets:
        print_ticket(ticket)
    print("\nWORKFLOW: verify → record → preserve → triage → escalate when justified → recover only with authority → validate")
    print("Use the account reference + reported window + user/device context in your SOC escalation; do not tell SOC what conclusion to reach.")
    return 0


def course_entitlements(args: argparse.Namespace) -> None:
    """Display only a current ticket's server-issued course evidence projection."""
    manifest, tickets = read_ticket_resource(refresh=True)
    if manifest.get('scenario_id') != 'w04-broken-gate' or not re.fullmatch(r'pod-0[1-5]', manifest['pod_id']):
        fail('no current Week 4 course evidence is published for this assigned pod')
    ticket = next((item for item in tickets if item.get('ticket_id') == args.ticket), None)
    if ticket is None:
        fail('that ticket ID is not in your current server-issued queue')
    course = validate_course_evidence(manifest, ticket)
    print(json.dumps({'scenario_id': 'w04-broken-gate', 'pod_id': manifest['pod_id'],
                      'ticket_id': ticket['ticket_id'], 'account_reference': ticket['account_reference'],
                      'course_access': course,
                      'change_mode': 'proposed_or_simulated_only'}, indent=2, sort_keys=True))


def validate_course_evidence(manifest: dict[str, Any], ticket: dict[str, Any]) -> dict[str, Any]:
    course = ticket.get('course_access')
    if not isinstance(course, dict) or course.get('contract_version') != '1.0.0':
        fail('no approved course evidence is published for this ticket; do not infer course permissions from platform access')
    pod = manifest.get('pod_id')
    if (course.get('pod_id') != pod or course.get('scenario_id') != 'w04-broken-gate'
            or course.get('account_reference') != ticket.get('account_reference') or course.get('read_only') is not True):
        fail('course evidence failed the ticket/pod/scope check; stop and contact a mentor')
    if (course.get('enrolment_status') not in {'ACTIVE', 'SUSPENDED', 'REVOKED', 'NONE'}
            or course.get('course_role') not in {'LEARNER', 'INSTRUCTOR', 'NONE'}
            or not re.fullmatch(r'[A-Za-z0-9_-]{1,160}', str(course.get('course_id', '')))):
        fail('the server-issued course evidence is invalid')
    from datetime import datetime
    try:
        observed = datetime.fromisoformat(course['observed_at'].replace('Z', '+00:00'))
        if observed.tzinfo is None: raise ValueError('timezone required')
        for field in ('enrolment_starts_at', 'enrolment_ends_at'):
            if course.get(field) is not None:
                value = datetime.fromisoformat(course[field].replace('Z', '+00:00'))
                if value.tzinfo is None: raise ValueError('timezone required')
    except (KeyError, AttributeError, TypeError, ValueError):
        fail('course evidence is missing a trustworthy observation timestamp')
    # Explicit allowlist: mentor-only policy answers, secrets, arbitrary comments
    # and raw internal role/approval objects never enter this output.
    projected = {key: course[key] for key in ('contract_version', 'pod_id', 'scenario_id', 'account_reference',
                                             'course_id', 'enrolment_status', 'course_role', 'read_only', 'observed_at')}
    for field in ('enrolment_starts_at', 'enrolment_ends_at'):
        projected[field] = course.get(field)
    return projected


if __name__ == "__main__":
    raise SystemExit(main())
