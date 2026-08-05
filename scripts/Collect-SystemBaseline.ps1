#requires -Version 5.1
<#
.SYNOPSIS
Collects a read-only Windows security and support baseline.

.DESCRIPTION
Use only on an assigned NeoLabs training system. The report can contain host,
account and network metadata. Store it in the approved evidence location and
never commit generated reports to GitHub.
#>

[CmdletBinding()]
param(
    [Parameter()]
    [string]$OutputDirectory = ".\evidence\local-baseline"
)

$ErrorActionPreference = "Continue"
$timestamp = (Get-Date).ToUniversalTime().ToString("yyyyMMddTHHmmssZ")
New-Item -ItemType Directory -Path $OutputDirectory -Force | Out-Null
$reportPath = Join-Path $OutputDirectory "windows-baseline-$timestamp.txt"

function Add-Section {
    param(
        [Parameter(Mandatory)] [string]$Title,
        [Parameter(Mandatory)] [scriptblock]$Command
    )

    Add-Content -Path $reportPath -Value "`r`n===== $Title ====="
    try {
        & $Command 2>&1 | Out-String -Width 240 | Add-Content -Path $reportPath
    }
    catch {
        Add-Content -Path $reportPath -Value "Collection error: $($_.Exception.Message)"
    }
}

@(
    "NeoLabs IT Security Support — Windows Read-Only Baseline"
    "Collected UTC: $((Get-Date).ToUniversalTime().ToString('o'))"
    "Purpose: authorised diagnosis and baseline comparison"
    "Warning: may contain host, account and network metadata; do not commit this report"
) | Set-Content -Path $reportPath -Encoding UTF8

Add-Section "Operating system" { Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber, OsArchitecture, CsDomain, CsPartOfDomain }
Add-Section "System uptime" { Get-CimInstance Win32_OperatingSystem | Select-Object LastBootUpTime, LocalDateTime }
Add-Section "Storage" { Get-Volume | Select-Object DriveLetter, FileSystem, HealthStatus, SizeRemaining, Size }
Add-Section "Network configuration" { Get-NetIPConfiguration }
Add-Section "Listening TCP connections" { Get-NetTCPConnection -State Listen | Sort-Object LocalPort | Select-Object LocalAddress, LocalPort, OwningProcess }
Add-Section "Firewall profiles" { Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction, LogFileName }
Add-Section "Microsoft Defender status" { Get-MpComputerStatus | Select-Object AntivirusEnabled, AntispywareEnabled, RealTimeProtectionEnabled, BehaviorMonitorEnabled, IoavProtectionEnabled, NISEnabled, AntivirusSignatureLastUpdated, QuickScanAge, FullScanAge }
Add-Section "BitLocker status" { Get-BitLockerVolume | Select-Object MountPoint, VolumeStatus, ProtectionStatus, EncryptionMethod, EncryptionPercentage }
Add-Section "Recent hotfixes" { Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 30 HotFixID, Description, InstalledOn }
Add-Section "Automatic services" { Get-Service | Where-Object StartType -eq 'Automatic' | Sort-Object Status, Name | Select-Object Status, Name, DisplayName }
Add-Section "Local administrators" { Get-LocalGroupMember -Group 'Administrators' | Select-Object Name, ObjectClass, PrincipalSource }
Add-Section "Local users" { Get-LocalUser | Select-Object Name, Enabled, LastLogon, PasswordRequired, PasswordExpires, UserMayChangePassword }
Add-Section "Recent system warnings and errors" { Get-WinEvent -FilterHashtable @{LogName='System'; Level=2,3; StartTime=(Get-Date).AddDays(-2)} -MaxEvents 200 | Select-Object TimeCreated, Id, ProviderName, LevelDisplayName, Message }
Add-Section "Recent security audit failures" { Get-WinEvent -FilterHashtable @{LogName='Security'; Keywords=4503599627370496; StartTime=(Get-Date).AddDays(-1)} -MaxEvents 100 | Select-Object TimeCreated, Id, ProviderName, Message }

$hash = Get-FileHash -Path $reportPath -Algorithm SHA256
"$($hash.Hash)  $([System.IO.Path]::GetFileName($reportPath))" | Set-Content -Path "$reportPath.sha256" -Encoding ASCII

Write-Host "Read-only baseline saved to: $reportPath"
Write-Host "Review and redact it before sharing through an approved channel."
