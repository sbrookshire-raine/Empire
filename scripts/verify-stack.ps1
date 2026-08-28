# Run automated integration verification for the EMPIRE stack
param(
    [switch]$SkipCognee,
    [switch]$FullIngest,
    [switch]$Json
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root "venv\Scripts\python.exe"
$Script = Join-Path $PSScriptRoot "verify-stack.py"

if (-not (Test-Path $Python)) {
    Write-Error "Python venv not found at $Python. Run .\scripts\setup.ps1 first."
}

$argsList = @($Script)
if ($SkipCognee) { $argsList += "--skip-cognee" }
if ($FullIngest) { $argsList += "--full-ingest" }
if ($Json) { $argsList += "--json" }

& $Python @argsList
exit $LASTEXITCODE
