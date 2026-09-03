#Requires -Version 5.1
<#
.SYNOPSIS
  Curate a small eve_core dataset from the workbench harvest for useful Eve recall.
.DESCRIPTION
  Bulk eve_memory is an archive. This scores your project/interests files, writes
  00_Core_Profile/USER_CORE_PROFILE.md, and embeds ~60 high-signal docs into eve_core.
  Chat recall prefers eve_core automatically.
.EXAMPLE
  .\scripts\optimize-eve-memory.ps1 -DryRun
.EXAMPLE
  .\scripts\optimize-eve-memory.ps1 -Fresh
#>
param(
    [int]$MaxFiles = 60,
    [switch]$DryRun,
    [switch]$Fresh,
    [switch]$Memify
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root "venv\Scripts\python.exe"

if (-not (Test-Path $Python)) { throw "Missing venv: $Python" }
if (-not (Test-Path "V:\Cognee")) {
    throw "V:\Cognee not mounted. Plug in T7 and run Start-EMPIRE.bat first."
}

$models = & ollama list 2>$null | Out-String
if ($models -notmatch "nomic-embed-text") {
    throw "nomic-embed-text required. Run: ollama pull nomic-embed-text"
}

$env:PYTHONPATH = $Root
$env:PYTHONUNBUFFERED = "1"
$env:PYTHONIOENCODING = "utf-8"
$env:CACHING = "false"
$env:COGNEE_SKIP_CONNECTION_TEST = "true"

$argsList = @(
    "-u",
    (Join-Path $Root "scripts\optimize_eve_memory.py"),
    "--max-files",
    $MaxFiles
)
if ($DryRun) { $argsList += "--dry-run" }
if ($Fresh) { $argsList += "--fresh" }
if ($Memify) { $argsList += "--memify" }

Write-Host "Optimizing workbench memory -> dataset eve_core on V:\Cognee ..."
& $Python @argsList
if ($LASTEXITCODE -ne 0) { throw "optimize_eve_memory failed ($LASTEXITCODE)" }
