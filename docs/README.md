# NeoLabs IT Security Support Documentation Index

Use this page as the learning-material map. For current connection/runtime behaviour read [`../PROGRAMME_CURRENT_STATE.md`](../PROGRAMME_CURRENT_STATE.md); follow [`../LEARNING_PATH.md`](../LEARNING_PATH.md); and read [`../SUPPORT_BOUNDARIES.md`](../SUPPORT_BOUNDARIES.md) before making any change.

## Current Week 1

- `week-01/operation-night-watch-launch-pack.md` — current setup/task flow
- `week-01/secure-support-foundations.md` — Week 1 foundations
- `week-01/support-ticket-01-normal-learner-access.md` — synthetic support ticket

On Windows, current programme setup is `setup-windows.cmd` once and then toolkit-local `.\neolabs.cmd` commands. Old global-CLI/manual-gateway examples are superseded. During Week 1, the restricted local learner/support surface is normally `http://localhost:18080` while `connect` is running and the current manifest publishes the resource.

## Core modules

- `01-secure-support-foundations/` — intake, verification, evidence, diagnosis and escalation
- `02-windows-diagnostics/` — Windows services/security/diagnostic workflow
- `03-linux-diagnostics/` — Linux users/services/SSH/firewall/packages/journals
- `04-networking-decision-trees/` — TCP/IP, DNS, DHCP, routing, ports, firewall/TLS diagnosis
- `05-asset-software-management/` — inventory/lifecycle
- `06-identity-access-operations/` — accounts/MFA/access review
- `08-patch-vulnerability-management/` — advisory review, prioritisation, change/rollback
- `09-backup-recovery/` — backup integrity/restore/RPO/RTO
- `10-incident-intake-escalation/` — security incident recognition/SOC handoff
- `11-cloud-saas-support/` — cloud/SaaS support
- `12-change-management-capstone/` — controlled change/handover/capstone; use only when released

## Practical resources

- `../scripts/` — read-only Windows/Linux baseline collectors and guarded helpers
- `../labs/` — synthetic diagnosis/recovery/support practice
- `../templates/` — tickets, access reviews, changes, escalation and handover
- `../troubleshooting/` — common platform/identity/network/recovery problems

Diagnosis is read-only by default. Live changes require the current assigned ticket/task, explicit approval, original-state evidence, rollback and validation. Technical reachability or an old endpoint is not authorisation.
