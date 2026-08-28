# Gracefully start EMPIRE services in dependency order (for dashboard / operational use)
param(
    [string[]]$Only = @(),
    [switch]$SkipOllamaCheck
)

$ErrorActionPreference = "Stop"

# Mount the Cognee NTFS VHDX (heavy graph/vector DB on V:, backed by I:) BEFORE any Cognee
# consumer starts. Non-fatal: warn and continue if elevation/VHDX is missing.
try {
    & (Join-Path $PSScriptRoot 'mount-cognee-vhdx.ps1')
}
catch {
    $mountErr = $_.Exception.Message
    Write-Warning ('roll-in: Cognee VHDX mount step failed ({0}). Cognee needs V: - see scripts/mount-cognee-vhdx.ps1.' -f $mountErr)
}

try {
    & (Join-Path $PSScriptRoot 'ensure-cognee-postgres.ps1')
}
catch {
    Write-Warning ('roll-in: Cognee Postgres step failed ({0}). Ingest/recall need Docker Desktop.' -f $_.Exception.Message)
}

. (Join-Path $PSScriptRoot "lib\service-control.ps1")

$params = @{}
if ($Only.Count -gt 0) { $params.Only = $Only }
if ($SkipOllamaCheck) { $params.SkipExternalCheck = $true }

Invoke-EmpireRollIn @params
