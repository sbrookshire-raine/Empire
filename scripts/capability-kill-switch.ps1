# Disable all Eve capability arms (governance kill switch).
# Stops managed arm processes and rewrites the snapshot to empty so every
# verify_capability() check fails closed. Leaves core EMPIRE data + Cognee
# unmodified.
#
# Usage: .\scripts\capability-kill-switch.ps1 [-KeepSnapshot]

param(
    [switch]$KeepSnapshot
)

$ErrorActionPreference = "Continue"
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

Write-Host "EMPIRE capability kill switch"
Write-Host "============================="

# 1) Stop any running arm worker processes (python modules under pipeline/).
Write-Host "[1/3] Stopping arm worker processes..."
Get-CimInstance Win32_Process -Filter "Name='python.exe'" -ErrorAction SilentlyContinue |
    Where-Object { $_.CommandLine -match 'pipeline[\\/](workspace_search|query_data|read_document|create_spreadsheet|author_code|python_verify|switchboard)' } |
    ForEach-Object {
        Write-Host "  stopping pid $($_.ProcessId)"
        Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue
    }

# 2) Empty the schema snapshot so all capability verification fails closed.
if (-not $KeepSnapshot) {
    Write-Host "[2/3] Clearing tool-schema snapshot (fail closed)..."
    & $py -c @"
import json
from pathlib import Path
from pipeline import capability_registry as cr
p = cr.snapshot_path()
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps({'schema_version': cr.SCHEMA_VERSION, 'tools': {}}, indent=2) + '\n', encoding='utf-8')
print('cleared', p)
"@
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to clear snapshot"
        exit 1
    }
} else {
    Write-Host "[2/3] Skipping snapshot clear (-KeepSnapshot)."
}

# 3) Revoke egress hint (arms should run network-denied already; no-op note).
Write-Host "[3/3] Kill switch complete. Core EMPIRE data and Cognee untouched."
exit 0
