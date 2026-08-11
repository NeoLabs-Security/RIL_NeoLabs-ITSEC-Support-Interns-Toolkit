# Start Here — IT Security Support

This repository is the **NeoLabs × RIL IT Security Support Toolkit**. It provides branded learning material, read-only diagnostic helpers, recovery/change templates and the student-side client that reveals only the support resources assigned to your VCC pod.

Official weekly tasks and graded submissions belong in the separate **RIL_NeoLabs-Intern-Assignments** repository.

## Before practical work

1. Read `SUPPORT_BOUNDARIES.md`.
2. Set the programme-provided lab base URL as `NEOLABS_LAB_BASE_URL`.
3. Use the private pod number + NeoLabs Access Code delivered for the week.
4. Authenticate and load the current support context:

```bash
python3 tools/neolabs.py login
python3 tools/neolabs.py connect
python3 tools/neolabs.py status
python3 tools/neolabs.py targets
```

The broker decides which endpoints/assets belong to your pod. Do not hard-code a private IP or copy another pod's endpoint into a script.

## What `connect` does

- refreshes the current pod assignment from the NeoLabs broker;
- stores the live manifest in the ignored `runtime/` directory;
- exposes only the support endpoints/assets published for your pod and current scenario;
- lets the existing diagnostic/support scripts work from an authorised context without putting live addresses in this public repository.

## Support workflow

1. Confirm the assigned ticket/requester and the resource shown by `neolabs targets`.
2. Record the reported symptom and current state.
3. Begin with read-only inspection.
4. Preserve evidence relevant to the ticket.
5. Prepare rollback before a permitted change.
6. Obtain approval for changes affecting accounts, permissions, firewalls, services, packages, updates or security controls.
7. Validate the result and document anything unresolved.
8. Escalate suspected compromise to the SOC track rather than destroying evidence.

## Useful commands

```bash
python3 tools/neolabs.py pod info
python3 tools/neolabs.py targets
python3 tools/neolabs.py disconnect
```

## Repository boundary

This public toolkit may contain reusable tools, synthetic tickets/labs, templates and NeoLabs-branded learning material. It must not contain Access Codes, session tokens, private keys, real user/device information, unredacted cohort evidence, mentor answer keys or production data.

The `runtime/` folder is ignored because it is regenerated from the live server-issued manifest.

## Learning order

Follow `LEARNING_PATH.md`. Diagnosis, documentation, escalation and change control come before hardening or automation.
