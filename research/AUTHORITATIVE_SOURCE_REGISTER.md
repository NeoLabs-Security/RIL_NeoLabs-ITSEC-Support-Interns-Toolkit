# Authoritative Source Register — IT Security Support

Review date: 2026-08-02

Use current primary documentation and clearly separate vendor guidance, standards alignment and NeoLabs procedures.

## Workforce and operating model

| Source | Use in toolkit | Notes |
|---|---|---|
| NIST SP 800-181 Rev. 1 and NICE Framework Components v2.2.0 | task, knowledge and skill outcomes | Current components release announced April 2026 |
| NIST Cybersecurity Framework 2.0 | governance, protection, detection, response and recovery context | Use as organising context, not a technical checklist |
| NIST SP 800-61 Rev. 3 | incident intake, escalation, response and recovery integration | Final April 2025 |

## Baselines and operations

| Source | Use in toolkit | Notes |
|---|---|---|
| CIS Controls v8.1 | asset, software, configuration, account, vulnerability, logging, recovery and incident-response priorities | Current official control set |
| Microsoft Windows security documentation | Defender, Firewall, BitLocker, updates, event logs and security baselines | Verify procedures against the supported Windows release |
| Microsoft Security Compliance Toolkit documentation | baseline comparison and policy resources | Do not apply baselines blindly; assess environment and rollback |
| Ubuntu security documentation | updates, hardening, AppArmor, firewall, software integrity and common mistakes | Current Canonical documentation reviewed in 2026 |
| Ubuntu Server security guidance | layered server protection and operational hardening | Prefer supported LTS examples |

## Vulnerability and recovery

| Source | Use in toolkit | Notes |
|---|---|---|
| NIST vulnerability-management publications | remediation lifecycle and risk decisions | Select current final publications during module drafting |
| CISA vulnerability and patch guidance | operational prioritisation and remediation practice | Verify dated directives before publication |
| NIST data-integrity and recovery practice guides | backup, integrity and recovery exercises | Adapt only to synthetic training systems |

## Source-control rules

- Prefer official standards, operating-system vendors and primary project documentation.
- Record version and review date in each published module.
- Distinguish a secure baseline from an automatic change prescription.
- Every remediation exercise must include validation and rollback.
- Never copy live environment data, credentials or private configuration into this public repository.
