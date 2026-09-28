# Week 3 arena — Blue response

Use this pack only while the central assignment explicitly opens `w03-credential-storm`.

1. Read [`arena-contract.yaml`](arena-contract.yaml) and the current assignment.
2. Read [`../../docs/week-03/credential-storm-blue-response-runbook.md`](../../docs/week-03/credential-storm-blue-response-runbook.md).
3. Accept containment requests only when they contain an in-scope synthetic account ID plus a SOC alert/event ID.
4. Record the original state, approval, action, UTC time, validation and rollback owner in the response ledger/change record.
5. Use only the approved responder interface issued for the event. Do not improvise AWS or server commands.
6. Validate a copied ledger offline with `python scripts/validate-week03-response-ledger.py PATH.csv`.

Student responders may request or perform the approved `contain-account` and exact-source `block-ip` actions. Recovery, unblocking, secret rotation, deployment and broad Security Group isolation remain facilitator/mentor-only.
