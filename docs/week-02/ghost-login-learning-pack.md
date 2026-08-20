# Week 02 - The Ghost Login

**Track:** IT Security Support  
**Programme:** NeoLabs x Renaissance Innovation Labs Cybersecurity Internship  
**Classification:** Student Training Material - Authorised Synthetic Use Only

## Why this week matters

Many security incidents first appear as ordinary support requests: 'I cannot sign in', 'I received a login notice I do not recognise', 'my account is locked', or 'my password suddenly stopped working.' Support staff must restore legitimate access without destroying evidence or making an unsafe account change.

Week 2 teaches a secure support sequence: **verify, record, diagnose, preserve, recover only when authorised, escalate when suspicious, and validate the result.**

It also introduces the working relationship between IT Security Support and the SOC team. **Support owns the user-facing problem and first evidence. SOC owns the telemetry-based security investigation.** The two teams should exchange enough information to solve the case without duplicating work or destroying evidence.

## Learning outcomes

By the end of this pack you should be able to:

- prepare the supported Windows workstation for the Support toolkit;
- authenticate to the NeoLabs broker and identify the resources assigned to your server-controlled pod;
- use the Week 2 `tickets` command to retrieve the current pod-scoped synthetic support queue;
- collect a useful suspicious-login ticket without exposing credentials;
- distinguish an ordinary sign-in problem from indicators that require SOC escalation;
- verify a synthetic user through the approved lab procedure;
- preserve timestamps and contextual evidence before recovery actions;
- produce a focused Support-to-SOC escalation;
- carry out only the recovery/containment action authorised by the ticket;
- document account recovery and handoff clearly;
- validate that legitimate access works after the fixed scenario.

## 1. Set up your IT Security Support workstation

The Week 2 Support path uses the **Windows toolkit-local NeoLabs client**. You do not need a separate EC2/Wazuh server for this track.

### 1.1 Clone the toolkit

Open PowerShell and run:

```powershell
git clone https://github.com/NeoLabs-Security/RIL_NeoLabs-ITSEC-Support-Interns-Toolkit.git
cd RIL_NeoLabs-ITSEC-Support-Interns-Toolkit
```

If you already cloned it, update it from the toolkit folder:

```powershell
git pull origin main
```

### 1.2 Run the one-time Windows readiness check

From the toolkit root:

```powershell
.\setup-windows.cmd
```

The readiness check confirms:

- Python 3.10 or newer;
- Windows OpenSSH Client for the isolated live tunnel; and
- the toolkit-local NeoLabs launcher.

It does not require a global `pip install` or Python Scripts PATH changes.

If the check reports a missing prerequisite, install that prerequisite and run `setup-windows.cmd` again.

### 1.3 Sign in to the NeoLabs lab

Use only the toolkit-local commands:

```powershell
.\neolabs.cmd login
.\neolabs.cmd status
.\neolabs.cmd pod info
```

`login` asks for your assigned pod number and private NeoLabs Access Code. The server controls your actual pod, track and current resources.

Do not store the Access Code in notes, screenshots, Slack, GitHub or your assignment submission.

### 1.4 Check the current Support resources

```powershell
.\neolabs.cmd targets
```

During an approved live window, `connect` opens the restricted pod-isolated Support/learner surface:

```powershell
.\neolabs.cmd connect
```

The local learner/support surface is normally available at:

```text
http://localhost:18080
```

Keep the connection terminal open while using the live surface. Treat `targets` and the current assignment as the authority; never substitute an old IP, public EC2 address or another pod.

## 2. Use the Week 2 Support ticket queue

After NeoLabs login succeeds, retrieve the current queue with:

```powershell
.\neolabs.cmd tickets
```

The command refreshes the authenticated manifest and shows only the synthetic Support cases issued for your server-assigned pod. There is no student pod selector.

Each Week 2 queue contains a mixture of user reports. You may see cases labelled or described as:

- **routine** - likely ordinary support behaviour that still needs verification;
- **needs-triage** - not enough information yet to classify safely; and
- **security-review** - contains indicators that justify a focused SOC handoff.

The queue order can vary by pod. **Do not assume Ticket 1, Ticket 2 or Ticket 3 is always the suspicious case.** Read and triage every ticket from its facts.

A typical start-of-shift command sequence is:

```powershell
.\neolabs.cmd status
.\neolabs.cmd pod info
.\neolabs.cmd targets
.\neolabs.cmd tickets
```

Then use `connect` only when the ticket requires the live Support/learner surface.

## 3. Start with the user's report

A good support ticket captures facts before assumptions.

Record:

- ticket/case reference;
- synthetic user/account label when provided;
- time the user noticed the problem or notification;
- what the user was trying to do;
- exact error/notification wording where available;
- device/browser context if the exercise permits it;
- whether the user remembers a login at that time;
- whether access currently works;
- what troubleshooting or recovery has already been attempted.

Never ask the user to send a password through the ticket, Slack, email or screenshot.

## 4. Authentication problems are not all security incidents

Common non-malicious causes can include:

- mistyped credentials;
- browser/session confusion;
- account lockout after several mistakes;
- service availability or connectivity problems;
- expected login from another authorised lab client;
- a normal retry after an initial failed attempt.

Indicators that deserve escalation may include:

- an unfamiliar successful login the synthetic user cannot explain;
- a cluster of failures followed by a success that does not match the user's story;
- activity at a time inconsistent with the user's report;
- a source/device pattern the ticket cannot explain;
- multiple users reporting similar suspicious activity;
- evidence suggesting the account/session state changed without the user's authorised action.

Support does not need to prove the entire incident before escalating. Your job is to preserve useful facts and hand off a high-quality case.

## 5. Verify identity before account recovery

Use only the programme-approved synthetic verification process. In a real organisation this might involve approved identity checks or a managed help-desk procedure; in the VCC lab the mentor/ticket defines the verification method.

Do not improvise identity questions, request secrets in chat, or bypass verification simply because the user sounds urgent.

Record that verification succeeded; do not record secret answers.

## 6. Preserve evidence before changing the account

Before a reset, unlock or session termination, record the state requested by the exercise.

Useful items may include:

- reported timestamp/time window;
- current account or access status;
- device/browser context supplied by the user or approved Support surface;
- ticket reference;
- relevant error/notification wording;
- whether the user confirms, denies or is unsure about the login;
- any suspicious indicator that should be passed to SOC.

> **Evidence requirement:** Capture only what the ticket needs. Do not collect unrelated data from another pod or user.

## 7. How IT Security Support and SOC work together

Support and SOC are not competing investigators. They answer different parts of the same incident story.

### Support's role

Support should establish the user-facing facts:

- Who is reporting the issue?
- Has the synthetic identity been verified?
- What exactly did the user see?
- When did it happen?
- Does the user remember the login?
- Which approved device/browser context is relevant?
- Does access work now?
- What actions have already been taken?

Support should preserve these facts before destructive recovery.

### SOC's role

SOC should independently examine Wazuh telemetry to answer the security question:

- What authentication events occurred in that window?
- Were there failures, successes or session changes?
- Does the telemetry agree with the user's statement?
- Can related events be correlated by event time, account, `request_id`, `correlation_id` or session information?
- Is the case benign, suspicious, confirmed within the lab scenario, or still inconclusive?

Support should **not** tell SOC what conclusion to reach. A useful handoff asks SOC to investigate a question.

### Minimum Support-to-SOC handoff

Include:

```text
Ticket/case reference
Synthetic account reference, when supplied
Reported time window
User confirms / denies / is unsure about the login
Approved device/browser context
Current access/account state
Evidence already preserved
Actions already taken by Support
Specific question for SOC to answer
```

Example:

> Synthetic learner reports an unfamiliar successful-login notification during the stated Week 2 window and denies using VCC at that time. Identity verification completed. Device/browser context and current access state recorded. No destructive recovery performed. Please correlate authentication and session activity for this case and advise whether further containment is justified.

That is stronger than saying, "This is the Ghost Login." The SOC analyst must still verify the telemetry independently.

### Closing the loop

The intended relationship is:

```text
User report -> Support verifies and preserves ->
Support escalates focused facts -> SOC correlates telemetry ->
SOC returns finding/recommendation -> Support performs authorised recovery ->
Support validates the user-facing result and closes the ticket
```

## 8. Recovery and containment actions

Only perform the action explicitly authorised by the Week 2 ticket/Issue. Depending on the prepared scenario, that may include a synthetic password reset, approved session termination, account unlock or another controlled recovery step.

Before changing anything:

1. Confirm the target account/resource from `neolabs targets` and the ticket.
2. Confirm user verification is complete.
3. Record the original state.
4. Preserve the information SOC may need.
5. Confirm the action is authorised.
6. Know how you will validate success.
7. Know whether a rollback is possible or needed.

Do not disable security controls to make the problem disappear.

## 9. Documenting the recovery record

A useful recovery record contains:

| Field | Example content |
|---|---|
| Ticket | Week 2 synthetic ticket ID |
| Pod | Broker-returned pod |
| Account | Synthetic account label/reference |
| Verification | Completed using approved procedure |
| Original state | Active / inaccessible / session concern, as applicable |
| Evidence preserved | Timestamps, context, screenshot/event reference |
| Approved action | Exact recovery step authorised by ticket |
| Time | UTC timestamp |
| Validation | How restored access was confirmed |
| Escalation | SOC reference/result if suspicious activity was present |

Never place a password, Access Code or session secret in the recovery record.

## 10. Validation after recovery

Do not close a ticket just because a command or admin action returned 'success.' Validate the user-facing outcome.

Confirm:

- the synthetic user can perform the intended authorised login;
- expected access is restored;
- the user is not granted extra privileges;
- the suspicious condition has been handed to SOC when required;
- the SOC finding/recommendation has been reflected in the closure decision;
- the ticket contains enough information for another support analyst to understand what happened;
- the fixed-version scenario behaves as expected when released.

## 11. What Support should not do

- Do not clear logs to 'clean up' the incident.
- Do not delete suspicious evidence just to close a ticket.
- Do not reset an account before required evidence is captured.
- Do not request or store user passwords in support notes.
- Do not browse another pod's resources.
- Do not make an unauthorised firewall/service/security-control change.
- Do not diagnose the full security incident from Support data alone when SOC should investigate telemetry.
- Do not label a ticket as the exercise answer for SOC.

## 12. Week 2 operating sequence

```text
1. Clone/update the Support toolkit.
2. Run .\setup-windows.cmd once and fix any missing prerequisite it reports.
3. Run .\neolabs.cmd login with your pod number and private Access Code.
4. Confirm .\neolabs.cmd status and .\neolabs.cmd pod info.
5. Run .\neolabs.cmd targets to confirm current authorised resources.
6. Run .\neolabs.cmd tickets and triage the full pod-scoped queue.
7. Verify the synthetic user using the approved procedure.
8. Record the reported symptom, time window, context and current state.
9. Preserve relevant evidence before any destructive recovery.
10. Send a focused SOC escalation when the facts justify it.
11. Perform only the approved recovery action.
12. Validate user access and document the SOC handoff/result.
13. Retest after the fixed scenario is released.
14. Submit through the central assignment repository Pull Request workflow.
```

## Safety boundary

- Do not attempt to select another pod.
- Do not use a public EC2 address or guessed endpoint as a substitute for `neolabs targets`.
- Do not commit Access Codes, session tokens, passwords, private URLs or local runtime manifests.
- Do not collect unrelated user data.
- Stop and notify a mentor if another pod, real data, credentials/private keys, unexpected infrastructure access or service instability appears.

## Quick knowledge check

1. Which command retrieves your Week 2 pod-scoped Support queue?
2. Why should you triage every ticket instead of assuming one queue position is suspicious?
3. Why should Support preserve evidence before resetting an account?
4. Name five facts that belong in a Support-to-SOC escalation.
5. What part of the incident should SOC verify independently?
6. Why should a Support escalation ask a neutral question instead of naming the final conclusion?
7. What must be validated before closing the ticket?

## Remember

**Verify first. Preserve evidence. Triage the queue. Give SOC a focused lead. Change only with authority. Validate recovery.**
