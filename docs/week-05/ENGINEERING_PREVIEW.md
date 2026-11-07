# Week 05 — IT Security & Support standalone test guide (draft)

**Authorized target:** mentor's separate Week 05 test server through localhost-only gateway (TCP 18600). Use only the mentor-issued W05 Support Access Code for your assigned pod.

The preferred client obtains a short-lived server-verified session and does not ask you to pick a pod locally:

```bash
python3 tools/week05_client.py login
python3 tools/week05_client.py status
python3 tools/week05_client.py target
python3 tools/week05_client.py uploads
```

When a synthetic incident is assigned, pick an exact `upload_id` from **your own pod's** inventory:

```bash
python3 tools/week05_client.py quarantine --upload-id '<upload-id>' \
  --incident INC-W05-001 --confirm
python3 tools/week05_client.py uploads
python3 tools/week05_client.py logout
```

The quarantine command moves a harmless fixture into restricted persistent storage and logs an event. Do not SSH into the container, modify DB tables, use arbitrary filesystem paths or quarantine another pod's item.

The earlier prototype `tools/week05_quarantine.py` accepts mentor internal tokens and is **superseded** for the stand-alone test. Interns must use the broker-scoped client `tools/week05_client.py` instead.

The existing Support `neolabs.cmd` and `neolabs.ps1` routines remain unchanged for Week 4. Official W05 root-CLI publishing, ticket authority and sign-off are not completed by the standalone test.
