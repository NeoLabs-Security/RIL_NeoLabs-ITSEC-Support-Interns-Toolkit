# NeoLabs IT Security Support Intern Toolkit

The **NeoLabs × RIL IT Security Support Toolkit** is the student-side **Learn + Connect + Operate** repository for secure endpoint, identity, network and service-support training through the VCC Security Lab.

It contains NeoLabs-branded learning material, read-only diagnostic helpers, synthetic tickets/recovery labs, change/rollback templates, SOC escalation resources and the NeoLabs pod-access client. Official weekly assignments and graded submissions belong in the separate central assignments repository.

## Current week

**Week 02 — The Ghost Login**

- Learning source: `docs/week-02/ghost-login-learning-pack.md`
- Branded PDF: `publications/NeoLabs_ITSEC_Support_Week_02_Ghost_Login.pdf`
- Practical task: issued through `RIL_NeoLabs-Intern-Assignments`

## Student flow

1. Read `START_HERE.md`, `SUPPORT_BOUNDARIES.md` and `LEARNING_PATH.md`, then install the repo CLI once with `python3 -m pip install --user -e .`.
2. Receive your pod number, stable NeoLabs lab URL and private NeoLabs Access Code.
3. Authenticate and inspect the current runtime:

```bash
neolabs login
neolabs connect
neolabs status
neolabs targets
```

4. When an interactive surface is active, diagnose only the endpoints/assets returned for your pod and ticket.
5. During replay windows, use:

```bash
neolabs replay
neolabs evidence
```

for pod-scoped archived telemetry and approved native evidence without requiring the main VCC EC2 to remain on.
6. Make a change only when the assignment/ticket explicitly authorises it.
7. Submit the requested ticket, recovery, escalation and validation evidence to `RIL_NeoLabs-Intern-Assignments`.

## Runtime states

- **LIVE** — VCC support endpoints/account workflows are available.
- **CLOUD_LIVE** — the approved S3/cloud support surface is active while the main VCC EC2 may be off.
- **ENDPOINT_LIVE** — the disposable Week 11 endpoint is active while the main VCC EC2 may be off.
- **REPLAY** — no interactive VCC change should be attempted; archived telemetry/evidence remains available for chronology, escalation and documentation.
- **OFFLINE** — no current practical surface is published.

## Why live endpoint data is not committed here

The VCC runtime may rebuild a pod with different endpoints. The deployment controller publishes current resources; the stable Replay Gateway mirrors those resources and runtime state. `neolabs connect` therefore knows whether the task is live or replay-only.

That keeps this public toolkit reusable and prevents an intern from applying an old endpoint from a previous live window.

## Toolkit contents

- secure support/ticket-handling foundations;
- Windows/Linux troubleshooting and security review;
- networking/connectivity diagnosis;
- asset/software/identity/access management;
- endpoint baseline and patch/remediation material;
- backup/restore/integrity/service-continuity practice;
- security-incident intake and SOC escalation;
- change/rollback/handover guidance;
- read-only Windows/Linux diagnostic collectors;
- pod-scoped replay/evidence download for offline investigation;
- synthetic tickets and recovery labs;
- professional support templates;
- NeoLabs-branded publication pipeline.

## Architecture boundary

**Toolkit repo:** Learn + Connect + Operate  
**Replay Gateway:** Stable Authentication + Runtime State + S3 Replay  
**VCC EC2:** On-demand Support Endpoints + VCC Scenario  
**Lab S3/Cloud:** Storage-native Weeks 7–9 + Archived Evidence  
**Disposable Endpoint:** Week 11 live endpoint only when required  
**Central Assignment repo:** Task + Evidence + Submission + Assessment

## Safety boundary

- Work only on resources returned by the current gateway manifest and explicitly authorised by the ticket/assignment.
- Prefer read-only diagnosis before changes.
- Obtain approval before changing accounts, permissions, firewall rules, services, packages or security controls.
- Never attempt live changes when `neolabs status` reports `REPLAY` or `OFFLINE`.
- Preserve the original state and rollback plan.
- Never disable security controls merely to make an error disappear.
- Never commit Access Codes, runtime manifests, private keys, real user data or unredacted evidence.
- Escalate suspected incidents to SOC rather than destroying evidence.
- Students never receive AWS credentials or bucket-wide S3 access.

## Release status

The toolkit on `main` contains the installable client, runtime-state-aware support resources, pod-scoped replay/evidence download, existing diagnostic helpers and the current branded Week 2 learning pack. Interactive support work depends only on the appropriate live surface being published; investigation/reporting can continue from S3 during approved replay windows.
