# Module 5 - Asset, Software and Identity Operations

## Asset and software records

Every managed training asset should have a unique identifier, owner, purpose, operating system, criticality, location, support status and lifecycle state. Software records should capture product, version, source, approval status, support date and affected assets.

Interns compare observed state with the approved inventory. Unknown software or an unexplained privileged account is not automatically malicious, but it requires verification and possibly SOC escalation.

## Identity lifecycle

- onboarding: verified request, approved role, least privilege, MFA and documented handover;
- role change: review inherited and new access, remove unnecessary privileges;
- offboarding: disable access at the approved time, revoke sessions, recover assets and preserve records;
- access review: confirm owner, purpose, privilege, last use and approval;
- service accounts: named owner, non-interactive use where appropriate, controlled secret rotation and monitoring.

## Safety boundary

Interns do not create, disable, delete or reset accounts without an approved change. They never share administrator credentials or record passwords in tickets.

## Evidence

Record the request, approver, original state, intended entitlement, action taken by an authorised operator, validation and any residual access.

## Practice outcome

Given a synthetic inventory and access list, identify stale software, unsupported assets, dormant accounts, excess privilege and missing ownership, then prepare recommendations rather than making uncontrolled changes.

## Authoritative basis

CIS Controls v8.1 asset, software and account management safeguards; NIST NICE work-role concepts; Microsoft and Canonical identity administration guidance.