# Sweep expired eve_staging proposals (TTL). Safe for Eve sandbox only.
# Usage: .\scripts\sweep-eve-staging.ps1
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not $Root) { $Root = "C:\EMPIRE" }
Set-Location $Root
$py = Join-Path $Root "venv\Scripts\python.exe"
if (-not (Test-Path $py)) {
    Write-Error "Missing venv python at $py"
}
$env:PYTHONPATH = $Root
$env:PYTHONIOENCODING = "utf-8"
& $py -m pipeline.eve_staging sweep
exit $LASTEXITCODE
