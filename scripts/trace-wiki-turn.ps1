#Requires -Version 5.1
<#
.SYNOPSIS
  Playwright + eve-trace timeline for one wiki chat turn (Architect phrasing).

.EXAMPLE
  .\scripts\trace-wiki-turn.ps1
  .\scripts\trace-wiki-turn.ps1 -Question "Go to my local Wikipedia and find what are the albums released by the Beach Boys."
#>
param(
    [string]$Question = "Go to my local Wikipedia and find what are the albums released by the Beach Boys.",
    [switch]$Headful
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
. (Join-Path $PSScriptRoot "lib\resolve-wiki-storage.ps1")
Initialize-EmpireWikiStorageEnv | Out-Null

if (-not $env:EMPIRE_TRACE) {
    Write-Warning "Start the Workbench with EMPIRE_TRACE=1 for server-side tool timings."
    Write-Warning "  .\scripts\start-frontend.ps1  (after: `$env:EMPIRE_TRACE='1')"
}

$env:PYTHONPATH = $Root
$env:EMPIRE_WIKI_REPORTS_ROOT = $env:EMPIRE_WIKI_REPORTS_ROOT
$py = Join-Path $Root "venv\Scripts\python.exe"
$args = @(
    (Join-Path $Root "scripts\trace-eve-browser.py"),
    "--question", $Question
)
if ($Headful) { $args += "--headful" }
& $py @args
exit $LASTEXITCODE
