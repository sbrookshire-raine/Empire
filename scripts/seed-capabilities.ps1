# Seed the EMPIRE capability registry + tool-schema snapshot (idempotent).
#
# Activation step for the fail-closed governance layer. Re-running recomputes
# the same canonical tool signatures and rewrites the snapshot — safe to call
# after any deliberate arm schema change. If a schema drifts *without* re-seeding,
# `mechanic-green` reports it fail-closed.

param()

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not $Root) { $Root = "C:\EMPIRE" }
Set-Location $Root

$py = Join-Path $Root "venv\Scripts\python.exe"
if (-not (Test-Path $py)) {
    Write-Error "Missing venv python at $py"
    exit 1
}

$env:PYTHONPATH = $Root
$env:PYTHONIOENCODING = "utf-8"

Write-Host "EMPIRE capability seed"
Write-Host "======================"

& $py -m pipeline.capability_seed
if ($LASTEXITCODE -ne 0) {
    Write-Error "Capability seed failed (exit $LASTEXITCODE)"
    exit 1
}
exit 0
