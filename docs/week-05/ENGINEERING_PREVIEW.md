# Week 05 — IT Security & Support: Operation Poisoned Upload

**Scenario:** `w05-poisoned-upload` · **Access:** central NeoLabs Lab Access Broker · **Status:** operator-tested Week 05 release

The Week 05 app runs behind the loopback-only VCC gateway. Students must use an active broker-issued assignment and the official toolkit, not the standalone mentor rehearsal code. Central Wazuh remains the authoritative SOC alert source.

## Student connection — same Week 4 experience

From the **updated IT Security Support toolkit**, on the intern's own authorized workstation:

```bash
bash neolabs login --pod XX
bash neolabs connect
```

Replace `XX` with the mentor-assigned pod (for example `02`). Enter the **existing NeoLabs Access Code** when requested. Leave `connect` open, and in a second terminal on the same workstation run:

```bash
bash neolabs incident dashboard
```

The Support Incident Desk opens at `http://127.0.0.1:18080/support` using a central-broker one-time browser handoff. The intern does not need to run `keygen`, exchange keys with a mentor, enter a separate cohort code, configure SSH usernames, or manually pin a host fingerprint.

`connect` generates or reuses a private local Ed25519 key, submits **only** the public key to the authenticated broker, waits for the root-owned server enrollment timer to create a dedicated restricted SSH account, validates the trusted server host key returned by the broker, then opens the pod-scoped tunnel. All private key material stays on the intern's device.

If the status remains `PENDING_SSH` or the tunnel fails, contact the mentor. Do not bypass the broker, disable SSH host-key checking, reuse another intern's key or use the obsolete standalone cohort profile.

See [Week 05 automatic connection](../WEEK05_AUTO_CONNECT.md) for the complete client instructions.

## Incident workflow and evidence

Pentesting demonstrates the harmless intentionally accepted MIME/signature mismatch. SOC confirms the event in the central Wazuh index (rule `100191`) and hands off the exact `upload_id`, `event_id` and mentor-authorized incident reference.

In the Incident Desk, Support:

1. Confirms its assigned pod and the suspicious upload's filename, SHA-256, detected/declared MIME, upload ID and original event ID.
2. Records approval for the **exact** synthetic file and incident reference (`INC-W05-…`) before quarantine.
3. Performs the approved quarantine and records the **new** containment event ID and request ID.
4. Confirms the quarantined state and shares the containment event ID with SOC.
5. Obtains SOC confirmation of central Wazuh rule `100193`, documents the response timeline and submits a sanitized ticket.
6. Documents the mentor-approved fixed-release retest and expected legitimate PNG versus mismatched JPG results.

The Support Incident Desk allows neither raw uploaded content download nor filesystem browsing. A quarantined artifact cannot be restored by a student; do not attempt direct database or host modifications.

**Required submission:** `submissions/week-05/support/<github-username>/ticket-resolution.md` and `evidence-register.md` in the Intern Assignments repository, using the official templates and mentor Issue. Do not include access codes, session tokens, handoff URLs, private SSH keys or raw synthetic upload binaries.

## Operator information — do not circulate mentor preview codes

The existing Week 05 gateway remains loopback-only at `127.0.0.1:18600`. Operator-only standalone rehearsal routes and codes are **not intern onboarding**. The deployed central broker and root-owned `neolabs-w05-ssh-enrolment.timer` implement automatic enrollment across assigned pods.

The operator must confirm current scenario, intern-to-pod assignment, a valid code, active enrollment timer, SSH ingress for authorized intern IPs, correct remote forwarding restrictions and central Wazuh indexing. Do not expose the gateway publicly or restart W04 pods/volumes to address an intern connection issue.

The old `tools/week05_quarantine.py` direct-internal-token prototype and the obsolete `bash neolabs week05 configure` preview workflow are not the approved student path.
