# NeoLabs × RIL IT Security Support — Current Programme State

**Operational baseline:** 2026-08-14  
**Current assignment:** Week 01 — Operation Night Watch  
**VCC topology:** five isolated pods (`pod-01` through `pod-05`)

This file is the current operational reference for the Support toolkit. Technical learning chapters remain valid unless they conflict with this file, the root README, `SUPPORT_BOUNDARIES.md`, the current central assignment or the server-issued manifest.

## Windows startup

Run `setup-windows.cmd` once from the latest toolkit checkout. Then use the toolkit-local launcher from PowerShell:

```powershell
.\neolabs.cmd login
.\neolabs.cmd status
.\neolabs.cmd pod info
.\neolabs.cmd scope
.\neolabs.cmd targets
.\neolabs.cmd connect
```

Windows interns do **not** need a global `pip install`, Python Scripts PATH changes or a manually entered gateway URL for the normal programme flow.

The server controls the intern → track → pod → current support resource mapping. Students do not choose another pod/resource by editing local files.

## Week 1 support surface

Operation Night Watch is a HYBRID baseline week. During the approved interactive window, `connect` opens a restricted pod-isolated local learner/support surface, normally:

```text
http://localhost:18080
```

Keep the connection terminal open. The learner application uses its normal email/password login; Google sign-in is intentionally disabled in internship pods.

If the current manifest does not publish a support resource, stop live-resource work. Never substitute the public EC2 address, an old endpoint or another pod.

## Week 1 intent

Verify normal learner services, work the assigned synthetic support/onboarding ticket(s), separate browser/application problems from device/DNS/network/account problems, preserve evidence before changes, and document symptom → evidence → diagnosis → action/recommendation → validation → escalation.

Read-only diagnosis is the default. Account, permission, firewall, service, package or security-control changes require explicit task/mentor authorisation plus rollback/validation information.

## Twelve-week support arc

| Week | Scenario | Main support emphasis |
|---|---|---|
| 01 | Operation Night Watch | normal service baseline + evidence-first support |
| 02 | Ghost Login | login/reset/session support and identity verification |
| 03 | Credential Storm | lockout/reset/recovery/session revocation handoff |
| 04 | Broken Gate | permissions/entitlement diagnosis and correction |
| 05 | Poisoned Upload | upload/quarantine/recovery support |
| 06 | Web Breach | containment communication, restore and patch validation |
| 07 | Cloud Locker | cloud access/IAM policy troubleshooting |
| 08 | S3 Insider Trail | containment/access review |
| 09 | Data Escape | credential rotation, permissions and recovery |
| 10 | Hidden Endpoint | API/service dependency troubleshooting |
| 11 | Developer Ransomware Drill | isolate/preserve/restore/backup validation |
| 12 | Blackout at VCC | recovery coordination, incident handoff and service validation |

Later-week content can be staged before release. Only the current assignment and server-issued resource state authorise practical work.

## Safety precedence

`SUPPORT_BOUNDARIES.md` + current central assignment + current server manifest are authoritative. Stop/escalate suspected compromise, another pod/resource becoming visible, real data/credentials, unapproved privilege/configuration changes, unexpected infrastructure access or service instability.
