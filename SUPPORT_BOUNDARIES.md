# IT Security Support Boundaries

Current runtime/access reference: [`PROGRAMME_CURRENT_STATE.md`](PROGRAMME_CURRENT_STATE.md).

## Default authority

Interns may inspect/document only the **current server-assigned training resource** and only when the current ticket/assignment authorises access. Read-only diagnosis is the default.

A pod number, old endpoint, screenshot, technically reachable service or another student's instructions do not create authority. The current central assignment + current NeoLabs manifest/resource are authoritative.

## Changes requiring explicit approval

Obtain explicit task/mentor approval before:

- creating, disabling, deleting or changing an account;
- resetting credentials/MFA or revoking sessions;
- changing group membership/permissions/entitlements;
- opening/closing firewall ports;
- installing/removing software or packages;
- starting/stopping/disabling services;
- changing security/logging/update/backup settings;
- editing scheduled tasks/startup/system-wide configuration;
- restoring/rolling back data/system state.

## Prohibited shortcuts

- disabling antivirus, firewall, logging, encryption or access controls merely to resolve a symptom;
- clearing logs/deleting suspicious artefacts;
- using shared administrator credentials;
- copying real user/production data into personal/public storage;
- making unrecorded changes;
- working on another pod/unassigned asset;
- substituting a public EC2/old endpoint when the current manifest does not publish it;
- presenting a successful command as proof the root cause is understood.

## Incident / stop indicators

Pause routine support and escalate when evidence suggests unauthorised account/privilege changes, malware/persistence, unusual authentication, unexpected data access/transfer, security-control tampering, unexplained log loss, administrator/service-account compromise, another pod/resource becoming visible, real data/credentials/private keys, unexpected infrastructure access or service instability.

## Change standard

Every approved change must record:

1. current authorised asset/resource and original state;
2. reason/expected outcome;
3. risk/dependencies;
4. approval;
5. implementation steps;
6. validation evidence;
7. rollback method;
8. final status/handover.

When compromise is suspected, preserve evidence and hand off to SOC before making routine-fix changes that could destroy evidence.
