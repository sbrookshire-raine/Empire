#Requires -Version 5.1
<#
.SYNOPSIS
  Ensure Title DNS index exists for Wiki Local glasses; optionally start a background build.

.EXAMPLE
  .\scripts\ensure-wiki-title-index.ps1
  .\scripts\ensure-wiki-title-index.ps1 -StartBackgroundBuild
#>
param(
    [string]$Year = "2026",
    [switch]$StartBackgroundBuild
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
. (Join-Path $PSScriptRoot "lib\resolve-wiki-storage.ps1")
$paths = Initialize-EmpireWikiStorageEnv -Year $Year
$indexPath = Join-Path $paths.year_dir "title-index.sqlite"

if (Test-Path -LiteralPath $indexPath) {
    Write-Host "  Wiki Title DNS index: $indexPath"
    return
}

$wikiYear = Join-Path "D:\wiki_md" $Year
if (-not (Test-Path -LiteralPath $wikiYear)) {
    Write-Warning "Wiki Local glasses down: title index missing and D:\wiki_md\$Year not found."
    Write-Warning "  Expected index: $indexPath"
    Write-Warning "  Build when corpus is available: .\scripts\build-wiki-title-index.ps1 -Year $Year -Resume"
    exit 0
}

Write-Warning "Wiki Title DNS index missing ($indexPath)."
Write-Warning "  Eve wiki lookup needs this file (~hours first build from D:\wiki_md\$Year)."

if (-not $StartBackgroundBuild) {
    Write-Warning "  Run: .\scripts\build-wiki-title-index.ps1 -Year $Year -Resume"
    Write-Warning "  Or stack with: .\scripts\ensure-wiki-title-index.ps1 -StartBackgroundBuild"
    exit 0
}

$buildScript = Join-Path $PSScriptRoot "build-wiki-title-index.ps1"
$logDir = Join-Path $paths.reports_root "logs"
if (-not (Test-Path -LiteralPath $logDir)) {
    New-Item -ItemType Directory -Force -Path $logDir | Out-Null
}
$logPath = Join-Path $logDir "title-index-build-$Year.log"
Write-Host "  Starting background Title DNS build (log: $logPath)..."

$argList = @(
    "-NoProfile",
    "-ExecutionPolicy", "Bypass",
    "-File", $buildScript,
    "-Year", $Year,
    "-Resume",
    "-IndexPath", $indexPath
)
Start-Process -FilePath "powershell.exe" `
    -ArgumentList $argList `
    -WorkingDirectory $Root `
    -WindowStyle Minimized `
    -RedirectStandardOutput $logPath `
    -RedirectStandardError (Join-Path $logDir "title-index-build-$Year.err.log") | Out-Null

Write-Host "  Build running in background. Ready strip turns green when index file appears."
