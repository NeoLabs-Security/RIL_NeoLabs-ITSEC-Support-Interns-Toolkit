# Module 7 - Backup, Recovery and Service Continuity

## Core terms

- Recovery Point Objective (RPO): acceptable amount of data loss measured in time.
- Recovery Time Objective (RTO): target time to restore service.
- Backup: protected copy intended for recovery.
- Restore test: proof that the copy can be read and used.

## Workflow

1. Define the data, configuration and service dependencies.
2. Confirm destination, encryption, retention and access control.
3. Create a backup using an approved method.
4. Generate and retain an integrity checksum where appropriate.
5. Restore into a separate approved location.
6. Compare files, permissions, versions and application behaviour.
7. Record elapsed time, gaps and corrective actions.

A successful archive command is not proof of recoverability. The toolkit's synthetic rehearsal demonstrates backup, checksum verification and separate-directory restoration.

## Security considerations

Backups can contain credentials and personal data. Restrict access, protect keys separately, avoid public storage, and test deletion/retention requirements. Suspected ransomware or compromise must be escalated before reconnecting or overwriting evidence.

## Evidence

Record scope, date, tool/version, destination class, checksum, restore location, validation, RPO/RTO result and failures.

## Authoritative basis

CIS Control 11, NIST contingency-planning guidance and vendor recovery documentation.