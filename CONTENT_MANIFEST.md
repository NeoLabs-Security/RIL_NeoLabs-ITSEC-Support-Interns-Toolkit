# Content Manifest

| Material | Contents | Version 1 status |
|---|---|---|
| Secure Support Foundations | ticket intake, requester verification, privacy, evidence, diagnosis and escalation | Complete |
| Windows Support and Security | services, updates, Defender, Firewall, BitLocker, logs and baselines | Complete |
| Linux Support and Security | users, permissions, sudo, SSH, packages, services, firewall and logs | Complete |
| Networking and Connectivity | TCP/IP, DNS, DHCP, routing, ports, VPN, TLS and firewall diagnosis | Complete |
| Asset and Software Management | inventories, ownership, lifecycle, approved software and disposal | Complete |
| Identity and Access Operations | onboarding, role changes, offboarding, MFA and privileged access | Complete |
| Patch and Vulnerability Management | advisories, exposure, testing, deployment, exceptions and rollback | Complete |
| Backup and Recovery | design, integrity, restore testing, ransomware readiness and service continuity | Complete with guarded rehearsal |
| Incident Intake and SOC Escalation | suspicious activity, evidence preservation, safe initial action and handoff | Complete |
| Cloud and SaaS Support | cloud identity, service status, file sharing, audit records and recovery | Complete |
| Change and Handover Management | approval, risk, implementation, validation, rollback and communication | Complete with capstone |
| Diagnostic Tooling | read-only Windows and Linux baseline collectors | Complete for Version 1 |
| Synthetic Ticket Labs | endpoint, identity, network, update, recovery and security scenarios | Starter library and twelve-lab catalogue complete |
| Templates | ticket, access, asset, change, patch, restore, escalation and handover records | Complete |
| Troubleshooting | Git, collectors, network, identity, recovery, patching and incident escalation | Complete |

## Current validation

- Bash and PowerShell syntax validation.
- Synthetic backup archive, checksum and separate-directory restore rehearsal.
- File-count and manifest comparison after restoration.
- CI rejection of destructive shortcuts, log-clearing commands, security-control disabling and credential material.
- Student-facing content contains no real users, credentials, private infrastructure or mentor answer keys.

## Publication rule

Version 1 is student-ready after the release PR passes CI and is merged. Changes to live accounts, services, packages, permissions, firewalls, backups or security controls remain subject to an assigned ticket, explicit approval, validation and rollback.
