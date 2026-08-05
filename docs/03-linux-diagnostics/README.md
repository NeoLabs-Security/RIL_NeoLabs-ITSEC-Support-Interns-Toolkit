# Module 3 — Linux Security Diagnostics

## Purpose

This module teaches a structured way to inspect Linux endpoints and servers while preserving evidence and avoiding unsafe configuration changes.

## Learning outcomes

An intern should be able to:

- identify the host, distribution, kernel, time and current user context;
- inspect services, processes, storage and package state;
- use `journalctl` and common log locations effectively;
- review users, groups, permissions, `sudo`, SSH and firewall state;
- distinguish availability problems from configuration and security problems;
- prepare an approved remediation and rollback plan;
- recognise activity that should be escalated to the SOC.

## Diagnostic order

### 1. Establish system identity and time

```bash
hostnamectl
uname -a
cat /etc/os-release
date --iso-8601=seconds
id
```

Time accuracy matters because support evidence may need to be correlated with application, network and SOC telemetry.

### 2. Check resources and filesystem state

```bash
uptime
free -h
df -hT
lsblk -f
ps -eo pid,user,comm,%cpu,%mem --sort=-%cpu | head -n 20
```

Low disk space, memory pressure and high load may be symptoms rather than root causes. Record the processes and time before restarting anything.

### 3. Review service status

```bash
systemctl --failed
systemctl status <approved-service> --no-pager
systemctl list-dependencies <approved-service>
```

Do not restart a service until its current state, dependencies, recent logs and business impact have been recorded.

### 4. Review logs

```bash
journalctl --since '-2 hours' -p warning..alert --no-pager
journalctl -u <approved-service> --since '-2 hours' --no-pager
last -a | head
```

Common locations may include:

- `/var/log/auth.log` or the distribution's authentication journal;
- `/var/log/syslog` or system journal;
- application-specific logs;
- package-manager history;
- web server access and error logs.

Never clear or truncate logs to resolve a support problem.

### 5. Review accounts and privilege

```bash
getent passwd
getent group sudo 2>/dev/null || true
sudo -l
find /etc/sudoers.d -maxdepth 1 -type f -ls 2>/dev/null
```

Record unexpected users, group membership or `sudo` rules and escalate before removing them when compromise is possible.

### 6. Review network state

```bash
ip address
ip route
ss -lntup
resolvectl status 2>/dev/null || cat /etc/resolv.conf
```

A listening port should be compared with the approved service inventory. Do not assume every unfamiliar port is malicious or every expected port is safe.

### 7. Review firewall and SSH configuration

```bash
ufw status verbose 2>/dev/null || true
nft list ruleset 2>/dev/null || true
sshd -T 2>/dev/null | head -n 80
```

Configuration output should be interpreted against the organisation's baseline. Avoid direct edits to SSH or firewall rules without console access, approval and rollback planning.

### 8. Review patch state

For Ubuntu systems:

```bash
apt list --upgradable 2>/dev/null
pro security-status 2>/dev/null || true
grep -h '' /var/log/apt/history.log 2>/dev/null | tail -n 80
```

Patch decisions require testing, maintenance planning, dependency awareness and recovery preparation.

## Common security mistakes

- using `chmod 777` as a generic fix;
- granting broad `sudo` access instead of correcting ownership or role design;
- disabling AppArmor, firewall or SSH controls to test connectivity;
- restarting services before collecting logs;
- applying a hardening profile without compatibility testing;
- deleting suspicious files before escalation and evidence capture.

## Escalate to the SOC when

- unknown privileged users or keys appear;
- authentication logs show suspicious access;
- security controls were unexpectedly disabled;
- an unapproved listening service or remote-access tool appears;
- scheduled tasks or startup entries are suspicious;
- system binaries, logs or package records appear altered;
- another pod's data is visible.

## Baseline principle

Canonical's Ubuntu security guidance treats hardening as a layered and environment-specific activity. Tools such as Ubuntu Security Guide can audit or apply recognised profiles, but changes must be tested and approved rather than applied blindly.

## Authoritative basis

- Ubuntu security documentation and Ubuntu Security Guide.
- CIS Controls v8.1.
- NIST SP 800-61 Rev. 3.
- NeoLabs `SUPPORT_BOUNDARIES.md`.
