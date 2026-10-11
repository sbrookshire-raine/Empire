#Requires -Version 5.1
<#
.SYNOPSIS
  Architect query battery — wiki green path, session inject, REA routing (+ optional live Eve).

.EXAMPLE
  .\scripts\run-query-battery.ps1 -Tier fast
  .\scripts\run-query-battery.ps1 -Tier live
#>
param(
    [ValidateSet("fast", "live", "all")]
    [string]$Tier = "fast"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
. (Join-Path $PSScriptRoot "lib\resolve-wiki-storage.ps1")
Initialize-EmpireWikiStorageEnv | Out-Null
$env:PYTHONPATH = $Root
$py = Join-Path $Root "venv\Scripts\python.exe"
& $py (Join-Path $Root "scripts\run-query-battery.py") --tier $Tier
exit $LASTEXITCODE
