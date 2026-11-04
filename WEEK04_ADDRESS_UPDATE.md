# Week 4 VCC address update — 4 November 2026

The current authorised VCC gateway is https://16.192.188.181:18443.
The VCC SSH tunnel host, when published by the broker, must also use 16.192.188.181.
Pod assignments and access codes are unchanged.

After pulling this update:

```bash
unset NEOLABS_LAB_BASE_URL
bash neolabs login --base-url https://16.192.188.181:18443
bash neolabs status
bash neolabs connect
```

Use your assigned pod and private track access code. Existing direct sessions
using either former gateway migrate on their next manifest refresh. Explicit
environment overrides and discovery records remain authoritative: update any
old NEOLABS_LAB_BASE_URL in your shell configuration. If discovery is configured,
the operator must update its published gateway_url too.

The server operator must reissue the ingress leaf certificate with
IP:16.192.188.181 in its Subject Alternative Name, signed by the existing CA,
and reload ingress. Keep the bundled CA and existing client certificates.
The operator must also update server-published resource, telemetry and tunnel
URLs. This toolkit update cannot change the running VCC server.
Do not bypass certificate validation.
