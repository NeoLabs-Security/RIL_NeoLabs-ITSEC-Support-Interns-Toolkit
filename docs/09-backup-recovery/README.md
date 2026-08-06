# Module 9 - Backup, Recovery and Service Continuity

## Purpose

A backup is useful only when it is protected, complete and restorable. This module teaches interns to document backup requirements, verify integrity and rehearse recovery without overwriting the original evidence or production-like data.

## Learning outcomes

An intern should be able to:

- distinguish backup, replication, snapshot and archive;
- explain recovery point objective and recovery time objective;
- identify protected data, configuration and dependency requirements;
- verify checksums and backup metadata;
- restore to a separate approved location;
- validate recovered files and services;
- document failures, limitations and escalation.

## Backup planning

For each protected system record:

- system or asset owner;
- data and configuration included;
- exclusions;
- backup type and frequency;
- retention period;
- encryption and access controls;
- storage location;
- recovery point objective (RPO);
- recovery time objective (RTO);
- restoration dependencies;
- responsible operator;
- last successful restore test.

## Backup types

- **Full backup:** complete selected dataset.
- **Incremental backup:** changes since the last backup of any type.
- **Differential backup:** changes since the last full backup.
- **Snapshot:** point-in-time state of a supported volume, filesystem or service.
- **Archive:** long-term retained records, not necessarily a rapid operational restore.
- **Replication:** a copy kept in sync; corruption or deletion may replicate, so it is not a complete replacement for backup.

## Safe restore workflow

1. Confirm the ticket and approved recovery objective.
2. Preserve the original system and evidence.
3. Select the correct backup by timestamp and scope.
4. Verify archive metadata and checksum.
5. Restore to a separate temporary location or approved isolated target.
6. Compare file counts, names, sizes and checksums.
7. Validate required configuration and service behaviour.
8. Record missing, stale or corrupt content.
9. Obtain approval before replacing active data.
10. Clean up temporary recovery material according to policy.

## Integrity verification

A successful copy command does not prove recovery. Validate:

- archive can be opened;
- checksum matches the recorded value;
- expected files are present;
- recovered file checksums match source records where available;
- permissions and ownership are appropriate;
- application or service validation passes;
- logging and security controls remain enabled.

## Ransomware-readiness scenario

For the VCC scenario in which a developer workstation contains encrypted pre-commit files, IT Security Support students should:

- preserve the affected synthetic workstation state;
- identify the last known-good protected copy;
- verify backup integrity;
- restore to an isolated location;
- coordinate with SOC before deleting suspicious files;
- validate that recovered source and configuration are complete;
- record recovery time, gaps and lessons learned.

No real malware is included in the toolkit. The exercise uses inert synthetic files and scenario-generated evidence.

## Common mistakes

- restoring directly over the only copy;
- assuming replication protects against deletion;
- failing to back up configuration and keys needed for recovery;
- keeping backups with the same credentials and exposure as the source;
- reporting success without testing restored content;
- deleting suspicious artefacts before SOC review;
- ignoring retention and privacy requirements.

## Practical lab

Run the guarded synthetic rehearsal script. Review its source and confirm that it:

- confines work to the supplied temporary directory;
- creates synthetic files;
- generates an archive and checksum;
- restores to a separate directory;
- compares source and restored manifests;
- produces a result record;
- does not modify external system paths.

## Authoritative basis

- CIS Controls v8.1 Data Recovery.
- NIST incident response and recovery considerations.
- Official platform backup and restore documentation for the approved environment.
