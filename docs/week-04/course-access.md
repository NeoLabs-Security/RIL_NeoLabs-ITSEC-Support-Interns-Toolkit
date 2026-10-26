# Broken Gate course access triage

Version 1.0.0. Reviewed 2026-10-23. Scenario: `w04-broken-gate`. Staged until the mentor publishes assigned tickets/evidence.

## Objectives

Verify a synthetic reporter, distinguish platform access from separate course enrolment/ownership, investigate expected and unexpected access, and select an authorized resolution or security escalation. Work individually; no competition or synchronized offensive/defensive session is required.

## Current commands

Use the existing Support access workflow from the repository root. On Linux:

```bash
bash neolabs login
bash neolabs status
bash neolabs tickets
bash neolabs tickets --ticket <published-ticket-id>
bash neolabs entitlements --ticket <published-ticket-id>
```

On Windows PowerShell use `.\neolabs.cmd` with the same arguments. Replace the angle-bracket value with an ID in your own current queue. There is no pod selector or unrestricted user lookup. Both ticket and course evidence lookups refresh existing server-authoritative access. Missing course evidence must be reported as unavailable, not treated as proof of membership or permission.

The read-only course evidence identifies the observed account/course, enrolment status, course role and observation time. Treat archived evidence as a snapshot, not a live recovery test. An ACTIVE status alone does not establish that an enrolment has started, remains unexpired or grants access to a private resource: request the authorized dated evidence where needed. Private assignment ownership and instructor scope require explicit policy evidence. Platform entitlement must never be modified as a shortcut for course enrolment.

## Case workflow and worked distinctions

1. Verify the reporter using only mentor-approved synthetic account attributes. Do not collect real identity documents or passwords.
2. Preserve ticket IDs, course/resource references, UTC times and safe evidence IDs. Separate symptom, observation, hypothesis and conclusion.
3. For missing access, compare the claimed membership with authoritative dated course evidence and the expected policy. A revoked or expired membership may explain a correct denial.
4. For unexpected successful access, preserve minimal evidence and escalate to SOC with actor/resource/window references. Do not pre-decide root cause or copy session tokens into the handoff.
5. A request for someone else's private assignment does not authorize transferring ownership. Ask for the required authority rather than changing data.
6. Record a proposed correction and seek the approved mentor/operator decision. This version does not execute permission changes; document simulation or mentor execution distinctly. Never treat a local role flag or copied approval text as authority.
7. Verify the outcome through a mentor-approved live check when available, or mark it pending. Record impact, authorization, before/after evidence, rollback plan and a short knowledge-base note.

## Review and limitations

Explain how a valid login can lead to a correct course denial. Which evidence would justify recovery rather than incident escalation? Which fields establish a course relationship, and what further evidence establishes private resource access? Do not report resolution merely because a ticket or UI label changed.

Unexpected infrastructure access, other-pod data, real data, credentials or instability require stopping and contacting a mentor. Use the central Week 4 ticket-resolution template and assignment Issue for deadlines and submissions. Sources: current Support boundaries, server-issued ticket authority, and [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).
