# NeoLabs IT Security Support Intern Toolkit

The **NeoLabs × RIL IT Security Support Toolkit** is the student-side **Learn + Connect + Operate** repository for authorised secure support training through the VCC Security Lab.

> **Current assignment:** Week 02 — Ghost Login / Unfamiliar Login: Identity, Recovery & Escalation.  
> **Current architecture/status:** [`PROGRAMME_CURRENT_STATE.md`](PROGRAMME_CURRENT_STATE.md)

## Week 2 objective

Work from synthetic identity-and-access support tickets, verify what the user actually reported, preserve useful evidence, distinguish routine support symptoms from security-relevant signals, escalate to SOC when justified, and perform only explicitly authorised recovery actions.

Read first:

1. [`publications/NeoLabs_ITSEC_Support_Week_02_Ghost_Login.pdf`](publications/NeoLabs_ITSEC_Support_Week_02_Ghost_Login.pdf)
2. [`SUPPORT_BOUNDARIES.md`](SUPPORT_BOUNDARIES.md)
3. [`docs/06-identity-access-operations/`](docs/06-identity-access-operations/)
4. [`docs/10-incident-intake-escalation/`](docs/10-incident-intake-escalation/)

Week 1 materials remain useful as the secure-support baseline, but the current scenario and ticket queue are server-issued for Week 2.

## Windows — run from the toolkit folder

From the latest toolkit checkout, double-click `setup-windows.cmd` once. Then open PowerShell **in the root of this toolkit folder — the folder that contains `neolabs.cmd`**.

You do not need to enter the `tools` folder and you do not need a global `neolabs` installation. The launcher resolves its own scripts relative to the toolkit directory.

Use:

```powershell
.\neolabs.cmd login
.\neolabs.cmd status
.\neolabs.cmd pod info
.\neolabs.cmd scope
.\neolabs.cmd tickets
```

For live resources when the current lab state permits them:

```powershell
.\neolabs.cmd targets
.\neolabs.cmd connect
```

Windows interns do **not** need a global `pip install`, Python Scripts PATH changes or a manually entered gateway URL. Do not use bare `neolabs` on Windows.

`login` asks for the assigned pod number + private NeoLabs Access Code. The server controls the pod, track, current scenario and Support resources.

### Week 2 ticket queue

After a successful NeoLabs login, run:

```powershell
.\neolabs.cmd tickets
```

The command refreshes the authenticated server-issued manifest and displays only the **current pod-scoped IT Security Support tickets** assigned to that intern. There is no student-side pod selector.

Useful options:

```powershell
.\neolabs.cmd tickets --ticket W02-POD-01-A
.\neolabs.cmd tickets --json
```

If the toolkit reports that no Support tickets are published yet, do not substitute old Week 1 resources or another pod. Confirm the current release state or contact a mentor.

## Week 2 Support workflow

1. Run `.\neolabs.cmd status` and confirm the current server-issued scenario/pod.
2. Run `.\neolabs.cmd tickets` and read the assigned synthetic queue.
3. Verify the reporter, account reference, reported time window, device/browser context and current access state.
4. Preserve relevant non-sensitive evidence before proposing changes.
5. Separate symptom, evidence, hypothesis and conclusion.
6. Escalate to SOC when the ticket indicates unexplained authentication or a security-relevant account/session inconsistency.
7. Send SOC the account reference, reported window and useful context — **not a pre-decided conclusion**.
8. Perform recovery only when the ticket/task explicitly authorises it, then validate the result.
9. Record the case outcome and escalation status in the required assignment deliverable.

Official graded submissions belong in `NeoLabs-Security/RIL_NeoLabs-Intern-Assignments`, not this toolkit.

## Change/safety boundary

Read-only diagnosis is the default. Do not change accounts, permissions, firewall rules, services, packages or security controls unless the current task explicitly authorises it. Preserve original state and rollback information. Stop/escalate suspected compromise, another pod/resource becoming visible, real personal/production data or credentials, unapproved privilege/configuration changes, unexpected infrastructure access or service instability.

## Repository map

```text
README.md                   ← current start page
PROGRAMME_CURRENT_STATE.md  ← current runtime/access reference
START_HERE.md               ← detailed onboarding
SUPPORT_BOUNDARIES.md       ← mandatory authority/change boundary
setup-windows.cmd           ← Windows readiness check
neolabs.cmd                 ← Windows toolkit-local launcher
tools/neolabs.py            ← authenticated access client
tools/support_tickets.py    ← current pod-scoped ticket viewer
publications/               ← branded student PDFs
scripts/                    ← read-only diagnostics
templates/                  ← support/evidence/handover forms
labs/                       ← safe synthetic practice
```

**Toolkit:** Learn + Connect + Operate  
**VCC:** scheduled five-pod isolated support surface  
**Central Assignments:** submissions + assessment
