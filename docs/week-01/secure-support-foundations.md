# Secure IT Support Foundations — Week 1

## Purpose
Secure support is not “try things until the error disappears.” It is a controlled process: establish scope, preserve evidence, isolate the layer causing the symptom, make the smallest authorised change, validate the result and escalate when security risk is involved.

## 1. The support loop
1. **Clarify the symptom** — what does the user see, when did it start, what should happen?
2. **Confirm scope** — assigned pod, authorised endpoint, synthetic account and ticket boundary.
3. **Collect evidence first** — screenshots, timestamps, error messages and read-only diagnostics.
4. **Localise the layer** — device/browser, DNS/network, identity/account, service/API or backend/data.
5. **Form a diagnosis** — explain why the evidence supports it.
6. **Act only with authority** — read-only by default; changes need task/ticket approval.
7. **Validate** — repeat the original workflow and confirm the result.
8. **Document and hand over** — another technician should be able to continue from your notes.

## 2. The NeoLabs access boundary
Before touching the VCC support surface run:

```bash
neolabs status
neolabs pod info
neolabs scope
neolabs targets
```

During the Week 1 live window `neolabs connect` opens an isolated SSH local-forward. The assigned application then appears at `http://127.0.0.1:18080`. That address is valid only while your tunnel is open and only represents your assigned pod.

Never reuse an old address, another student's tunnel or an endpoint not returned by the gateway.

## 3. Evidence before change
Capture enough information to answer:
- what failed;
- when it failed;
- which system/account/workflow was involved;
- what the user expected;
- what diagnostic check you performed;
- what the result was.

Do not include NeoLabs Access Codes, passwords, cookies, bearer tokens, private keys or personal data in tickets/screenshots.

## 4. A layered diagnostic model
### Layer A — Browser/device
Questions:
- Is only one browser affected?
- Does a private/incognito session behave differently?
- Is the device time correct?
- Is a local proxy/VPN interfering?

### Layer B — DNS/network
Questions:
- Does the name resolve?
- Is the expected TCP service reachable?
- Is the route stable?
- Is the issue local connectivity rather than the application?

Useful read-only tools include `ipconfig`/`ip`, `nslookup`/`dig`, `ping` where permitted, `tracert`/`traceroute`, `netstat`/`ss`, and the toolkit networking decision trees.

### Layer C — Identity/account
Questions:
- Is the account identifier correct?
- Is the error consistent with an invalid credential, lockout or permission problem?
- Does the user successfully authenticate but fail later in the workflow?

Never reset/change an account unless the ticket explicitly authorises it.

### Layer D — Application/API
Questions:
- Does the front page load?
- Does `/api/health` or the authorised application workflow respond?
- Does failure occur before or after authentication?
- Is the browser seeing a client error, authorization error or server error?

### Layer E — Backend/data
This layer is normally mentor/operator-owned in Week 1. A support intern should document evidence and escalate rather than modify databases or backend services.

## 5. Secure change discipline
A safe change has:
- an approved reason;
- expected effect;
- affected scope;
- pre-change evidence;
- rollback plan;
- post-change validation.

Week 1's assigned ticket is read-only. No account, permission, firewall, package, service or security-control change is pre-approved.

## 6. When Support becomes Security
Escalate to SOC/mentor when evidence suggests:
- unauthorized access;
- suspicious authentication patterns;
- malware or persistence;
- credential exposure;
- another pod/data boundary breach;
- tampering with logs/security controls;
- any action that could destroy evidence.

Support should preserve evidence, not “clean up” a suspected incident.

## 7. Writing a strong support ticket
Use these headings:
- **User request / symptom**
- **Scope**
- **Impact**
- **Evidence collected**
- **Diagnostic steps**
- **Diagnosis / current status**
- **Action or recommendation**
- **Validation**
- **Escalation / owner / next step**

Avoid vague notes such as “fixed it” or “network issue.” State exactly what was observed and how it was verified.

## 8. Knowledge-base writing
A useful KB article:
- solves one clearly stated problem;
- starts with safe checks;
- uses exact commands only where appropriate;
- explains expected results;
- includes stop/escalation conditions;
- never instructs users to disable antivirus/firewalls or share credentials just to make troubleshooting easier.

## 9. Week 1 Operation Night Watch checklist
- [ ] Correct pod and SUPPORT track confirmed.
- [ ] Isolated tunnel opened through `neolabs connect`.
- [ ] Normal front page, sign-in, authenticated content and logout checked.
- [ ] Evidence collected before any recommendation.
- [ ] Browser/device, network, identity and application hypotheses separated.
- [ ] Assigned synthetic ticket completed.
- [ ] Safe KB article completed.
- [ ] No unapproved change performed.
- [ ] Security concerns escalated instead of remediated blindly.
