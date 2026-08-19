# NeoLabs Synthetic Support Ticket Library

> **Practice library only.** These are reusable teaching examples, not the live Week 2 Ghost Login queue. During Week 2, retrieve your server-issued pod queue with `.\neolabs.cmd tickets` and use only the cases returned for your assigned pod.

All names, devices, addresses and data in these tickets are fictional. Students should use the secure support lifecycle, collect evidence, decide whether a change is authorized and identify when SOC escalation is required.

## Ticket 01 — Internal site does not open

- Reporter: Ada Nwosu
- Device: `NL-LAB-WIN-01`
- Symptom: Browser reports that the approved training site cannot be reached.
- Scope clue: Other students can access the site.
- Recent change: Device moved from Wi-Fi to a USB Ethernet adapter.
- Required output: Diagnostic journal, first failing network layer, proposed remediation and validation plan.
- Do not: Disable the firewall or replace DNS settings without approval.

## Ticket 02 — Repeated MFA prompts

- Reporter: Musa Bello
- Device: `NL-LAB-WIN-02`
- Symptom: Three MFA prompts appeared while the user was not signing in.
- Scope clue: The account still works.
- Recent change: None known.
- Required output: Identity verification, evidence-preserving intake and SOC escalation record.
- Do not: Approve a prompt, delete sign-in notifications or reset evidence before escalation.

## Ticket 03 — Linux web service failed after update

- Reporter: Training application owner
- Device: `NL-LAB-LNX-01`
- Symptom: A synthetic web service is inactive after an approved package update.
- Scope clue: The host is reachable and other services are healthy.
- Recent change: Maintenance window completed 20 minutes earlier.
- Required output: Service dependency review, relevant journal evidence, rollback decision and validation plan.
- Do not: Reinstall the operating system or remove packages without approval.

## Ticket 04 — Unknown local administrator

- Reporter: Endpoint review process
- Device: `NL-LAB-WIN-03`
- Symptom: Baseline collection shows a local administrator account not present in the asset record.
- Scope clue: The account was created two days earlier.
- Recent change: No approved account change found.
- Required output: Evidence record and immediate SOC escalation.
- Do not: Delete the account, change its password or sign in as the account before instruction.

## Ticket 05 — Backup exists but restore is untested

- Reporter: Support team lead
- System: Synthetic shared folder
- Symptom: Daily archive files exist, but no restore evidence is available.
- Scope clue: The data is synthetic and a maintenance window is approved.
- Required output: Recovery plan, checksum validation, separate-directory restore test and recovery report.
- Do not: Restore over the active source directory.

## Ticket 06 — User requests permanent admin rights

- Reporter: Chidi Okafor
- Device: `NL-LAB-WIN-04`
- Symptom: A required training application asks for elevation during installation.
- Scope clue: The user requests permanent local administrator membership for convenience.
- Required output: Business-need verification, least-privilege options, approval path and account-access review.
- Do not: Grant permanent admin rights without approved justification.

## Assessment questions for every ticket

1. What is confirmed, and what is only reported?
2. What read-only evidence should be collected first?
3. Does the ticket require a change, escalation or both?
4. What approval is required?
5. What could destroy evidence or weaken security?
6. How will resolution be validated?
