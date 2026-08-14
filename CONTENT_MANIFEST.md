# Content Manifest

| Material | Contents | Current status |
|---|---|---|
| Secure Support Foundations | intake, requester verification, evidence, diagnosis and escalation | Current |
| Windows Diagnostics | services, Defender, Firewall, BitLocker, updates and logs | Current |
| Linux Diagnostics | users, sudo, SSH, services, firewall, packages and journals | Current |
| Networking Decision Trees | TCP/IP, DNS, DHCP, routing, ports, firewall and TLS diagnosis | Current |
| Asset/Software Management | inventory, ownership, classification and lifecycle | Current |
| Identity/Access Operations | onboarding, role changes, offboarding, MFA and access review | Current |
| Patch/Vulnerability Management | advisory review, exposure, prioritisation, change/rollback | Current |
| Backup/Recovery | integrity, restore testing, RPO/RTO and continuity | Current |
| Incident Intake/Escalation | suspicious activity recognition, evidence preservation and SOC handoff | Current |
| Cloud/SaaS Support | cloud access/service troubleshooting foundations | Current |
| Change/Handover/Capstone | approval, validation, rollback, handover and capstone recovery | Current; capstone assignment-controlled |
| Read-only Collectors | Windows/Linux baseline collection | Current |
| Synthetic Support Labs/Tickets | evidence-first diagnosis/recovery practice | Current; later scenarios require release |
| Templates | tickets, access reviews, change, patch, recovery, escalation and handover | Current |
| VCC Pod Integration | server-assigned pod/resource, private Access Code, current target manifest and restricted local tunnel | Active programme path |

## Current operational path

The production training topology is five isolated pods. Windows students run `setup-windows.cmd` once and then use the toolkit-local `.\neolabs.cmd` commands. A global `pip install`, PATH edit or manually entered gateway URL is not required for the normal programme workflow.

For Week 1 Operation Night Watch, `connect` opens the authorised learner/support surface at `http://localhost:18080` while the current manifest publishes the resource. Google sign-in is intentionally disabled in internship pods. Old/cached endpoints are not continuing authorisation.

See [`PROGRAMME_CURRENT_STATE.md`](PROGRAMME_CURRENT_STATE.md).

## Safety/validation

- Read-only diagnosis is the default.
- Live changes require the current ticket/assignment, explicit authorisation, original-state evidence, rollback and validation.
- Student scope is server-authoritative and pod-isolated.
- CI checks source/syntax and prevents committed credential/private-key/destructive-control material.
- Student material contains no live Access Codes, mentor ground truth or real cohort evidence.

## Release rule

Later-week material can be staged before release. Presence of a guide/lab does not itself authorise practical activity; the current central assignment and current server-issued resource state are authoritative.
