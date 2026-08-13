# Support Ticket 01 — Learner Access Baseline

**Classification:** Synthetic training ticket  
**Scenario:** Operation Night Watch  
**Priority:** P3 / normal support  
**Change authority:** Read-only diagnosis. No account, permission, firewall, service or security-control change is pre-approved.

## User report

> I can reach the learner application, but I am not sure everything is working correctly. Please verify that my normal learner access is healthy before I begin the internship lab tasks. I also want to know what I should capture if I later have trouble signing in or opening course content.

## Synthetic user context

Use only the learner account/workflow provided by the programme for your assigned pod. Do **not** put the password, NeoLabs Access Code, browser cookie or bearer token into the ticket.

## Required checks

1. Confirm the server-issued Support endpoint matches your assigned pod.
2. Confirm the learner front page loads.
3. Confirm the supplied synthetic account can sign in normally.
4. Confirm the authenticated profile/session is usable.
5. Confirm course/section content is reachable.
6. Confirm a normal logout completes.
7. Record the evidence you would collect for these future symptoms without making a change:
   - DNS/name-resolution failure;
   - TCP/service unreachable;
   - invalid/locked account symptom;
   - application/API error after sign-in;
   - browser-only issue while the API/service remains healthy.
8. Decide which of those symptoms Support can continue diagnosing and which should be escalated if security compromise is suspected.

## Required output

Complete the toolkit Support Ticket template with:

- user-visible symptom / request;
- scope and assigned pod;
- evidence collected;
- normal-service check results;
- diagnosis/status;
- action or recommendation;
- validation method;
- escalation status.

Then write a short KB article titled:

**“How to Collect Safe First-Line Evidence for a NeoLabs Learner Access Problem”**

The article must tell a learner what to check without asking them to disable security controls or share credentials.

## Success condition

A second Support intern or mentor should be able to repeat your normal-service checks from your notes without receiving any secret values.
