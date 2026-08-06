# Module 8 - Security Incident Intake and SOC Escalation

## Purpose

Help support interns recognise when an ordinary service ticket may be a security incident and preserve evidence for the SOC team.

## Possible indicators

Unexpected account or group changes, suspicious sign-ins, malware alerts, unexplained encryption, disabled logging, unknown startup items, unusual data access, lost devices, repeated MFA prompts, or a user reporting activity they did not perform.

## First actions

1. Verify the reporter and affected asset.
2. Record exact time, symptom and user actions.
3. Preserve screenshots, alert identifiers and relevant read-only logs.
4. Avoid clearing logs, deleting files, reinstalling, resetting broadly or powering off unless the approved playbook requires it.
5. Escalate through the SOC channel with urgency and business impact.
6. Follow containment instructions from the authorised incident lead.

## Handover fields

Ticket ID, reporter, asset, identity, earliest known time, current state, observed indicators, actions already taken, evidence locations, service impact and contact details.

## Communication

Do not speculate or accuse. Tell the user what is known, what protective action is approved and when the next update will occur. Never publish evidence in public repositories or general Slack channels.

## Authoritative basis

NIST SP 800-61 Rev. 3, CISA incident-response guidance and the NeoLabs programme escalation process.