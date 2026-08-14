# Start Here — IT Security Support

This repository is the **NeoLabs × RIL IT Security Support Toolkit**. It contains learning material, read-only diagnostic helpers, templates and the student-side NeoLabs client. Official graded work belongs in `RIL_NeoLabs-Intern-Assignments`.

For current runtime/access behaviour read [`PROGRAMME_CURRENT_STATE.md`](PROGRAMME_CURRENT_STATE.md).

## Windows — start here

1. Pull the latest toolkit.
2. Double-click `setup-windows.cmd` once.
3. Open PowerShell in the toolkit folder and confirm:

```powershell
.\neolabs.cmd --help
```

Windows interns do **not** need a global `pip install`, Python Scripts PATH edit or manually configured gateway URL.

## Before practical work

1. Read `SUPPORT_BOUNDARIES.md` and the current central assignment.
2. Read the current Week 1 launch pack when working Operation Night Watch.
3. Authenticate/confirm the current server-issued assignment:

```powershell
.\neolabs.cmd login
.\neolabs.cmd status
.\neolabs.cmd pod info
.\neolabs.cmd scope
.\neolabs.cmd targets
.\neolabs.cmd connect
```

For Week 1, keep `connect` running and use the restricted local learner/support surface, normally `http://localhost:18080`. Never substitute a public EC2 IP, old endpoint or another pod.

## Support workflow

Begin with read-only diagnosis, preserve evidence, document reported symptom/current state, separate endpoint/network/identity/application causes, obtain approval before changes, record rollback information, validate the result and escalate suspected compromise rather than destroying evidence.

## Repository boundary

This public toolkit may contain reusable tools, synthetic tickets/labs, templates and learning material. It must not contain Access Codes, Wazuh/other passwords, session tokens, signed private URLs, private keys/certificates, real user/device information, unredacted cohort evidence, mentor answer keys or production data.

## Learning order

Follow `LEARNING_PATH.md`. Diagnosis, documentation, escalation and change control come before hardening/automation.

## Stop/escalate

Stop when another pod/resource becomes visible, real personal/production data or credentials appear, a change is outside the assigned ticket/approval, unexpected infrastructure becomes accessible or service stability is affected.
