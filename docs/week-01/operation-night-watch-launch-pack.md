# Week 1 Launch Pack — Operation Night Watch

## Your objective
Verify that normal learner services work, practise evidence-preserving support and establish a support baseline for later security scenarios.

## Start in this order
1. Clone this IT Security Support toolkit repository.
2. In the repository folder install the NeoLabs CLI:

```bash
python -m pip install -e .
```

3. Set the NeoLabs lab gateway URL supplied in your onboarding message.
4. Authenticate with your assigned pod and private Access Code:

```bash
neolabs login
neolabs status
neolabs pod info
neolabs scope
```

5. Retrieve only the support resources the server has authorised:

```bash
neolabs targets
```

If the CLI reports that the endpoint is not yet published, do not invent an IP/hostname or work on another pod. Wait for the approved live window.

## Read before the task
- `START_HERE.md`
- `SUPPORT_BOUNDARIES.md`
- `docs/01-secure-support-foundations/README.md`
- `docs/02-windows-diagnostics/README.md`
- `docs/03-linux-diagnostics/README.md`
- `docs/04-networking-decision-trees/README.md`
- support, handover and escalation templates in `templates/`

## Week 1 workflow
1. Confirm the approved support endpoint and synthetic account.
2. Complete the normal learner workflow supplied in the assignment.
3. Verify approved functions such as sign-in, course/lesson access, projects/workspaces and approved downloads where present.
4. Work through the supplied onboarding/support ticket(s).
5. Separate browser/application symptoms from device, DNS, connectivity and account symptoms.
6. Preserve non-sensitive evidence before proposing a corrective action.
7. Record symptom, evidence, diagnosis, action/recommendation, validation and escalation status.
8. Write one short knowledge-base article for a common Week 1 issue.

## Useful diagnostic tools in this repository
- `scripts/Collect-SystemBaseline.ps1`
- `scripts/collect-system-baseline.sh`
- networking decision trees
- support ticket template
- technical handover template
- SOC escalation template

Run diagnostic scripts only on systems you are authorised to inspect. Do not change firewall, permissions, services or accounts unless the task explicitly authorises the change.

## Deliverables
- completed setup/readiness checklist
- completed support ticket(s)
- `normal-service-check.md`
- one `knowledge-base-article.md`
- evidence references with secrets and personal data removed

## Evidence standard
A support record should show what the user reported, what you observed, which diagnostic step produced the evidence, what changed (if anything), how you validated the result and whether escalation was required.

## Escalate instead of improvising when
- the symptom suggests compromise;
- another pod becomes visible;
- real personal data or credentials appear;
- the fix would require an unapproved permission/account/firewall/service change;
- the endpoint is outside the server-issued scope;
- service instability appears.

## Before submission
- [ ] `neolabs status` shows the correct pod and SUPPORT track.
- [ ] You used only the server-issued endpoint/resource.
- [ ] Evidence was captured before changes/recommendations.
- [ ] Ticket notes distinguish symptom, diagnosis, action and validation.
- [ ] One safe knowledge-base article is complete.
- [ ] Secrets and personal data are redacted.
