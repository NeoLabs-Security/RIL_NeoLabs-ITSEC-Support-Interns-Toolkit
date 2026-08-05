# Module 2 — Windows Security Diagnostics

## Purpose

This module teaches a repeatable, evidence-preserving way to diagnose Windows endpoint problems without weakening the device. The process begins with system identity and time, then moves through services, logs, updates, protection status, storage and networking.

## Learning outcomes

An intern should be able to:

- identify the Windows edition, build, device and signed-in context;
- collect relevant system information without exposing secrets;
- use Event Viewer and PowerShell to locate useful events;
- check Microsoft Defender, Windows Firewall, BitLocker and update state;
- distinguish service failure from network, DNS, account or application failure;
- document current state before proposing a change;
- recognize indicators that require SOC escalation.

## Diagnostic order

### 1. Confirm the scope

Record the device name, affected user, operating-system version, issue start time, recent changes and whether the issue affects other users or devices.

Useful read-only commands include:

```powershell
Get-ComputerInfo | Select-Object WindowsProductName,WindowsVersion,OsBuildNumber,CsName
Get-Date
whoami
```

Do not paste access tokens, passwords or recovery keys into the ticket.

### 2. Check resource and service state

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 15
Get-Service | Where-Object Status -ne 'Running'
Get-CimInstance Win32_LogicalDisk | Select-Object DeviceID,Size,FreeSpace
```

A stopped service is not automatically the root cause. Confirm whether the service is expected to run and what depends on it.

### 3. Review event evidence

Start with a narrow time window and a specific symptom.

```powershell
$start = (Get-Date).AddHours(-2)
Get-WinEvent -FilterHashtable @{LogName='System'; StartTime=$start; Level=2,3} -ErrorAction SilentlyContinue |
  Select-Object -First 50 TimeCreated,Id,ProviderName,LevelDisplayName,Message
```

Important locations may include:

- Windows Logs: System, Application and Security;
- Microsoft-Windows-Windows Defender/Operational;
- Microsoft-Windows-Windows Firewall With Advanced Security;
- Microsoft-Windows-DNS-Client/Operational;
- Microsoft-Windows-Dhcp-Client event channels;
- Microsoft-Windows-WLAN-AutoConfig/Operational.

Do not clear logs as a troubleshooting shortcut.

### 4. Check protection state

```powershell
Get-MpComputerStatus | Select-Object AntivirusEnabled,RealTimeProtectionEnabled,AntivirusSignatureLastUpdated
Get-NetFirewallProfile | Select-Object Name,Enabled,DefaultInboundAction,DefaultOutboundAction
Get-BitLockerVolume -ErrorAction SilentlyContinue | Select-Object MountPoint,VolumeStatus,ProtectionStatus
```

Unexpectedly disabled protection, exclusions the user did not request, or failed security services may indicate an incident.

### 5. Check update and restart context

Confirm update history, pending restart indicators and the relevant Windows release-health information before repeatedly reinstalling or rolling back components.

Record:

- last successful update;
- failed update identifier;
- error code;
- available storage;
- restart state;
- whether the same failure affects similar devices.

### 6. Check networking by layer

```powershell
Get-NetAdapter
Get-NetIPConfiguration
Resolve-DnsName example.invalid -ErrorAction SilentlyContinue
Test-NetConnection 127.0.0.1 -Port 443 -InformationLevel Detailed
```

Use the actual approved target in a support environment. A failed name lookup, failed route and refused application port are different problems.

## Security baseline principle

Microsoft security baselines represent a recommended, broadly tested configuration starting point. They still require organizational review, compatibility testing and change control. Interns must not apply a complete baseline blindly to a live device.

## Escalate to the SOC when

- Defender reports malware or tampering;
- protection services were disabled unexpectedly;
- a new administrator account or privilege appears;
- the user reports unknown logins or repeated MFA prompts;
- logs appear deleted or altered;
- suspicious scripts, scheduled tasks or remote-access tools are found;
- evidence suggests credential theft or lateral movement.

## Evidence checklist

- [ ] Device, user and UTC time recorded.
- [ ] Symptom reproduced safely.
- [ ] Relevant events exported or referenced.
- [ ] Security controls checked and left enabled.
- [ ] Changes separated from diagnostic observations.
- [ ] Secrets and personal data redacted.
- [ ] Escalation decision documented.

## Authoritative basis

- Microsoft Windows security baseline documentation.
- Microsoft Windows networking and TCP/IP troubleshooting guidance.
- NIST SP 800-61 Rev. 3.
- CIS Controls v8.1, especially Controls 4, 5, 6, 7 and 8.
