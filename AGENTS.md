# AGENTS.md — NeoLabs IT Security Support Toolkit

## Mission

Build beginner-to-intermediate learning materials, diagnostic resources and controlled remediation labs for secure endpoint, identity, network and service support.

## Non-negotiable boundaries

- Never add credentials, private keys, real user data, private infrastructure addresses or raw cohort evidence.
- Never create scripts that disable security controls, erase logs, delete evidence or make uncontrolled system changes.
- Diagnosis must be read-only by default.
- Remediation scripts require explicit confirmation, a documented change record, validation and rollback.
- Keep mentor ground truth, assignment details and answer keys outside this public repository.
- Suspected incidents must be escalated to the SOC workflow rather than treated as ordinary support failures.

## Content standard

- Preserve correct terminology and explain it before asking beginners to use it.
- Base guidance on NIST, CIS, Microsoft, Canonical, CISA and other primary sources.
- Separate symptom, evidence, hypothesis, root cause, corrective action and validation.
- Do not present a baseline as universally safe to apply without environment review.
- Every practical change must include impact, dependency, approval and rollback considerations.

## Code standard

- Prefer small, readable PowerShell, Bash and Python tools.
- Collect the minimum information necessary and warn when output may contain sensitive metadata.
- Fail safely when privileges, dependencies or scope are unclear.
- Do not upload reports automatically.
- Add syntax and safety validation in CI.

## Pull requests

Summarise learning changes, tooling changes, affected platforms, safety controls, tests performed, sources reviewed and remaining limitations.
