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
2. Receive your pod number and private NeoLabs Access Code.
3. Authenticate and load the live support context:

```bash
neolabs login
neolabs connect
neolabs status
neolabs targets
```

4. Diagnose only the endpoints/assets returned for your pod and ticket.
5. Make a change only when the assignment/ticket explicitly authorises it.
6. Submit the requested ticket, recovery, escalation and validation evidence to `RIL_NeoLabs-Intern-Assignments`.

## Why live endpoint data is not committed here

The VCC runtime may rebuild a pod with different internal/routable endpoints. The deployment controller publishes the current resources to the NeoLabs broker; `neolabs connect` refreshes them into ignored `runtime/access-manifest.json`.

That keeps this public toolkit reusable while still allowing authorised support work to receive the exact endpoints/assets needed for the current scenario.

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
- synthetic tickets and recovery labs;
- professional support templates;
- NeoLabs-branded publication pipeline.

## Architecture boundary

**Toolkit repo:** Learn + Connect + Operate  
**VCC Security Lab:** Assigned Systems + Scenario + Synthetic Data  
**Lab Access Broker:** Authenticate + Resolve Pod + Publish Support Resources  
**Central Assignment repo:** Task + Evidence + Submission + Assessment

## Safety boundary

- Work only on resources returned by the broker and explicitly authorised by the ticket/assignment.
- Prefer read-only diagnosis before changes.
- Obtain approval before changing accounts, permissions, firewall rules, services, packages or security controls.
- Preserve the original state and rollback plan.
- Never disable security controls merely to make an error disappear.
- Never commit Access Codes, runtime manifests, private keys, real user data or unredacted evidence.
- Escalate suspected incidents to SOC rather than destroying evidence.

## Release status

The toolkit on `main` contains the installable broker client, existing support helpers and the current branded Week 2 learning pack. Live VCC work still depends on the broker being deployed/enabled and current pod support resources being published by the operator pipeline.
