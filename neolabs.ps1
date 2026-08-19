$ErrorActionPreference = 'Stop'
$env:NEOLABS_LAB_BASE_URL = 'https://pg1wb0sklb.execute-api.us-east-1.amazonaws.com'
$client = Join-Path $PSScriptRoot 'tools\neolabs.py'
$ticketsClient = Join-Path $PSScriptRoot 'tools\support_tickets.py'
if (-not (Test-Path $client)) { throw 'NeoLabs client file is missing from this toolkit.' }

$scriptToRun = $client
$forwardArgs = @($args)
if ($args.Count -gt 0 -and $args[0].ToString().ToLowerInvariant() -eq 'tickets') {
    if (-not (Test-Path $ticketsClient)) { throw 'NeoLabs Support ticket client is missing from this toolkit.' }
    $scriptToRun = $ticketsClient
    if ($args.Count -gt 1) {
        $forwardArgs = @($args[1..($args.Count - 1)])
    } else {
        $forwardArgs = @()
    }
}

if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 $scriptToRun @forwardArgs
    exit $LASTEXITCODE
}
if (Get-Command python -ErrorAction SilentlyContinue) {
    & python $scriptToRun @forwardArgs
    exit $LASTEXITCODE
}
throw 'Python 3.10 or newer is required.'
