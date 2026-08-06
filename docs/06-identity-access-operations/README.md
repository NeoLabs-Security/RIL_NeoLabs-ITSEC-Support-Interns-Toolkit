# Module 6 - Identity and Access Operations

## Purpose

This module teaches interns to support account lifecycles securely: onboarding, role changes, password and MFA support, privileged access review, temporary access and offboarding.

## Learning outcomes

An intern should be able to:

- verify the requester before performing an account action;
- distinguish authentication problems from authorisation problems;
- apply least privilege and separation of duties;
- document account creation, role changes and deactivation;
- support MFA without bypassing identity verification;
- recognise suspicious account activity and escalate to the SOC track;
- validate and record the final access state.

## Identity lifecycle

Use a controlled lifecycle:

`request -> verify -> approve -> provision -> validate -> review -> change or revoke -> close`

Every stage should be attributable to a ticket, approver and affected synthetic identity.

## Requester verification

Before a sensitive action:

- confirm the approved ticket or workflow;
- verify the requester using the programme-approved method;
- verify the target account and requested role;
- confirm the approver is authorised;
- avoid relying only on information supplied in the same message;
- stop and escalate if the request is unusual or inconsistent.

Interns must never request or view a user's password.

## Onboarding

Record:

- approved identity label;
- role and group membership;
- required applications;
- MFA enrolment status;
- temporary credentials delivery method;
- expiry for temporary access;
- manager or mentor approval;
- successful sign-in validation;
- review date.

## Role changes

A role change should not simply add new permissions. Review and remove access that is no longer needed. Confirm whether existing sessions, tokens, group memberships and shared resources must be updated.

## Password and MFA support

- verify identity before reset;
- use approved reset workflows;
- issue temporary access through a protected channel;
- require change or re-enrolment as designed;
- never disable MFA merely to close a ticket;
- record recovery method and validation;
- escalate unexpected MFA prompts or repeated reset requests.

## Privileged access

Privileged access requires stronger approval, a defined purpose and time limit. Record:

- privileged role;
- business or lab justification;
- approver;
- start and expiry time;
- actions permitted;
- review and revocation evidence.

Shared administrator credentials are prohibited.

## Offboarding

Offboarding should cover:

- account disablement or deletion policy;
- session and token revocation;
- group and application access;
- device return or reassignment;
- ownership transfer for files and services;
- secrets or keys issued to the identity;
- mailbox or record retention where approved;
- final validation and inventory update.

## Suspicious indicators

Pause routine support and escalate when evidence suggests:

- unexpected administrator membership;
- repeated MFA prompts not initiated by the user;
- impossible or unusual sign-in patterns;
- account recovery requests from an unverified source;
- access persisting after approved offboarding;
- new tokens, keys or service accounts without a change record;
- security-control or audit-log tampering.

Do not clear logs or make broad changes before SOC guidance.

## Guided exercise

Using synthetic tickets, complete:

1. one onboarding record;
2. one role-change review that removes obsolete access;
3. one MFA recovery request;
4. one privileged-access approval with expiry;
5. one offboarding checklist;
6. one SOC escalation for suspicious identity activity.

## Authoritative basis

- CIS Controls v8.1 Account Management and Access Control Management.
- NIST digital identity and NICE Framework concepts.
- Vendor identity-platform documentation for approved lab systems.
