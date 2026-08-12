# NeoLabs IT Security Support Intern Toolkit

The **NeoLabs × RIL IT Security Support Toolkit** is the student-side **Learn + Connect + Operate** repository for authorised secure support training through the VCC Security Lab.

## 🚀 WEEK 1 — START HERE

**Scenario:** Operation Night Watch  
**Goal:** verify normal learner services, practise evidence-preserving troubleshooting and establish a support baseline.

### 1. Read the current pack

- Source: [`docs/week-01/operation-night-watch-launch-pack.md`](docs/week-01/operation-night-watch-launch-pack.md)
- Branded PDF: [`publications/00_NeoLabs_ITSEC_Week_01_Launch_Pack.pdf`](publications/00_NeoLabs_ITSEC_Week_01_Launch_Pack.pdf)
- Boundaries: [`SUPPORT_BOUNDARIES.md`](SUPPORT_BOUNDARIES.md)

### 2. Install the NeoLabs client

```bash
python -m pip install -e .
```

### 3. Authenticate and inspect your authorised resources

Set the NeoLabs gateway URL supplied in your onboarding message, then run:

```bash
neolabs login
neolabs status
neolabs pod info
neolabs scope
neolabs targets
```

Work only with resources returned for **your assigned pod**. If no live support endpoint is published, do not invent or reuse an old address.

### 4. Complete Operation Night Watch

Use the Week 1 pack for the service checks, support ticket(s), evidence requirements and knowledge-base article. Official submissions belong in `RIL_NeoLabs-Intern-Assignments`.

## Week 1 study shelf

- `docs/01-secure-support-foundations/README.md`
- `docs/02-windows-diagnostics/README.md`
- `docs/03-linux-diagnostics/README.md`
- `docs/04-networking-decision-trees/README.md`
- templates under `templates/`

## What is preconfigured here

- installable `neolabs` authenticator/access client;
- server-managed pod/track/support-resource scope;
- Windows and Linux read-only baseline collectors;
- networking/connectivity decision trees;
- synthetic support/recovery exercises;
- support ticket, escalation, change and handover templates;
- branded educational/publication workflows.

## Repository map

```text
README.md                 ← you are here
docs/week-01/             ← current Week 1 instructions
publications/             ← branded student PDFs
tools/neolabs.py          ← pod access/authenticator client
scripts/                  ← read-only diagnostics
templates/                ← support/evidence/handover forms
labs/                     ← safe practice tickets/recovery
research/                 ← deeper reference material
```

## Safety boundary

- Prefer read-only diagnosis before changes.
- Work only on resources returned by the current gateway manifest and explicitly authorised by the task/ticket.
- Obtain approval before changing accounts, permissions, firewall rules, services, packages or security controls.
- Preserve original state and rollback information.
- Never commit Access Codes, runtime manifests, private keys, real user data or unredacted evidence.
- Escalate suspected compromise rather than destroying evidence.
- Stop if another pod, real personal data, a credential or unexpected infrastructure becomes visible.

**Toolkit:** Learn + Connect + Operate  
**VCC:** scheduled authorised support surface  
**Central Assignments:** submissions + assessment
