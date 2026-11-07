# Week 05 — IT Security & Support: Operation Poisoned Upload

**Status:** mentor-only test integration, not an announcement of cohort publication. Five standalone W05 upload pods, the central SOC broker, and the central Wazuh dashboard are separate authorized components. Do not share local mentor preview codes with students.

## Your assignment

Support receives a synthetic suspicious-upload incident from SOC, reviews pod-scoped upload metadata and original security event IDs, confirms containment authorization, quarantines the exact artifact, and submits a sanitized incident/ticket record. Coordinate your incident reference and confirmation with the SOC intern or mentor.

The Week 05 Incident Desk shows:
- Assigned pod's upload inventory, upload IDs, SHA-256, filename, declared MIME, detected MIME, size and active/quarantined status.
- Matching **local** audit events with exact `event_id`, `request_id`, UTC time and reason code (including `extension_only_validation`).
- A guarded quarantine form requiring `INC-W05-…`, an approval checkbox and an explicit confirmation.
- A local Markdown ticket export that records the observed artifact state and containment event ID without leaking credentials.

The upload content is **never downloaded**. Neither raw content nor arbitrary filesystem path browsing is included. The local audit endpoint is not a replacement for SOC's independently verified Wazuh alert.

## Mentor-only browser rehearsal: existing localhost SSH tunnel

With the mentor's **already approved** local SSH forward on the same browser machine:

```bash
# From the root of this Support toolkit:
bash neolabs incident dashboard --mentor-preview

# Or, when no graphical browser is available:
bash neolabs incident dashboard --mentor-preview --no-open
```

Open `http://127.0.0.1:18600/support` in the **browser on the same machine that owns the SSH tunnel**. Do not open or expose port 18600 publicly.

In a PRIVATE operator terminal on the separate W05 VCC host, the mentor may reveal only that assigned pod's Support preview code:

```bash
cd ~/VCC-Security-Lab
python3 scripts/w05-lab.py code --pod pod-01 --track support --reveal
```

Do not paste the code into issues, submissions or shared screenshots. In the browser, login only with the authorized Support code for that pod.

Suggested rehearsal: the Pentest side first uploads the **approved harmless mislabeled JPG** in the intentionally vulnerable W05 release; SOC verifies the suspicious accepted-upload event `100191` and sends its `upload_id`, event ID and mentor-authorized incident reference to Support. Support reviews the same upload, checks MIME mismatch and hash, obtains approval, quarantines, and observes a new `file.upload_quarantined` event. The SOC side verifies corresponding rule `100193` on the **central** Wazuh dashboard. Support exports the ticket and records who approved the action, UTC timeline, and post-containment verification. Repeat with an accepted normal PNG and a rejected TXT as negative controls; do **not** quarantine a normal upload without a specific approved incident.

A quarantined upload cannot be reactivated by this student workflow. Repeated quarantine returns an already-quarantined status, not a new containment event; the UI blocks repeating a confirmed action.

## Support SSH key enrollment (operator-controlled, before student release)

The Week 05 Support student uses a **distinct** SSH key, not the old Week 04 password/SSH identity. The student can create it on the **machine that will own the localhost SSH tunnel**:

```bash
bash neolabs incident keygen
```

This generates `~/.neolabs/support/w05-tunnel-ed25519` (private, permission 0600) and displays only its `.pub` contents. Students transmit the **public** key privately to the mentor; nobody should send private keys or Access Codes in Slack/GitHub.

The mentor must verify the exact student-to-pod-to-track broker assignment, choose the approved `nlw05sup_<12hex>` SSH username, place the public key into a restricted local file on the **separate W05 server**, and run:

```bash
sudo bash scripts/w05-configure-restricted-support-ssh.sh \
  pod-01 nlw05sup_012345abcdef /absolute/path/to/approved-support-key.pub
```

The example username is illustrative. Substitute the **actual published identity**, not an arbitrary guessed value. The script first verifies that the running localhost gateway is specifically W05, then installs a no-shell, publickey-only SSH identity permitted to forward solely to `127.0.0.1:18600`. Restrict EC2 SSH ingress to approved student source IPs. Confirm SSH host fingerprints out-of-band before students connect.

This operation only creates a restricted SSH transport identity; it does **not** publish a W05 broker manifest, change the active W04 release, issue Access Codes, or authorize students on its own. Never perform it on the existing W04 server.

## Student path (only AFTER central broker publishes Week 05)

```bash
bash neolabs login
bash neolabs connect           # maintain in a dedicated terminal
bash neolabs incident dashboard
```

The Support CLI validates `track=SUPPORT`, `scenario_id=w05-poisoned-upload`, `student_ready=true`, `lab_state=STUDENT_READY`, an assigned pod, and explicit `support_ticket_queue.v1` + `week05_support` resources. Only a published restricted SSH key, assigned tunnel to local 18080 -> remote 18600 and broker-authorized one-use handoff can open official student mode. A Week 4 ticket or password credential **does not authorize Week 5**. Staff must register the separate approved W05 Support SSH key in advance; the CLI refuses to fall back to W04 password SSH.

The official path is **not ready** until the operator publishes the W05 broker manifest, establishes the restricted student SSH account/key, and validates the authorized handoff. The temporary preview is a mentor-only alternative, not a student login.

## Evidence checklist

For each incident record include: scenario and pod; the source upload ID; original accepted event ID and `metadata.reason_code`; declared/detected MIME and SHA-256; approved incident reference; decision justification and escalation; containment UTC and exact quarantine event ID; SOC confirmation of **indexed** 100193; normal-use retest; and limitations.

The export from the Incident Desk is an initial ticket record, not the entirety of the final report. Complete any additional assignment-repository fields and use the official Week 5 submission instructions when published. Never include internal access codes, bearer sessions, SSH private keys or SOC broker exporter credentials.

## Existing Week 4 compatibility

Existing `bash neolabs tickets` and `bash neolabs entitlements` remain unchanged for Week 4. The old `tools/week05_quarantine.py` direct-internal-token prototype is **not** the recommended intern workflow. Never run `docker compose down -v` or `--remove-orphans` when updating the new Week 5 gateway: exporter and upload containers share its Compose project.
