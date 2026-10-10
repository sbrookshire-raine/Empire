#Requires -Version 5.1
param(
    [switch]$Live,
    [switch]$SyncCognee
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root
$py = Join-Path $Root "venv\Scripts\python.exe"
if (-not (Test-Path $py)) { throw "Missing venv: $py" }
$env:PYTHONPATH = $Root

$argsList = @()
if ($Live) { $argsList += "--live" }
if ($SyncCognee) { $argsList += "--sync-cognee" }

& $py -m pipeline.capability_verification @argsList
if ($LASTEXITCODE -ne 0) {
    Write-Host "verify-capabilities FAILED" -ForegroundColor Red
    exit $LASTEXITCODE
}
Write-Host "verify-capabilities PASSED" -ForegroundColor Green
exit 0
