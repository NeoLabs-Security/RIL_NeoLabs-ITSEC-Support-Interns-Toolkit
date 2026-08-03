# Module 4 — Networking Troubleshooting Decision Trees

## Principle

Troubleshoot from the local device outward and identify the first failing layer. Do not disable firewalls, reset the entire network stack or change DNS before collecting the current state.

## Decision tree A — No network access

1. **Is the network adapter present and enabled?**
   - Windows: `Get-NetAdapter`
   - Linux: `ip link`
2. **Does the adapter have a valid address?**
   - Windows: `Get-NetIPConfiguration`
   - Linux: `ip address`
3. **Is there a default route?**
   - Windows: `Get-NetRoute -DestinationPrefix '0.0.0.0/0'`
   - Linux: `ip route`
4. **Can the device reach its local gateway?**
5. **Can it resolve the approved hostname?**
6. **Can it reach the approved service port?**
7. **Does the application still fail after transport succeeds?**

Record the first failed test. Do not treat a successful ping as proof that an application is healthy.

## Decision tree B — Name resolution failure

1. Confirm the exact hostname and spelling.
2. Check configured DNS servers.
3. Test resolution with an approved tool.
4. Compare the result with another authorised device on the same network.
5. Determine whether the failure affects one hostname or all names.
6. Check DNS-client events, resolver status and recent network changes.
7. Escalate rather than overriding DNS with an unapproved public resolver.

## Decision tree C — Port or service unreachable

1. Confirm DNS resolves to the expected lab address.
2. Confirm a route exists.
3. Test the exact approved port.
4. Determine whether the result is timeout, refusal or reset.
5. Check whether the service is listening on the destination.
6. Review host and network firewall evidence.
7. Review service logs and dependency health.
8. Change a firewall rule only through an approved change with rollback.

## Decision tree D — Intermittent connectivity

1. Record start and end times in UTC.
2. Check whether the issue affects one application, one device or many devices.
3. Capture adapter state, address, gateway and signal information during the failure.
4. Correlate DHCP, WLAN, DNS, firewall and application events.
5. Compare failures with roaming, sleep, VPN, update or power-state changes.
6. Avoid continuous high-rate testing; collect only enough evidence to identify the failing transition.

## Interpreting common outcomes

| Observation | Possible layer | Next evidence |
|---|---|---|
| No address or `169.254.x.x` | DHCP or link | Adapter, DHCP service and DHCP-client events |
| Name fails but IP works | DNS | Resolver configuration and DNS-client events |
| Timeout | Route, firewall or unavailable service | Route, firewall logs and listener state |
| Connection refused | Destination reachable but service not listening | Service status and port binding |
| TLS certificate error | Identity, time or certificate chain | System time, hostname and certificate details |
| HTTP `401` or `403` | Application identity or authorization | Account, role and application logs |
| HTTP `500` | Application failure | Application and dependency logs |

## Evidence record

For each test record:

- UTC timestamp;
- source device;
- approved destination;
- command or interface used;
- result;
- interpretation;
- next decision;
- any change approval.

## Escalation boundaries

Escalate when evidence suggests:

- firewall or protection tampering;
- unknown DNS or proxy configuration;
- unauthorized VPN or remote-access software;
- traffic to unexpected destinations;
- another pod or user's traffic;
- possible credential theft or malicious persistence.

## Authoritative basis

- Microsoft Windows networking troubleshooting documentation.
- Ubuntu networking and security documentation.
- CIS Controls v8.1.
