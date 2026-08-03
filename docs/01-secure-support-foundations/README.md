# Module 1 — Secure IT Support Foundations

## Purpose

IT Security Support combines technical troubleshooting with protection of identities, devices, data and evidence. A successful fix is not acceptable if it creates unnecessary privilege, disables security controls, destroys logs or leaves the organization unable to explain what changed.

## Learning outcomes

An intern should be able to:

- verify the user and the support request before making changes;
- distinguish diagnosis, remediation, containment and escalation;
- document symptoms, evidence, hypotheses and actions;
- apply least privilege and separation of duties;
- recognize when a support ticket may be a security incident;
- prepare a change, validation and rollback plan;
- communicate clearly with users and the SOC team;
- close a ticket only after confirming the result.

## The secure support lifecycle

### 1. Intake

Record:

- who reported the issue;
- affected user, device and service;
- time first observed;
- business impact;
- error messages and screenshots;
- recent changes;
- whether suspicious activity is suspected.

Do not ask a user to send their password, MFA code, private key or full recovery key.

### 2. Identity and authority verification

Confirm that the requester is authorized to receive support for the account or device. Elevated access, account resets, permission changes and security-control changes require the approved authorization path.

### 3. Evidence-preserving diagnosis

Begin with read-only checks. Record current state before changing it. Prefer commands and tools that collect configuration, status and relevant logs without clearing, rotating or modifying them.

### 4. Classification

Classify the ticket as one of the following:

- routine service issue;
- configuration issue;
- account or access issue;
- suspected security incident;
- approved change request;
- recovery request;
- problem requiring escalation.

### 5. Remediation or escalation

Routine issues may follow an approved support runbook. Suspected compromise, unauthorized access, malware indicators, unexpected privilege, log tampering or cross-pod data exposure must be escalated to the SOC workflow before cleanup.

### 6. Validation

Confirm both functionality and security:

- Is the original issue resolved?
- Are expected security controls still active?
- Is access limited to the correct user or role?
- Are logs and monitoring still functioning?
- Did the change introduce a new error?

### 7. Closure and handover

Record the root cause when known, actions taken, approvals, evidence, validation result, unresolved risks and follow-up ownership.

## Core terminology

| Term | Working meaning |
|---|---|
| Symptom | What the user or technician observes. |
| Root cause | The underlying condition that produced the issue. |
| Workaround | A temporary method that restores use without resolving the root cause. |
| Remediation | A controlled change intended to correct the cause or reduce risk. |
| Containment | A temporary action that limits further harm during an incident. |
| Change | An approved modification to a system, service, account or configuration. |
| Rollback | The planned method for returning to the previous known state. |
| Validation | Evidence that the change produced the intended result without unacceptable side effects. |
| Escalation | Transfer to a person or team with the required authority or expertise. |

## Security incident indicators in support tickets

Escalate when a ticket includes:

- login notifications the user does not recognize;
- unexpected MFA prompts;
- new administrator accounts or privileges;
- antivirus or endpoint-security alerts;
- disabled firewall, logging or protection services;
- files encrypted, renamed or unexpectedly missing;
- suspicious email attachment execution;
- unauthorized software or remote-access tools;
- evidence involving another pod or user;
- requests to clear logs or conceal activity.

## Worked example

### Ticket

A user cannot access an approved internal web application.

### Weak response

Disable the firewall and retry.

### Secure response

1. Confirm the affected device, user and time.
2. Verify whether the issue affects one user, one device or the entire service.
3. Collect IP configuration, DNS resolution, route and connection-test results.
4. Check relevant client, firewall and application events.
5. Identify the failing layer.
6. Apply only an approved change with a rollback plan.
7. Confirm connectivity and verify that firewall protection remains enabled.

## Professional communication

Use language such as:

- “The evidence currently shows…”
- “The root cause is not yet confirmed.”
- “This action requires approval because it changes…”
- “The issue has been escalated to the SOC because…”
- “Service was restored and the following security controls were revalidated…”

Avoid blaming the user or claiming certainty that the evidence does not support.

## Review questions

1. Why should diagnosis begin with read-only checks?
2. When does a support ticket become a possible incident?
3. What must a rollback plan contain?
4. Why is disabling a firewall a poor default troubleshooting step?
5. What evidence is needed before closing a ticket?

## Authoritative basis

- NIST NICE Framework Components v2.2.0.
- NIST SP 800-61 Rev. 3.
- CIS Controls v8.1.
- NeoLabs `SUPPORT_BOUNDARIES.md` and `AGENTS.md`.
