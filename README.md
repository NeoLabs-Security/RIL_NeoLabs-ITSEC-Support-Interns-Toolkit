# NeoLabs IT Security Support Intern Toolkit

The **NeoLabs × RIL IT Security Support Toolkit** is the student-side **Learn + Connect + Operate** repository for authorised secure support training through the VCC Security Lab.

> **Current assignment:** Week 01 — Operation Night Watch.  
> **Current architecture/status:** [`PROGRAMME_CURRENT_STATE.md`](PROGRAMME_CURRENT_STATE.md)

## Week 1 objective

Verify normal learner services, practise evidence-preserving troubleshooting and establish a support baseline for later security scenarios.

Read first:

1. `publications/00_NeoLabs_ITSEC_Week_01_Launch_Pack.pdf`
2. `publications/01_NeoLabs_ITSEC_Week_01_Secure_Support_Foundations.pdf`
3. [`SUPPORT_BOUNDARIES.md`](SUPPORT_BOUNDARIES.md)

## Windows — current startup

From the latest toolkit checkout, double-click `setup-windows.cmd` once. Then open PowerShell in this toolkit folder and use:

```powershell
.\neolabs.cmd login
.\neolabs.cmd status
.\neolabs.cmd pod info
.\neolabs.cmd scope
.\neolabs.cmd targets
.\neolabs.cmd connect
```

Windows interns do **not** need a global `pip install`, Python Scripts PATH changes or a manually entered gateway URL. Do not use bare `neolabs` on Windows.

`login` asks only for the assigned pod number + private NeoLabs Access Code. The server controls pod/track/current support resources.

## Week 1 support surface

During the approved interactive window, `connect` opens the restricted pod-isolated learner/support surface, normally:

```text
http://localhost:18080
```

Keep the connection terminal open. The internship learner app uses its normal email/password form; Google sign-in is intentionally disabled in internship pods.

Confirm current `targets` before work. Never substitute the public EC2 address, an old endpoint or another pod. If no current support resource is published, wait for the approved window.

## Operation Night Watch workflow

1. Verify the current server-issued support endpoint/resource.
2. Verify the normal learner workflow and approved functions.
3. Work through the supplied synthetic support/onboarding ticket(s).
4. Separate browser/application symptoms from device, DNS, network and account symptoms.
5. Preserve non-sensitive evidence before proposing changes.
6. Record symptom, evidence, diagnosis, action/recommendation, validation and escalation status.
7. Write one short knowledge-base article for a common Week 1 issue.

Official graded submissions belong in `NeoLabs-Security/RIL_NeoLabs-Intern-Assignments`, not this toolkit.

## Change/safety boundary

Read-only diagnosis is the default. Do not change accounts, permissions, firewall rules, services, packages or security controls unless the current task explicitly authorises it. Preserve original state and rollback information. Stop/escalate suspected compromise, another pod/resource becoming visible, real personal/production data or credentials, unapproved privilege/configuration changes, unexpected infrastructure access or service instability.

## Repository map

```text
README.md                   ← current start page
PROGRAMME_CURRENT_STATE.md  ← current runtime/access reference
START_HERE.md               ← detailed onboarding
SUPPORT_BOUNDARIES.md        ← mandatory authority/change boundary
setup-windows.cmd           ← Windows readiness check
neolabs.cmd                 ← Windows toolkit-local launcher
docs/week-01/               ← current Week 1 sources
publications/               ← branded student PDFs
tools/neolabs.py            ← underlying access client
scripts/                    ← read-only diagnostics
templates/                  ← support/evidence/handover forms
labs/                       ← safe synthetic practice
```

**Toolkit:** Learn + Connect + Operate  
**VCC:** scheduled five-pod isolated support surface  
**Central Assignments:** submissions + assessment
