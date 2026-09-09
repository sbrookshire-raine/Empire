#Requires -Version 5.1
<#
.SYNOPSIS
  Ingest DAZE canonical profile + DAZE_flattened_3.txt chunks into Cognee.
.NOTES
  Requires V:\Cognee mounted and Ollama with nomic-embed-text.
#>
param(
    [string]$Dataset = "eve_memory",
    [switch]$DryRun,
    [switch]$ProfileOnly
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root "venv\Scripts\python.exe"

if (-not (Test-Path $Python)) { throw "Missing venv: $Python" }
if (-not $DryRun -and -not (Test-Path "V:\Cognee")) {
    throw "V:\Cognee not mounted. Plug in T7 and run Start-EMPIRE.bat first."
}

$env:PYTHONPATH = $Root
$env:PYTHONUNBUFFERED = "1"
$env:CACHING = "false"
$env:COGNEE_SKIP_CONNECTION_TEST = "true"

$argsList = @("-u", (Join-Path $Root "scripts\ingest_daze_product.py"), "--dataset", $Dataset)
if ($DryRun) { $argsList += "--dry-run" }
if ($ProfileOnly) { $argsList += "--skip-flattened" }

Write-Host "Ingesting DAZE product canon -> dataset $Dataset ..."
& $Python @argsList
if ($LASTEXITCODE -ne 0) { throw "ingest_daze_product failed ($LASTEXITCODE)" }
