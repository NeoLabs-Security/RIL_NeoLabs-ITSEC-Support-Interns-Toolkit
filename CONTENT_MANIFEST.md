# Content Manifest

| Material | Planned contents | Status |
|---|---|---|
| Secure Support Foundations | ticket intake, verification, privacy, evidence, diagnosis and escalation | Module 1 complete; editorial review pending |
| Windows Support and Security | services, updates, Defender, Firewall, BitLocker, logs and baselines | Diagnostic handbook complete; practical QA pending |
| Linux Support and Security | users, permissions, sudo, SSH, packages, services, firewall and logs | Diagnostic handbook complete; practical QA pending |
| Networking and Connectivity | TCP/IP, DNS, DHCP, routing, ports, VPN and firewall diagnosis | Decision-tree handbook complete; platform labs pending |
| Asset and Software Management | inventories, ownership, lifecycle, approved software and disposal | Planned |
| Identity and Access Operations | onboarding, role changes, offboarding, MFA and privileged access | Account and access review template complete; module pending |
| Patch and Vulnerability Management | advisories, exposure, testing, deployment, exceptions and rollback | Foundations referenced; dedicated module pending |
| Backup and Recovery | backup design, integrity, restore testing and service continuity | Guarded synthetic backup/restore lab complete and CI-rehearsed |
| Incident Intake and SOC Escalation | suspicious activity, evidence preservation and handoff | Foundations and ticket scenarios complete; dedicated module pending |
| Change and Handover Management | approval, risk, implementation, validation, rollback and communication | Change request template complete; module pending |
| Diagnostic Tooling | read-only Windows and Linux baseline collectors | Initial collectors complete and syntax-validated |
| Synthetic Ticket Labs | endpoint, account, network, update, recovery and security scenarios | Six-ticket starter library complete |
| Templates | ticket, asset, change, rollback, restore, escalation and handover records | Ticket, access review and change request complete; remaining templates pending |

## Current validation

- Bash and PowerShell syntax validation.
- Synthetic backup archive, checksum and separate-directory restore rehearsal.
- File-count and manifest comparison after restoration.
- CI rejection of destructive shortcuts, log-clearing commands, security-control disabling and credential material.

## Publication rule

A student-facing material is approved only after technical review, safety review, source verification, lab validation, NeoLabs branding and Markdown/PDF quality assurance.
