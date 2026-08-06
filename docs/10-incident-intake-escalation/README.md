# Module 10 - Security Incident Intake and SOC Escalation

## Purpose

IT Security Support is often the first team to hear that something unusual has happened. The intern must recognise possible incidents, preserve evidence, perform safe initial actions and hand the case to the SOC without treating it as an ordinary troubleshooting ticket.

## Learning outcomes

An intern should be able to:

- recognise common incident indicators;
- verify the reporter and affected asset;
- preserve logs, messages and system state;
- distinguish safe support containment from destructive action;
- record an incident intake clearly;
- escalate with priority, evidence and business context;
- support recovery after SOC direction.

## Possible incident indicators

Escalate when evidence suggests:

- unexpected account or administrator changes;
- unusual sign-ins or repeated MFA prompts;
- malware or suspicious persistence;
- security-control tampering;
- unexplained encryption, deletion or file changes;
- unusual data access or transfer;
- phishing or suspicious messages;
- unknown remote-access tools;
- lost or stolen devices;
- missing logs or unexplained service-account activity.

An indicator is not proof of compromise, but it changes the handling path.

## Intake workflow

1. Record the time the report was received.
2. Verify the reporter using the approved process.
3. Identify affected synthetic user, asset, service and location.
4. Record the symptom in the reporter's own words.
5. Ask what changed, when it began and what actions were already taken.
6. Preserve screenshots, message headers, filenames, timestamps and alert IDs as instructed.
7. Avoid clearing logs, deleting files or broadly resetting systems.
8. Classify urgency and impact.
9. Notify the SOC through the approved channel.
10. Continue only with actions approved by the incident lead.

## Evidence preservation

Record:

- source and collector;
- timestamp and time zone;
- asset and synthetic identity label;
- original location;
- collection method;
- checksum where appropriate;
- access restrictions;
- actions performed before collection;
- evidence ID referenced in the ticket.

Do not upload raw evidence to public repositories or general Slack channels.

## Safe initial actions

Depending on the scenario and approval, Support may:

- ask the user to stop interacting with the affected application;
- record current network and service state;
- preserve a suspicious message without opening links or attachments;
- document active sessions or account state;
- isolate a synthetic endpoint through the approved lab control;
- revoke a synthetic account session after SOC approval;
- prepare a replacement device or recovery environment.

Do not power off, wipe, reimage or delete artefacts unless the approved incident plan specifically requires it.

## Severity and priority

Consider:

- safety and service impact;
- number of affected users or assets;
- privilege of the affected account;
- sensitivity of data;
- ongoing activity;
- business criticality;
- containment already available;
- confidence and evidence quality.

## SOC handoff

A useful escalation contains:

- concise summary;
- affected asset and synthetic identity;
- start and report times;
- observed indicators;
- actions already taken;
- evidence IDs and restricted locations;
- current service state;
- business impact;
- urgent decisions needed;
- contact for follow-up.

## Communication

Do not promise that the issue is resolved or identify an attacker. Use factual language such as:

> We have recorded unusual activity and escalated it for security investigation. Please avoid further changes to the affected system until the incident lead provides instructions.

## Guided exercises

Complete synthetic tickets for:

- suspicious password-reset request;
- repeated MFA prompts;
- unknown privileged account;
- encrypted pre-commit files;
- suspicious email;
- lost lab device.

For each, decide what to preserve, what not to do, the priority and the SOC handoff.

## Authoritative basis

- NIST SP 800-61 Rev. 3 incident response recommendations and CSF 2.0 alignment.
- CIS Controls v8.1 Incident Response Management.
- CISA incident and phishing reporting guidance.
