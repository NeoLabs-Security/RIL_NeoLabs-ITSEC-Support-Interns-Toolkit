# Week 05 Pod01 — automatic SSH connection (standalone cohort)

**Scope**: current Nov 9–16 temporary **Week05-only** `w05-poisoned-upload` cohort. **Not** the Week04 Lab Access broker. The operator controls a separate W05 Pod01 SUPPORT code and a *per-student* SSH transport identity. Central Wazuh remains separate.

**Student CLI** on Linux/Ubuntu, inside this W05 feature-branch toolkit:

## One-time mentor-approved enrollment
1. Run `bash neolabs week05 keygen`. This creates a local private W05 Ed25519 SSH key (0600) and prints the corresponding **public key**. Never email the private key.
2. Send **only the printed public key** privately to your NeoLabs mentor along with your track and identity.
3. Mentor checks identity, registers the public key against an isolated restricted `nlw05sup_<12hex>` SSH user on the main VCC server using the existing authorized provisioning script, and returns the exact SSH username, server hostname/public IP, and **verified server ED25519 SSH host fingerprint** by trusted private channel.
4. Using those verified values, run:
   ```bash
   bash neolabs week05 configure \
      --host ACTUAL_VCC_PUBLIC_IP_OR_HOST \
      --username ACTUAL_RESTRICTED_USERNAME \
      --fingerprint SHA256:ACTUAL_VERIFIED_ED25519_HOST_FINGERPRINT
   ```
   The toolkit checks the live server Ed25519 key against this previously verified fingerprint and pins it in a private known-hosts file. It does **not** accept a new or changed host key silently. If the SSH host key changes, report it to the mentor before any reconfiguration.

## Every training session
1. `bash neolabs connect` — automatically opens only the localhost SSH forward `127.0.0.1:18080 -> VCC localhost:18600` with your approved private key. Keep this terminal open.
2. In a second terminal on the **same machine**:
   ```bash
   bash neolabs incident dashboard
   ```
   It opens `http://127.0.0.1:18080/support` in your browser; enter the separate, privately distributed **Week05 SUPPORT cohort code** there. The W05 cohort code is NOT an SSH password and should never be supplied to `bash neolabs login` (which still queries Week04).
3. Keep work within the assigned Pod01 scenario. Upload or quarantine only benign files and mentor-approved incident references.

## Restore Week04 behavior
`bash neolabs week05 clear` disables the special Week05 local profile so `bash neolabs connect` again follows the normal authoritative Week04 broker. It does not delete private keys and it does not revoke any server account. Request revocation from the mentor after the exercise.

## Operator prerequisites
- The main VCC gateway is already running in `W05_AUTH_MODE=cohort` on `127.0.0.1:18600` (loopback only), and its PENTEST, SOC and SUPPORT private codes are distinct and expire **2026-11-16 06:00 UTC = 07:00 WAT**. Never publish 18600 to the Internet.
- Each student must have a **distinct restricted SSH server identity** and have their own public key enrolled in an approved `authorized_keys` by the mentor. Re-running the server's one-key enrolment helper for an existing username overwrites that account's key—always use a separate username for each student.
- Server-side authorized-key restrictions and sshd Match rules must restrict forwarding to `127.0.0.1:18600`, with no shell, PTY or agent forwarding. Use only trusted key fingerprint. Do not reuse the EC2 admin SSH private key.
- The toolkit cannot automatically grant SSH privileges based on a **shared application code**: that would remove the per-student enrollment and revoke controls. After the one-time enrollment, tunnel creation is automatic.
- Browser must run on the computer where port 18080 is forwarded. When using a headless student EC2 instance, a further approved local forward to a desktop browser is needed.
- If `bash neolabs connect` reports an expired profile or mismatched host fingerprint, stop and contact the mentor.
