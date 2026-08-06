# NeoLabs IT Security Support Lab Catalogue

All labs use synthetic accounts, devices, files and tickets. Read-only diagnosis is the default. Any configuration change requires the supplied change record, approval, validation and rollback plan.

## Lab 1 - Secure Ticket Intake

- verify the synthetic requester;
- classify the issue;
- separate symptom from evidence;
- identify privacy and security concerns;
- produce a complete support ticket.

## Lab 2 - Windows Baseline Review

- run the approved read-only PowerShell collector;
- review system identity, services, updates, Defender, Firewall, BitLocker and recent events;
- identify three observations and their limitations;
- prepare one support action and one SOC escalation.

## Lab 3 - Linux Baseline Review

- run the approved read-only shell collector;
- review users, groups, sudo, services, SSH, packages, firewall and journal evidence;
- distinguish configuration drift from confirmed compromise;
- document recommended next steps.

## Lab 4 - Network Troubleshooting Decision Tree

Use synthetic DNS, routing and service symptoms to determine whether the failure is at the link, addressing, routing, DNS, port, TLS or application layer. Do not disable the firewall as a troubleshooting shortcut.

## Lab 5 - Asset and Software Inventory

- create an asset register from supplied baseline outputs;
- compare installed software with the approved list;
- identify stale, unsupported and unknown entries;
- prepare an inventory update, change request and exception record.

## Lab 6 - Identity Lifecycle

- complete onboarding;
- process a role change that removes obsolete access;
- support an MFA recovery request;
- approve temporary privileged access with expiry;
- complete offboarding and session revocation.

## Lab 7 - Patch and Vulnerability Remediation

- map synthetic advisories to assets;
- validate exposure;
- prioritise remediation;
- prepare backup, validation and rollback;
- record a simulated successful patch and one approved exception.

## Lab 8 - Backup and Restore Rehearsal

Run the guarded recovery script, verify checksums, restore to a separate directory and complete the backup/restore test record. A copied archive without a validated restore does not pass.

## Lab 9 - Incident Intake and SOC Handoff

Process synthetic cases involving repeated MFA prompts, an unknown privileged account, suspicious email, encrypted pre-commit files and missing logs. Preserve evidence and prepare the SOC escalation without deleting artefacts.

## Lab 10 - Cloud and SaaS Support

Diagnose synthetic application assignment, MFA, external sharing and service-status issues. Apply least privilege and prepare an escalation for an unexpected administrative role.

## Lab 11 - Approved Change and Rollback

- capture original state;
- confirm approval;
- implement the supplied reversible change in the isolated lab;
- validate service and security controls;
- trigger rollback when the supplied failure condition appears;
- complete the handover.

## Lab 12 - Red-Blue-Support Capstone

Grey-Box students confirm a bounded weakness, SOC students investigate the telemetry, and Support students remediate and restore service. The fixed release is retested and the pod produces a joint closure report.

## Release rule

VCC scenario details, private hostnames, credentials and answer keys are delivered through the central assignments system. This public catalogue contains only safe learning objectives and deliverables.
