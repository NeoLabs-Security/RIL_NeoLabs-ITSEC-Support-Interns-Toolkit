# Week 05 — Poisoned Upload (IT Security & Support preview)

**Draft, mentor-only.** Normal student deployment must replace the manually prompted training token with the current server-authorized NeoLabs Support scope and published tunnel.

The new `tools/week05_quarantine.py` supports metadata-only inventory and explicitly confirmed quarantine of one server-issued upload ID. It checks the exact Week 05 scenario and pod before any state change; all URLs are localhost-only, and the token is never printed.

Mentor-only inventory (requires Support token):

```bash
python3 tools/week05_quarantine.py --url http://127.0.0.1:18080 --expected-pod pod-01
```

One **approved** quarantine, only after a ticket + SOC incident identifier has been published:

```bash
python3 tools/week05_quarantine.py --url http://127.0.0.1:18080 \
 --expected-pod pod-01 --incident INC-W05-001 \
 --upload-id '<server-issued-id>' --confirm
```

The operation moves an inert fixture into protected, non-public storage and creates a W05 synthetic event. There is no host shell, generic filesystem access, force delete, or permission change.

Pending before student publication: broker-authorized Support scope, authorized resource publication, incident/ticket ID validation on the server, audit correlation in Wazuh, recovery and fixed-retest tests, root NeoLabs CLI integration.
