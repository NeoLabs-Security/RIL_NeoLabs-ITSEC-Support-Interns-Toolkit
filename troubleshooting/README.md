# IT Security Support Toolkit Troubleshooting

Use the smallest safe diagnostic step first. Do not solve a support problem by disabling security controls, clearing logs or making unapproved changes.

## 1. GitHub and repository access

### Repository invitation or clone problem

- Confirm you are signed into the GitHub account registered for the programme.
- Accept the organisation or repository invitation.
- Confirm the repository name and URL.
- Use the track GitHub fundamentals guide.

### Push rejected

- Work on a submission branch, not `main`.
- Run `git status` and confirm your files.
- Pull only the branch instructed by the mentor.
- Never force-push a shared branch.
- Submit through a Pull Request linked to the assigned Issue.

## 2. Windows collector problems

### PowerShell script will not run

- Confirm the script came from this repository.
- Use the programme-approved execution instructions.
- Do not weaken system-wide execution policy to run one script.
- Record the exact error and PowerShell version.
- Confirm the output directory is writable.

### Some sections show access denied

The collector is read-only and may have limited visibility without elevated rights. Do not automatically rerun as administrator. Record the visibility gap and request approval if privileged collection is required.

### Defender, BitLocker or Firewall command unavailable

Record the operating-system edition and feature status. Do not install or disable components without an approved change.

## 3. Linux collector problems

### Command missing

Record the distribution and version. The script should continue where possible. Do not install packages without approval simply to complete a report.

### Permission denied

Do not add `sudo` automatically. Identify the specific field that requires privilege and request approval. Mark unavailable evidence clearly.

### Journal output is empty

Check the requested time window and whether the service uses another approved log source. Do not change log retention or clear state.

## 4. Network diagnosis

Use this order:

1. physical or virtual link;
2. address and interface state;
3. local route;
4. DNS resolution;
5. destination reachability where authorised;
6. port and service state;
7. firewall or proxy evidence;
8. TLS and certificate state;
9. application response.

Do not disable the firewall. Compare rules and logs, then raise an approved change if required.

## 5. Identity and access problems

- Verify the requester before reset or MFA action.
- Confirm the correct synthetic identity and assigned role.
- Check account state, group membership, licence or application assignment.
- Do not grant administrator access as a troubleshooting shortcut.
- Repeated MFA prompts, unexpected privilege or unverified recovery requests require SOC escalation.

## 6. Backup and restore problems

### Checksum mismatch

Stop. Do not restore the archive. Verify the selected backup, transfer path and recorded checksum, then escalate.

### Restore is incomplete

Keep the original backup and restored copy unchanged. Compare manifests, record missing files and do not replace active data.

### Script refuses the path

The recovery script is intentionally path-confined. Use only the supplied temporary lab workspace; do not alter the guard to target another directory.

## 7. Patch or change problems

- Confirm the approved asset and window.
- Check dependencies and backup.
- Preserve the original error.
- Stop if service health or security controls degrade.
- Follow the documented rollback trigger.
- Record failure honestly; do not hide or improvise an unapproved workaround.

## 8. Possible incident

Stop routine troubleshooting and escalate when you see suspicious privilege, malware indicators, unusual authentication, unexplained encryption or deletion, security-control tampering, data-access concerns or missing logs.

Do not:

- delete suspicious files;
- clear logs;
- reimage or power off without direction;
- reset broad groups of accounts;
- upload evidence to public GitHub or general Slack.

## Support request package

Provide:

- intern ID and assignment ID;
- asset or synthetic identity label;
- operating system and version;
- exact non-secret error;
- step that failed;
- expected result;
- evidence ID and restricted location;
- changes already made;
- whether rollback or SOC escalation is needed.
