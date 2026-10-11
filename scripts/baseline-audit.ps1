#Requires -Version 5.1
<#
.SYNOPSIS
  Layered fresh-boot audit: orphans, Docker, ports, toolbelt vs pulse.

.EXAMPLE
  .\scripts\baseline-audit.ps1
  .\scripts\baseline-audit.ps1 -Json
#>
param(
    [switch]$Json,
    [switch]$FixOrphans
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$py = Join-Path $Root "venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $py)) {
    Write-Error "Missing venv at $py"
}
$env:PYTHONPATH = $Root

if ($FixOrphans) {
    & (Join-Path $Root "scripts\stop-eve-sandbox-containers.ps1") -Kill -Remove -Quiet | Out-Null
    $orphans = & $py -c @"
import json
from pipeline.baseline_audit import _orphan_llama_servers
print(json.dumps(_orphan_llama_servers()))
"@
    $parsed = $orphans | ConvertFrom-Json
    if ($parsed -is [System.Array]) {
        $rows = $parsed
    }
    elseif ($null -ne $parsed) {
        $rows = @($parsed)
    }
    else {
        $rows = @()
    }
    foreach ($row in $rows) {
        $pid = $row.pid
        if (-not $pid) { $pid = $row.Id }
        if ($pid) {
            Stop-Process -Id ([int]$pid) -Force -ErrorAction SilentlyContinue
        }
    }
}

& $py (Join-Path $Root "pipeline\baseline_audit.py")
$code = $LASTEXITCODE

if (-not $Json) {
    if ($code -eq 0) {
        Write-Host ""
        Write-Host "Baseline PASS" -ForegroundColor Green
    }
    else {
        Write-Host ""
        Write-Host "Baseline FAIL — read blockers in JSON above" -ForegroundColor Red
    }
}
exit $code
