# NeoLabs IT Security Support Intern Toolkit

The **NeoLabs × RIL IT Security Support Toolkit** is the student-side **Learn + Connect + Operate** repository for authorised secure support training through the VCC Security Lab.

## 🚀 WEEK 1 — START HERE

**Scenario:** Operation Night Watch  
**Goal:** verify normal learner services, practise evidence-preserving troubleshooting and establish a support baseline.

### 1. Read the current pack

1. [`publications/00_NeoLabs_ITSEC_Week_01_Launch_Pack.pdf`](publications/00_NeoLabs_ITSEC_Week_01_Launch_Pack.pdf) — exact Week 1 task and deliverables.
2. [`publications/01_NeoLabs_ITSEC_Week_01_Secure_Support_Foundations.pdf`](publications/01_NeoLabs_ITSEC_Week_01_Secure_Support_Foundations.pdf) — evidence-first support and diagnostic foundations.
3. [`SUPPORT_BOUNDARIES.md`](SUPPORT_BOUNDARIES.md) — mandatory safety/change boundary.

### 2. Windows setup — IMPORTANT

> **Windows interns: use ` .\neolabs.cmd ` — not `neolabs`.**  
> Run every NeoLabs command from inside this toolkit folder. Do not use bare `neolabs` and do not manually add the Python Scripts folder to PATH.

From the cloned toolkit folder, double-click:

```text
setup-windows.cmd
```

It checks that Python and the Windows OpenSSH Client are available. You do **not** need to run `pip install -e .`, edit PATH, or manually enter the NeoLabs gateway URL.

Then open PowerShell in this toolkit folder and test the launcher:

```powershell
.\neolabs.cmd --help
```

The launcher uses the official NeoLabs gateway automatically and runs the toolkit client with the Python installation Windows can find.

### 3. Authenticate and open your isolated live tunnel

Use these exact Windows commands:

```powershell
.\neolabs.cmd login
.\neolabs.cmd status
.\neolabs.cmd pod info
.\neolabs.cmd scope
.\neolabs.cmd targets
.\neolabs.cmd connect
```

`login` asks only for your assigned pod number and your private NeoLabs Access Code. For Week 1, `connect` opens a pod-isolated local connection. When prompted for the connection password, use the same private NeoLabs Access Code and keep that terminal open.

Your authorised learner/support surface is then available only at:

```text
http://localhost:18080
```

For the internship learner app, use the normal email-and-password form. Google sign-in is intentionally disabled in internship pods.

Work only with that server-issued local endpoint while the connection is running.

### 4. Complete Operation Night Watch

Use the Week 1 pack for the service checks, assigned synthetic support ticket, evidence requirements and knowledge-base article. Official submissions belong in `RIL_NeoLabs-Intern-Assignments`.

## Windows command reminder

```text
CORRECT:   .\neolabs.cmd login
CORRECT:   .\neolabs.cmd status
CORRECT:   .\neolabs.cmd connect

DO NOT USE: neolabs login
DO NOT USE: neolabs status
DO NOT USE: python tools\neolabs.py login --base-url ...
```

## Week 1 study shelf

- `docs/01-secure-support-foundations/README.md`
- `docs/02-windows-diagnostics/README.md`
- `docs/03-linux-diagnostics/README.md`
- `docs/04-networking-decision-trees/README.md`
- templates under `templates/`

## What is preconfigured here

- local Windows `neolabs.cmd` launcher with the official gateway preconfigured;
- Windows readiness check with no pip/PATH dependency;
- server-managed pod/track/support-resource scope;
- restricted pod-isolated connection workflow using the private Access Code;
- Windows and Linux read-only baseline collectors;
- networking/connectivity decision trees;
- synthetic support/recovery exercises;
- support ticket, escalation, change and handover templates;
- branded Week 1 launch/foundations PDFs.

## Repository map

```text
README.md                 ← you are here
setup-windows.cmd         ← one-click Windows readiness check
neolabs.cmd               ← use this for ALL Windows NeoLabs commands
neolabs.ps1               ← PowerShell launcher implementation
docs/week-01/             ← current task/foundations sources
publications/             ← branded student PDFs
tools/neolabs.py          ← underlying client
scripts/                  ← read-only diagnostics
templates/                ← support/evidence/handover forms
labs/                     ← safe practice tickets/recovery
research/                 ← deeper reference material
```

## Safety boundary

Prefer read-only diagnosis before changes. Work only on resources returned by the current gateway manifest and explicitly authorised by the task/ticket. Preserve original state and rollback information. Never share private access details or real user information. Stop and contact a mentor if another pod, real personal data, a credential, or unexpected infrastructure becomes visible.

**Toolkit:** Learn + Connect + Operate  
**VCC:** scheduled pod-isolated support surface  
**Central Assignments:** submissions + assessment
