# Lab — Backup Integrity and Restore Rehearsal

## Purpose

A backup is useful only when it can be located, verified and restored. This lab uses a disposable directory and synthetic files to practise:

- identifying what must be protected;
- creating a timestamped archive;
- generating and verifying a SHA-256 checksum;
- simulating loss in a controlled workspace;
- restoring to a separate validation directory;
- comparing restored data with the original manifest;
- documenting recovery time, errors and residual risk.

## Safety boundary

The included script operates only inside a learner-selected directory whose name ends with `neolabs-recovery-lab`. It refuses `/`, home directories and paths outside this naming rule. It never uses administrator privileges and does not modify system backup settings.

## Run

```bash
mkdir -p "$HOME/neolabs-recovery-lab"
bash scripts/backup-restore-rehearsal.sh "$HOME/neolabs-recovery-lab"
```

The script creates:

```text
neolabs-recovery-lab/
├── source/
├── backup/
├── restored/
└── evidence/
```

## Required report

Record:

- recovery objective;
- files included and excluded;
- archive name and checksum;
- start and completion times;
- checksum verification result;
- restored-file comparison result;
- recovery problems;
- changes needed before a real recovery process could be approved.

## Learning questions

1. Why should restoration occur into a separate directory first?
2. What does a matching archive checksum prove, and what does it not prove?
3. Why should recovery instructions be tested before an incident?
4. How would encryption, access control and retention apply to real recovery data?

## Authoritative basis

- CIS Control 11: Data Recovery, Controls v8.1.
- NIST SP 800-61 Rev. 3.
- CISA recovery and patch-management guidance.
