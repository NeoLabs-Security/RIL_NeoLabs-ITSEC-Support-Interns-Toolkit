# Week 1 Launch Pack — Operation Night Watch

## Your objective

Verify that normal learner services work, practise evidence-preserving support and establish a support baseline for later security scenarios.

## Windows — start in this order

1. Pull the latest IT Security Support toolkit.
2. Run `setup-windows.cmd` once.
3. Open PowerShell in the toolkit folder and use:

```powershell
.\neolabs.cmd login
.\neolabs.cmd status
.\neolabs.cmd pod info
.\neolabs.cmd scope
.\neolabs.cmd targets
.\neolabs.cmd connect
```

Windows interns do **not** need a global `pip install`, PATH edit or manually entered gateway URL for the current programme flow.

The server controls the assigned pod/track/current support resource. During the approved Week 1 live window, keep `connect` running and use the restricted local learner/support surface, normally:

```text
http://localhost:18080
```

The internship learner app uses its normal email/password form; Google sign-in is intentionally disabled in internship pods.

If no current support endpoint is published, do not invent/reuse an IP/hostname or work on another pod. Wait for the approved window.

## Read before the task

- `START_HERE.md`
- `PROGRAMME_CURRENT_STATE.md`
- `SUPPORT_BOUNDARIES.md`
- `docs/01-secure-support-foundations/README.md`
- `docs/02-windows-diagnostics/README.md`
- `docs/03-linux-diagnostics/README.md`
- `docs/04-networking-decision-trees/README.md`
- support, handover and escalation templates in `templates/`

## Week 1 workflow

1. Confirm the current server-issued support endpoint and synthetic account/context.
2. Complete the normal learner workflow supplied in the assignment.
3. Verify approved functions such as sign-in, course/lesson access, projects/workspaces and approved downloads where present.
4. Work through the supplied onboarding/support ticket(s).
5. Separate browser/application symptoms from device, DNS, connectivity and account symptoms.
6. Preserve non-sensitive evidence before proposing corrective action.
7. Record symptom, evidence, diagnosis, action/recommendation, validation and escalation status.
8. Write one short knowledge-base article for a common Week 1 issue.

## Useful diagnostic resources

- `scripts/Collect-SystemBaseline.ps1`
- `scripts/collect-system-baseline.sh`
- networking decision trees
- support ticket template
- technical handover template
- SOC escalation template

Run diagnostics only on systems/resources the current assignment authorises. Do not change firewall, permissions, services, packages, accounts or security controls unless the task explicitly authorises the change.

## Deliverables

- completed setup/readiness checklist
- completed support ticket(s)
- `normal-service-check.md`
- one `knowledge-base-article.md`
- evidence references with secrets/private data removed

Official graded submissions go to `RIL_NeoLabs-Intern-Assignments`.

## Evidence standard

A support record should show what the user reported, what you observed, which diagnostic step produced the evidence, what changed (if anything), how the result was validated and whether escalation was required. Record the current server-issued resource rather than an old endpoint.

## Escalate instead of improvising when

- the symptom suggests compromise;
- another pod/resource becomes visible;
- real personal/production data or credentials appear;
- the fix requires an unapproved permission/account/firewall/service/package change;
- the endpoint is outside the current server-issued scope;
- unexpected infrastructure access or service instability appears.

## Before submission

- [ ] Current `status` shows the correct pod and SUPPORT track.
- [ ] Current `targets`/resource matches what I worked on.
- [ ] Week 1 local tunnel was used rather than an old/public target.
- [ ] Evidence was captured before changes/recommendations.
- [ ] Ticket notes distinguish symptom, diagnosis, action and validation.
- [ ] Any change was explicitly authorised with rollback/validation.
- [ ] One safe knowledge-base article is complete.
- [ ] Secrets/private data are redacted.
