# Module 11 - Cloud and SaaS Security Support Foundations

## Purpose

Modern support work includes cloud identities, shared files, SaaS applications and remotely managed devices. This module teaches interns to troubleshoot those services without assuming they control the underlying cloud platform.

## Learning outcomes

An intern should be able to:

- explain shared responsibility at a practical support level;
- support cloud sign-in, MFA, group and file-sharing issues;
- distinguish user, device, network and service causes;
- recognise risky sharing and excessive permissions;
- use audit records and service status information safely;
- escalate platform, security or data-governance issues.

## Shared responsibility

The service provider secures parts of the underlying platform, while the customer remains responsible for areas such as identities, access decisions, data handling, device security and configuration. Exact responsibilities depend on the service model and contract.

Do not assume that using a cloud service automatically makes an account, file or application secure.

## Cloud identity support

Common tasks include:

- account activation;
- MFA enrolment and recovery;
- group and role assignment;
- application access;
- device registration;
- session revocation;
- offboarding.

Apply the identity-verification and approval requirements from Module 6.

## Secure file sharing

Before changing access, record:

- owner;
- data classification;
- intended recipients;
- internal or external sharing requirement;
- permission level;
- expiry date;
- download or resharing controls where available;
- approval.

Prefer the least privilege needed. Public links and unrestricted external sharing require explicit approval.

## Troubleshooting decision path

1. Check service status through the approved source.
2. Verify the user and assigned application licence.
3. Confirm sign-in and MFA state.
4. Check group, role and application assignment.
5. Verify device and browser requirements.
6. Check network, DNS, proxy and time synchronisation.
7. Review non-sensitive audit events available to the assigned role.
8. reproduce with a synthetic test account where authorised;
9. escalate platform-wide, suspicious or data-governance issues.

## Audit records

Cloud audit records may show:

- sign-in result and reason;
- source context;
- MFA requirement;
- role or group changes;
- file sharing and access;
- application consent;
- administrative actions;
- session revocation.

Support interns collect only records needed for the ticket. Suspicious activity goes to the SOC track.

## SaaS account recovery

Recovery must not become an identity bypass. Verify the requester, use approved recovery methods, record changes and confirm that old sessions or recovery methods are handled as designed.

## Common mistakes

- granting an administrator role to solve an ordinary access problem;
- sending sensitive files through public links;
- disabling MFA instead of fixing enrolment;
- assuming every error is a local device problem;
- changing a tenant-wide setting for one user;
- copying audit records into public tickets;
- ignoring a service-status incident.

## Guided exercise

Using a synthetic SaaS environment or ticket pack:

1. diagnose an application-access issue;
2. review a risky external share;
3. support an MFA re-enrolment;
4. identify an unexpected administrator assignment;
5. prepare one change request and one SOC escalation;
6. document closure and user communication.

## Authoritative basis

- NIST Cybersecurity Framework 2.0 and NICE Framework concepts.
- CIS Controls v8.1 account, access and data-protection safeguards.
- Official service-provider identity, audit and sharing documentation.
