#!/usr/bin/env bash
set -euo pipefail

# Read-only Linux baseline collection for authorised NeoLabs training systems.
# The output can contain host and account information. Store it only in the
# approved evidence location and never commit generated reports to GitHub.

OUTPUT_DIR="${1:-./evidence/local-baseline}"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
REPORT="$OUTPUT_DIR/linux-baseline-$STAMP.txt"

mkdir -p "$OUTPUT_DIR"
chmod 700 "$OUTPUT_DIR" 2>/dev/null || true
umask 077

section() {
  printf '\n===== %s =====\n' "$1" >> "$REPORT"
}

run_readonly() {
  local title="$1"
  shift
  section "$title"
  if command -v "$1" >/dev/null 2>&1; then
    "$@" >> "$REPORT" 2>&1 || printf 'Command returned a non-zero status.\n' >> "$REPORT"
  else
    printf 'Command not available: %s\n' "$1" >> "$REPORT"
  fi
}

{
  echo "NeoLabs IT Security Support — Linux Read-Only Baseline"
  echo "Collected UTC: $(date -u +%FT%TZ)"
  echo "Purpose: authorised diagnosis and baseline comparison"
  echo "Warning: may contain host and account metadata; do not commit this report"
} > "$REPORT"

run_readonly "Kernel and architecture" uname -a
run_readonly "Operating system release" cat /etc/os-release
run_readonly "Hostname information" hostnamectl
run_readonly "Uptime and load" uptime
run_readonly "Memory" free -h
run_readonly "Mounted storage" df -hT
run_readonly "Block devices" lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
run_readonly "Network addresses" ip -brief address
run_readonly "Routes" ip route
run_readonly "Listening sockets" ss -lntup
run_readonly "Failed systemd units" systemctl --failed --no-pager
run_readonly "Enabled services" systemctl list-unit-files --state=enabled --no-pager
run_readonly "Recent boot warnings" journalctl -b -p warning --no-pager -n 200
run_readonly "User accounts" getent passwd
run_readonly "Group accounts" getent group
run_readonly "Sudo configuration validation" sudo -n visudo -c

section "Firewall status"
if command -v ufw >/dev/null 2>&1; then
  ufw status verbose >> "$REPORT" 2>&1 || true
elif command -v firewall-cmd >/dev/null 2>&1; then
  firewall-cmd --state >> "$REPORT" 2>&1 || true
  firewall-cmd --list-all >> "$REPORT" 2>&1 || true
else
  printf 'No supported host-firewall status tool found.\n' >> "$REPORT"
fi

section "Package update summary"
if command -v apt >/dev/null 2>&1; then
  apt list --upgradable 2>/dev/null >> "$REPORT" || true
elif command -v dnf >/dev/null 2>&1; then
  dnf check-update >> "$REPORT" 2>&1 || true
elif command -v yum >/dev/null 2>&1; then
  yum check-update >> "$REPORT" 2>&1 || true
else
  printf 'No supported package manager found.\n' >> "$REPORT"
fi

sha256sum "$REPORT" > "$REPORT.sha256"
chmod 600 "$REPORT" "$REPORT.sha256" 2>/dev/null || true

echo "Read-only baseline saved to: $REPORT"
echo "Review and redact it before sharing through an approved channel."
