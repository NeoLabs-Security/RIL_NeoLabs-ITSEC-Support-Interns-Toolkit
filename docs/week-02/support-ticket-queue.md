# Week 02 Support Desk Queue — The Ghost Login

**Track:** IT Security Support  
**Classification:** Student Training Material — Authorised Synthetic Use Only

## What this queue is

For Week 2, the VCC scenario publishes a small synthetic support queue for your **server-assigned pod**. The reports are intentionally mixed: some may describe normal user mistakes, some are ambiguous, and at least one requires careful security review.

A ticket is a **user report, not proof of an incident**. Your job is to verify, record, preserve, triage and escalate only what the evidence justifies.

## Retrieve your assigned queue

From the Support toolkit folder on Windows:

```powershell
.\neolabs.cmd login
.\neolabs.cmd status
.\neolabs.cmd pod info
.\neolabs.cmd tickets
```

The `tickets` command refreshes your authenticated manifest before displaying the queue. There is **no pod selector** for tickets. The server-issued pod controls what you receive.

To reopen one ticket by ID:

```powershell
.\neolabs.cmd tickets --ticket W02-POD-01-A
```

Use the ticket ID actually displayed in your own queue. Do not copy another pod's example ID.

## What to record from each ticket

For every report, record:

- ticket ID;
- synthetic account reference;
- reported time/window;
- whether the user remembers the login;
- approved device/browser context;
- current access state;
- the user's exact statement in your own concise notes;
- what Support is authorised to do;
- whether the case should remain in Support or be escalated.

Do not request or record passwords, NeoLabs Access Codes, session tokens or certificates/private keys.

## How your work helps SOC

When escalation is justified, do **not** send SOC a conclusion such as “this is the Ghost Login.” Give the analyst a focused lead they can verify in Wazuh.

A strong handoff contains:

1. the synthetic account reference;
2. the reported investigation window;
3. whether the user confirms or denies the login;
4. approved device/browser context;
5. current account/access state;
6. evidence already preserved;
7. any recovery action already taken;
8. a specific question for SOC.

Example question:

> Please correlate authentication and session events for the supplied synthetic account inside the reported Week 2 window and determine whether the activity matches the user's account of events.

That gives SOC enough information to narrow the Wazuh search while preserving analyst independence.

## Triage mindset

### Routine report

A user remembers making a password mistake and later successfully authenticating. Record the sequence and verify current access. A failed login alone is not a security incident.

### Ambiguous report

The user is unsure whether a session expired normally or whether a browser state caused another login. Preserve context and decide whether additional facts justify escalation.

### Security-review report

The user reports a successful login they do not recognise or another meaningful authentication/account-state inconsistency. Verify the synthetic identity, preserve the report and escalate before destructive recovery.

The queue order varies by pod. Do not assume a particular queue position is the important case.

## Recovery boundary

Only perform actions explicitly authorised by the ticket/assignment. Preserve evidence before a reset, unlock or session termination. If the task requires SOC review before recovery, wait for that handoff step.

## Fixed-release validation

When mentors announce the fixed release, use the current queue and your original notes to validate the user-facing outcome. Confirm legitimate access works and record whether the previously concerning condition still appears from the Support perspective.

## Related learning material

Review these sections in `docs/week-02/ghost-login-learning-pack.md`:

- **Start with the user's report**
- **Authentication problems are not all security incidents**
- **Verify identity before account recovery**
- **Preserve evidence before changing the account**
- **Escalate to SOC when appropriate**
- **Recovery and containment actions**
- **Validation after recovery**

Also review `SUPPORT_BOUNDARIES.md` and the templates:

- `templates/support-ticket.md`
- `templates/soc-escalation.md`
- `templates/account-access-review.md`

## Stop conditions

Stop and contact a mentor if another pod's account appears, real personal data appears, credentials/secrets are exposed, a requested action is outside the written ticket authority, or a change could affect service stability.
