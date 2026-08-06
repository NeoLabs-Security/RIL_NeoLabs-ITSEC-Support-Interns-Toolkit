# Module 12 - Change Management, Handover and Capstone

## Purpose

Security support work is complete only when a change is authorised, implemented safely, validated, documented and handed over. This module combines the full track into an end-to-end capstone.

## Learning outcomes

An intern should be able to:

- prepare a clear change request;
- assess dependencies, impact and risk;
- define backup and rollback steps;
- obtain approval before implementation;
- validate technical and user outcomes;
- communicate status and residual issues;
- produce a complete support handover.

## Change lifecycle

`request -> assess -> approve -> prepare -> implement -> validate -> monitor -> close or roll back`

Each stage must be linked to a ticket and an accountable owner.

## Change request contents

- ticket and change ID;
- affected asset or service;
- current state and evidence;
- reason for change;
- proposed implementation;
- affected users and dependencies;
- security impact;
- backup or snapshot plan;
- validation plan;
- rollback triggers and steps;
- implementation window;
- approver;
- communication plan.

## Implementation standard

Before making the change:

1. verify the approved target;
2. capture the original state;
3. confirm backup or recovery path;
4. confirm required access and dependencies;
5. notify affected users where instructed;
6. perform only the approved steps;
7. record timestamps and outcomes;
8. stop if unexpected effects occur.

## Validation

Validate at several levels:

- configuration or version is correct;
- service is running and healthy;
- normal user workflow succeeds;
- security controls and logging remain enabled;
- monitoring shows no new critical errors;
- the original problem no longer occurs;
- affected users receive clear confirmation.

A command completing successfully is not enough.

## Rollback

Rollback when:

- validation fails;
- service health degrades;
- an unexpected dependency breaks;
- security controls are weakened;
- the approved window expires without a stable result;
- the mentor or change owner directs rollback.

Record the rollback result and do not hide a failed change.

## Handover

A technical handover should state:

- what was requested;
- what evidence was collected;
- what changed;
- current service state;
- validation performed;
- monitoring or follow-up required;
- known limitations;
- access or credentials to revoke through the approved process;
- related tickets and evidence IDs.

Do not place secrets in the handover.

## Track capstone

The capstone combines:

1. intake and requester verification;
2. read-only Windows or Linux baseline collection;
3. network or service diagnosis;
4. asset and software inventory review;
5. identity or access validation;
6. vulnerability or patch prioritisation;
7. backup and recovery preparation;
8. SOC escalation where suspicious indicators exist;
9. approved remediation;
10. validation, rollback readiness and handover.

## Cross-track workflow

- Grey-Box Pentesters provide a confirmed lab finding.
- SOC L1 analysts investigate the related telemetry.
- IT Security Support prepares and applies the approved remediation.
- Pentesters retest the fixed release.
- All three tracks contribute to the closure report.

## Capstone deliverables

- completed support ticket;
- system baseline;
- asset or identity review;
- change request;
- backup or rollback record;
- implementation log;
- validation evidence;
- SOC escalation where applicable;
- technical handover;
- reflection and lessons learned.

## Assessment rubric

| Area | Weight |
|---|---:|
| Scope, verification and security boundaries | 20% |
| Diagnosis and evidence | 20% |
| Change design and rollback | 15% |
| Safe implementation | 15% |
| Validation and recovery | 15% |
| Documentation and communication | 10% |
| Cross-track collaboration | 5% |

A serious unauthorised or evidence-destroying action overrides the numerical score.

## Authoritative basis

- NIST CSF 2.0 and SP 800-61 Rev. 3.
- CIS Controls v8.1.
- NICE Framework task, knowledge and skill concepts.
- Official platform change, recovery and security-baseline documentation.
