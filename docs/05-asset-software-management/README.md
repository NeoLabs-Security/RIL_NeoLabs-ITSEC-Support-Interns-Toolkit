# Module 5 - Asset and Software Management

## Purpose

Security support begins with knowing what exists, who owns it, what it runs and whether it is still supported. This module teaches interns to maintain useful inventories without collecting unnecessary personal information.

## Learning outcomes

An intern should be able to:

- distinguish an asset register from a software inventory;
- record ownership, location, purpose, operating system and support status;
- identify unknown, duplicate, unmanaged or end-of-life assets;
- compare installed software with an approved list;
- document risk and escalation without uninstalling software without approval;
- support onboarding, change, incident and offboarding workflows.

## Asset record

A useful asset record includes:

- asset ID;
- device or service type;
- assigned owner or business role;
- operating system and version;
- hostname or approved label;
- location or environment;
- criticality;
- data classification;
- security tools present;
- patch-management method;
- backup status;
- lifecycle state;
- last verified date.

Do not record passwords, recovery codes, personal files or unnecessary user details.

## Software inventory

For each relevant application record:

- product and publisher;
- installed version;
- installation source;
- business purpose;
- licence or approval status;
- automatic-update state;
- end-of-support date where known;
- privileged components or services;
- owner;
- removal or exception decision.

An installed program is not automatically malicious. Verify purpose, provenance and approval before drawing a conclusion.

## Discovery workflow

1. Confirm the assigned asset and ticket.
2. Collect a read-only baseline using the approved script.
3. Compare the output with the authorised asset and software records.
4. Validate discrepancies with the owner or mentor.
5. Classify each discrepancy: stale record, legitimate change, unsupported software, unknown software or investigation required.
6. Raise a change request before removal, upgrade or reconfiguration.
7. Update the inventory after approved validation.

## Lifecycle states

Recommended states:

- requested;
- approved;
- staged;
- active;
- temporarily unavailable;
- repair;
- retired;
- disposed.

Retirement should include access revocation, data handling, licence recovery, evidence of approved disposal and inventory closure.

## Security uses

Inventories support:

- vulnerability and patch prioritisation;
- incident scoping;
- licence and support planning;
- detection of unmanaged systems;
- account and device offboarding;
- backup and recovery planning;
- change validation.

## Common mistakes

- treating an inventory scan as proof of ownership;
- deleting unknown software before confirming purpose;
- collecting excessive user data;
- using device names as the only identifier;
- failing to record cloud services and virtual assets;
- leaving retired devices marked active;
- recording an installed version but not its support status.

## Guided exercise

Using supplied synthetic baseline outputs:

1. create an asset register for five devices;
2. create a software inventory;
3. identify three discrepancies;
4. classify and prioritise them;
5. prepare one approved change request and one SOC escalation;
6. document the final inventory state.

## Authoritative basis

- CIS Controls v8.1: Enterprise Asset Inventory and Control of Enterprise Assets; Inventory and Control of Software Assets.
- NIST NICE Framework for task, knowledge and skill language.
- Vendor lifecycle and support documentation for specific products.
