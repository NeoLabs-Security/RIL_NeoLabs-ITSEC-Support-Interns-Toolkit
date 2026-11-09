# Week 05 — Automatic NeoLabs SSH connection (IT Security & Support)

**Scenario:** `w05-poisoned-upload` · **Authoritative identity:** original central NeoLabs Lab Access Broker · **Applies to:** your mentor-assigned Support pod

## Student quick start

Use your current toolkit on your own computer or authorized workstation. After updating from the approved repository branch, run:

```bash
bash neolabs login --pod XX
bash neolabs connect
```

Replace `XX` with your assigned pod number (for example `02`). Enter your **existing NeoLabs Access Code**. Keep the `connect` terminal open.

In a second terminal **on the same machine**:

```bash
bash neolabs incident dashboard
```

The authorized Incident Desk opens at `http://127.0.0.1:18080/support` using the broker's one-time browser handoff. No separate cohort code or manual SSH configuration is needed.

## What `connect` automatically does

1. Creates/reuses a local private Ed25519 identity without sharing its private key.
2. Sends the matching public key securely to the authenticated central NeoLabs broker.
3. Waits for the server's restricted identity enrollment service and approved pod resource.
4. Pins the verified SSH host public key supplied by the broker and creates only the allowed local tunnel.

**Do not** run `bash neolabs incident keygen`, `bash neolabs week05 configure`, or `scp` public keys to the main host. Those are not intern onboarding requirements.

## Authorized Support workflow

- Investigate only the assigned pod and harmless synthetic uploads linked to a mentor-approved incident.
- Collect the source `event_id`, `upload_id`, detected/declared MIME and SHA-256 before change.
- Obtain authorization for the exact file, use the Incident Desk's quarantine action, and record the **new** containment event ID.
- Ask SOC to verify that containment event in central Wazuh as rule `100193`.
- Do not download raw files, run code, open a server shell, change other pods or bypass the broker.

If the broker reports `PENDING_SSH` or enrollment times out, contact the mentor; do not disable SSH host-key checks or bypass authentication. If you used an old manual standalone Week 05 preview profile, coordinate with the mentor before clearing it (`bash neolabs week05 clear`). The local tunnel uses port 18080 and must stay open during dashboard use.

For the required `ticket-resolution.md` and `evidence-register.md`, consult `assignments/week-05/support.md` and `SUBMISSION_HANDBOOK.md` in the NeoLabs Intern Assignments repository. The official mentor Issue supplies the deadline.
