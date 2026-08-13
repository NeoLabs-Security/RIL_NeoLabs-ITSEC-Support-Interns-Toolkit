# Start Here — IT Security Support

This repository is the **NeoLabs × RIL IT Security Support Toolkit**. It contains the Week 1 learning material, read-only diagnostic helpers, templates and the student-side NeoLabs client.

Official weekly tasks and graded submissions belong in the separate **RIL_NeoLabs-Intern-Assignments** repository.

## Windows — start here

From this repository folder, double-click:

```text
setup-windows.cmd
```

The readiness check verifies the workstation prerequisites. Windows interns do **not** need to run `pip install`, edit the Python Scripts PATH or configure the programme gateway manually.

After the check passes, open PowerShell in this toolkit folder and confirm the local launcher works:

```powershell
.\neolabs.cmd --help
```

Then return to [`README.md`](README.md) and follow the current Week 1 sequence exactly.

## Before practical work

1. Read `SUPPORT_BOUNDARIES.md`.
2. Read the current Week 1 launch pack under `publications/`.
3. Have your assigned pod number and your private onboarding details ready.
4. Use only the local `neolabs.cmd` launcher shown in the current README.

## Support workflow

Begin with read-only diagnosis, preserve evidence, document the reported symptom and current state, obtain approval before making changes, validate the result and escalate suspected compromise instead of destroying evidence.

## Repository boundary

This public toolkit may contain reusable tools, synthetic tickets/labs, templates and NeoLabs-branded learning material. It must not contain Access Codes, session tokens, private keys, real user/device information, unredacted cohort evidence, mentor answer keys or production data.

The `runtime/` folder is ignored because it is regenerated from the server-issued context.

## Learning order

Follow `LEARNING_PATH.md`. Diagnosis, documentation, escalation and change control come before hardening or automation.
