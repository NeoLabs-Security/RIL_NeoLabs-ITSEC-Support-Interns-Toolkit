# Week 02 - The Ghost Login

**Track:** IT Security Support  
**Programme:** NeoLabs x Renaissance Innovation Labs Cybersecurity Internship  
**Classification:** Student Training Material - Authorised Synthetic Use Only

## Why this week matters

Many security incidents first appear as ordinary support requests: 'I cannot sign in', 'I received a login notice I do not recognise', 'my account is locked', or 'my password suddenly stopped working.' Support staff must restore legitimate access without destroying evidence or making an unsafe account change.

Week 2 teaches a secure support sequence: **verify, record, diagnose, preserve, recover only when authorised, escalate when suspicious, and validate the result.**

## Learning outcomes

By the end of this pack you should be able to:

- authenticate to the NeoLabs broker and identify the support resources assigned to your pod;
- collect a useful suspicious-login ticket without exposing credentials;
- distinguish an ordinary sign-in problem from indicators that require SOC escalation;
- verify a synthetic user through the approved lab procedure;
- preserve timestamps and contextual evidence before recovery actions;
- carry out only the recovery/containment action authorised by the ticket;
- document account recovery and handoff clearly;
- validate that legitimate access works after the fixed scenario.

## 1. Load the authorised support context

Before touching a system or account, load the resources for your assigned pod:

```bash
python3 tools/neolabs.py login
python3 tools/neolabs.py connect
python3 tools/neolabs.py status
python3 tools/neolabs.py targets
```

The broker returns only the endpoints/assets published for your pod and current scenario. The `runtime/` manifest is generated locally and is not committed to Git.

> **Change boundary:** An endpoint being reachable does not mean every change is authorised. The current ticket/GitHub Issue still determines what you may do.

## 2. Start with the user's report

A good support ticket captures facts before assumptions.

Record:

- synthetic user/account label;
- time the user noticed the problem or notification;
- what the user was trying to do;
- exact error/notification wording where available;
- device/browser context if the exercise permits it;
- whether the user remembers a login at that time;
- whether access currently works;
- what troubleshooting has already been attempted.

Never ask the user to send a password through the ticket, Slack, email or screenshot.

## 3. Authentication problems are not all security incidents

Common non-malicious causes can include:

- mistyped credentials;
- expired/changed synthetic password;
- browser/session confusion;
- account lockout after several mistakes;
- service availability or connectivity problems;
- expected login from another authorised lab client.

Indicators that deserve escalation may include:

- an unfamiliar successful login the synthetic user cannot explain;
- a cluster of failures followed by a success;
- activity at a time inconsistent with the user's report;
- a source/device pattern the ticket cannot explain;
- multiple users reporting similar suspicious activity;
- evidence suggesting the account state changed without the user's authorised action.

Support does not need to prove the entire incident before escalating. Your job is to preserve useful facts and hand off a high-quality case.

## 4. Verify identity before account recovery

Use only the programme-approved synthetic verification process. In a real organisation this might involve approved identity checks or a managed help-desk procedure; in the VCC lab the mentor/ticket defines the verification method.

Do not improvise identity questions, request secrets in chat, or bypass verification simply because the user sounds urgent.

Record that verification succeeded; do not record secret answers.

## 5. Preserve evidence before changing the account

Before a reset, unlock or session termination, record the state requested by the exercise.

Useful items may include:

- reported timestamp;
- current account status;
- recent authorised sign-in context shown by the support interface;
- ticket reference;
- relevant error message;
- any suspicious indicator that should be passed to SOC.

> **Evidence requirement:** Capture only what the ticket needs. Do not collect unrelated data from another pod or user.

## 6. Escalate to SOC when appropriate

A good SOC escalation answers:

- Who/which synthetic account is affected?
- What did the user report?
- When did it occur?
- Which endpoint/resource is involved?
- Which relevant evidence was preserved?
- What support action has already been taken?
- Is the user currently able to access the account?
- What question does Support need SOC to answer?

Example escalation language:

> Synthetic learner account reports an unfamiliar successful login at 14:18 UTC. Identity verification completed. No password was included in the ticket. Relevant timestamp and account-state evidence preserved. No destructive action taken. Request SOC review of authentication telemetry before further recovery steps.

## 7. Recovery and containment actions

Only perform the action explicitly authorised by the Week 2 ticket/Issue. Depending on the prepared scenario, that may include a synthetic password reset, approved session termination, account unlock or another controlled recovery step.

Before changing anything:

1. Confirm the target account/resource from `neolabs targets` and the ticket.
2. Confirm user verification is complete.
3. Record the original state.
4. Confirm the action is authorised.
5. Know how you will validate success.
6. Know whether a rollback is possible or needed.

Do not disable security controls to make the problem disappear.

## 8. Documenting the recovery record

A useful recovery record contains:

| Field | Example content |
|---|---|
| Ticket | Week 2 synthetic ticket ID |
| Pod | Broker-returned pod |
| Account | Synthetic account label |
| Verification | Completed using approved procedure |
| Original state | Locked / active / session present, as applicable |
| Approved action | Exact recovery step authorised by ticket |
| Time | UTC timestamp |
| Validation | How restored access was confirmed |
| Escalation | SOC reference if suspicious activity was present |

Never place the new password, access code or session secret in the recovery record.

## 9. Validation after recovery

Do not close a ticket just because a command or admin action returned 'success.' Validate the user-facing outcome.

Confirm:

- the synthetic user can perform the intended authorised login;
- expected access is restored;
- the user is not granted extra privileges;
- the suspicious condition has been handed to SOC when required;
- the ticket contains enough information for another support analyst to understand what happened;
- the fixed-version scenario behaves as expected when released.

## 10. What Support should not do

- Do not clear logs to 'clean up' the incident.
- Do not delete suspicious files/evidence just to close a ticket.
- Do not reset an account before required evidence is captured.
- Do not request or store user passwords in support notes.
- Do not browse another pod's resources.
- Do not make an unauthorised firewall/service/security-control change.
- Do not diagnose a security incident entirely alone when the SOC track should investigate telemetry.

## Week 2 operating sequence

```text
1. Read the GitHub Issue and assigned support ticket.
2. Study this learning pack.
3. Run neolabs login and neolabs connect.
4. Run neolabs targets to confirm the assigned resources.
5. Verify the synthetic user using the approved procedure.
6. Record the reported symptom/timestamps/current state.
7. Preserve relevant evidence.
8. Escalate suspicious activity to SOC when required.
9. Perform only the approved recovery action.
10. Validate user access and document closure/handoff.
11. Retest after the fixed scenario is released.
12. Submit through the central assignment repository Pull Request workflow.
```

## Quick knowledge check

1. Why should Support preserve evidence before resetting an account?
2. Name three facts that belong in a suspicious-login ticket.
3. When should a support case be escalated to SOC?
4. Why should a ticket never contain a user's password?
5. What must be validated before closing the ticket?

## Remember

**Verify first. Preserve evidence. Change only with authority. Escalate suspicion. Validate recovery.**
