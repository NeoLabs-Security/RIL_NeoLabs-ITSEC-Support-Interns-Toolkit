# Week 4 Student Runbook — IT Security Support | Broken Gate

**Scenario:** `w04-broken-gate` · **Pod:** server-assigned · **Track:** ITSEC/Support · **Mode:** read-only ticket investigation unless a mentor/operator separately approves and executes a change.

Read the detailed [course-access triage guide](course-access.md), [Support Boundaries](../../SUPPORT_BOUNDARIES.md) and [central submission handbook](https://github.com/NeoLabs-Security/RIL_NeoLabs-Intern-Assignments/blob/main/assignments/week-04/SUBMISSION_HANDBOOK.md).

## 1. Update and authenticate to the assigned pod

From the Support toolkit repository root on Linux:

```bash
cd ~/RIL_NeoLabs-ITSEC-Support-Interns-Toolkit
git pull --ff-only origin main
bash neolabs login
bash neolabs status
bash neolabs scope
bash neolabs tickets
```

On Windows PowerShell, run `.\neolabs.cmd login`, `.\neolabs.cmd status`, `.\neolabs.cmd scope` and `.\neolabs.cmd tickets` from the repository root. Do not invoke the bare `neolabs` command.

The login prompt requires the mentor-issued **Support** Access Code and assigned pod. There is **no student-profile password** required for the Support ticket reader; that separate credential belongs to the Pentest synthetic profile workflow. Never share or commit passwords, session tokens or Access Codes.

**Check**: the response must show your assigned pod and scenario `w04-broken-gate`. If the server has not published a queue or enrolment snapshot, report unavailable/pending, not resolved, and do not substitute another pod's tickets.

## 2. Read one assigned ticket and its course evidence

First list current tickets:

```bash
bash neolabs tickets
```

Copy an **exact ticket ID from your current queue** (no invented IDs):

```bash
TICKET="<published-ticket-id>"
bash neolabs tickets --ticket "$TICKET"
bash neolabs entitlements --ticket "$TICKET"
```

Optional structured ticket view:

```bash
bash neolabs tickets --json
```

On Windows PowerShell use `.\neolabs.cmd tickets --ticket <published-ticket-id>` and `.\neolabs.cmd entitlements --ticket <published-ticket-id>` with the same ticket ID.

The `entitlements --ticket` command retrieves the **read-only** server-provided Week 4 course evidence for that particular assigned ticket. It does not confer the right to select unrelated accounts or change a course enrolment.

## 3. Decision workflow

1. Record ticket ID, assigned pod, safe synthetic reporter alias, original UTC reporting window, account/course/resource IDs and approved evidence references.
2. Separate **platform entitlement** from **course enrolment**, **private assignment ownership** and **course instructor ownership**. An active platform entitlement does not automatically authorize a different course; course enrolment does not authorize another learner's private assignment.
3. Interpret dates and statuses. A revoked, suspended, expired, not-yet-started, or wrong-course enrolment may correctly produce a 403.
4. Decide whether the observed behavior is a **correct denial**, **legitimate missing access awaiting approved correction**, or **suspected unauthorized disclosure/security escalation**.
5. For a suspected violation, escalate to SOC with the **safe** actor alias, course/resource ID, UTC window, ticket ID and request/evidence ID; ask SOC to correlate rule `100141` / `100142`. Do **not** assert a violation from the ticket alone.
6. Record the proposed change, approver and rollback. The present Support toolkit **does not implement an authorized permission-changing action**; any actual change belongs to the approved mentor/operator process. Do not describe a proposed fix as completed.
7. Mark an outcome **PENDING** unless a separately authorized after-state or retest actually confirms it.

## 4. What Support should NOT do

- Do not impersonate a student, log into an unassigned course, or reuse Pentest student-profile credentials.
- Do not edit VCC's database, roles, permissions, enrolments or platform entitlements.
- Do not restart the API, reset accounts, block source IPs, delete evidence or force new security events.
- Do not attempt cross-pod ticket queries or inspect real personal data.

Support is an investigative/escalation track. It is **not required** to trigger Wazuh rules itself. Pentest generates approved activity; SOC correlates its telemetry; Support documents access symptoms, policy evidence and safe handoffs.

## 5. Deliverables and GitHub submission

Use `NeoLabs-Security/RIL_NeoLabs-Intern-Assignments`, branch `week-04/support/<github-username>-broken-gate`, under `submissions/week-04/support/<github-username>/`. Do not submit in this toolkit.

Include `ticket-resolution.md` (copy `assignments/week-04/templates/ticket-resolution.md`), `chronology.md`, `evidence-register.md`, and a short `kb-note.md`. Capture synthetic reporter and ticket, dated course evidence, policy reasoning, decision/approval status, escalation, recommended rollback, and observed outcome or `PENDING`.

Sanitize all evidence. Keep tokens, passwords, session files, private connection URLs, Access Codes, other pods' data and real identifying information out of Git commits. Open a PR against `main`, link your assigned Issue and leave the PR **unmerged** for mentor assessment.

See the [central submission handbook](https://github.com/NeoLabs-Security/RIL_NeoLabs-Intern-Assignments/blob/main/assignments/week-04/SUBMISSION_HANDBOOK.md) for exact Git commands and the submission checklist.
