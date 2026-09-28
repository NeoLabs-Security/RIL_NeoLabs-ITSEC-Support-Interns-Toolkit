# Week 03 — Credential Storm Blue response runbook

**Version:** 1.0  
**Reviewed:** 2026-09-28  
**Classification:** authorised synthetic training only

## Objective

Turn a SOC-authenticated signal into a controlled, auditable response without exposing infrastructure credentials. The event uses two separate responder identities:

- an AWS least-privilege responder identity for facilitator-approved Security Group actions; and
- an arena application responder identity for exact account containment on the dedicated server.

Credentials and resource identifiers are issued privately at event time and are never committed to this toolkit.

## Standard account-containment workflow

1. **Intake:** require the exact synthetic account ID, SOC alert/event ID, UTC observation time and analyst name.
2. **Validate:** confirm the ID is `syn-credential-storm-pod-01-01` through `-15` and the central assignment is active.
3. **Record:** write the current state and requested action in the change record.
4. **Approve:** obtain the event’s required responder/facilitator approval.
5. **Contain:** use the approved responder interface for the exact account. Do not use database, container or host access.
6. **Verify:** confirm the account is contained and record the response event ID and UTC completion time.
7. **Notify:** return the result to SOC so it can correlate containment with later authentication events.
8. **Recover:** only the facilitator performs recovery/reset after the scoring window; record validation and rollback completion.

## Exact-source firewall response

An IP block is secondary to account containment. It is allowed only when the source is supported by SOC evidence, is a single valid IP, is not an approved participant/monitoring address, and the event approval path permits it. Use the event’s approved responder interface and record the rule/change ID. Never widen a rule, block a network range or edit the host firewall directly.

## AWS Security Group emergency isolation

Broad Security Group isolation is a facilitator-only emergency action for service instability, out-of-scope traffic or loss of control. The custom IAM identity should allow only the specifically tagged arena Security Group and only the documented ingress revoke/restore operations. It must not permit instance termination, IAM changes, credential creation, broad resource discovery or changes to other Security Groups. Every action requires original-rule evidence, approval, a change ID, validation and an explicit rollback owner.

## Decision table

| Condition | Student response | Escalation |
|---|---|---|
| Valid account + SOC event ID | Approved account containment | Notify SOC |
| Exact suspicious source + approval | Approved single-IP block | Notify facilitator and SOC |
| Missing alert/event ID | No change | Return to SOC |
| Out-of-scope ID or real data | Stop | Facilitator immediately |
| Service instability/external traffic | Preserve evidence; no ad-hoc fix | Facilitator emergency isolation |
| Recovery/unblock/reset request | No student action | Facilitator |

## Common mistakes

- acting from a chat message without an alert/event ID;
- failing to record original state and rollback owner;
- using broad AWS privileges for convenience;
- blocking a whole CIDR when one source IP is evidenced;
- resetting an account during the scoring window;
- treating containment confirmation as proof of a Blue point without SOC timing correlation.

## Exercise

Complete a dry-run change record for one synthetic account, including approval, validation and rollback fields. Do not perform a live change. Have SOC verify that the response record contains enough information to correlate with its timeline.

## References

- NIST SP 800-61 Rev. 2, Computer Security Incident Handling Guide.
- AWS IAM documentation, least privilege and policy conditions.
- AWS Security Groups documentation, rule changes and referencing.
- CISA, incident response playbooks and operational guidance.
