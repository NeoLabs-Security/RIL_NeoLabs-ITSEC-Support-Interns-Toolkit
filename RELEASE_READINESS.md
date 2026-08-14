# IT Security Support Toolkit — Operational Readiness

**Status date:** 2026-08-14  
**State:** active programme baseline on `main`  
**Current assignment:** Week 01 — Operation Night Watch

Earlier release-candidate/operator-to-do notes are superseded by the active five-pod programme model in [`PROGRAMME_CURRENT_STATE.md`](PROGRAMME_CURRENT_STATE.md).

## Student-facing readiness

- [x] Start guide, current programme state, learning path and support boundaries
- [x] Secure support, Windows/Linux diagnostics and network decision trees
- [x] Asset/software/identity operations
- [x] Patch/vulnerability and backup/recovery guidance
- [x] Incident intake/SOC escalation and cloud/SaaS foundations
- [x] Change management, handover and capstone learning material
- [x] Troubleshooting, labs, synthetic tickets and templates
- [x] Week 1 launch pack/publications

## Tools/runtime readiness

- [x] Toolkit-local Windows NeoLabs launcher with official gateway preconfigured
- [x] Server-authoritative intern → track → pod/resource scope
- [x] Pod-isolated Week 1 local learner/support surface (`localhost:18080` while published)
- [x] Read-only Windows/Linux baseline collectors
- [x] Guarded synthetic recovery rehearsal
- [x] Credential/private-key boundary checks
- [x] Prohibited destructive/log-clearing/security-control disabling checks
- [x] Approval + validation + rollback required for changes

## Student operating rule

On Windows: run `setup-windows.cmd` once, then use `.\neolabs.cmd login/status/pod info/scope/targets/connect` from the toolkit folder. A global `pip install`, PATH edit or manual gateway configuration is not required.

Live VCC support work is permitted only while the current central assignment and server manifest expose the resource/window. An old endpoint or technically reachable system is not continuing authorisation.

## Current release decision

The toolkit is active for programme use. Week 1 is normal-service baseline/support practice. Later-week material can be staged before release; only the central assignment + current server state authorise practical work.

## Stop conditions

Do not continue when another pod/resource becomes visible, real personal/production data or credentials appear, the required change is not explicitly authorised, rollback/validation cannot be preserved, unexpected infrastructure becomes accessible or service stability is affected.
