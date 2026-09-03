#Requires -Version 5.1
<#
.SYNOPSIS
  Batch-embed Empire Workbench Memory Bank + Skills into Cognee eve_memory (V:\Cognee).
.NOTES
  Active Tools (flattened codebases) stay on disk — Eve reads them via workbench_read_file.
#>
param(
    [string]$Dataset = "eve_memory",
    [int]$Limit = 0,
    [switch]$Resume
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

$argsList = @("-u", (Join-Path $Root "scripts\ingest_workbench.py"), "--dataset", $Dataset)
if ($Limit -gt 0) { $argsList += @("--limit", $Limit) }
if ($Resume) { $argsList += "--resume" }

Write-Host "Ingesting C:\Empire_Workbench (01 + 02) -> dataset $Dataset on V:\Cognee ..."
& $Python @argsList
if ($LASTEXITCODE -ne 0) { throw "ingest_workbench failed ($LASTEXITCODE)" }
