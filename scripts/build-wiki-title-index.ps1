#Requires -Version 5.1
<#
.SYNOPSIS
  Build the Wikipedia Title DNS SQLite index from D:\wiki_md frontmatter.

.NOTES
  Default year 2026. Writes I:\EMPIRE_DATA\wiki-reports\{year}\title-index.sqlite
  Optional redirects TSV: I:\EMPIRE_DATA\wiki-reports\{year}\redirects.tsv
#>
param(
    [string]$Year = "2026",
    [int]$LimitBatches = 0,
    [string]$IndexPath = "",
    [string]$RedirectsPath = "",
    [switch]$Resume,
    [switch]$Links
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root "venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $Python)) {
    throw "Missing venv python: $Python"
}

$args = @("-m", "pipeline.wiki_title_dns", "build", "--year", $Year)
if ($LimitBatches -gt 0) {
    $args += @("--limit-batches", "$LimitBatches")
}
if ($IndexPath) {
    $args += @("--index", $IndexPath)
}
if ($RedirectsPath) {
    $args += @("--redirects", $RedirectsPath)
}
if ($Resume) {
    $args += "--resume"
}

if ($Links) {
    $linkArgs = @("-m", "pipeline.wiki_title_dns", "links", "--year", $Year)
    if ($IndexPath) { $linkArgs += @("--index", $IndexPath) }
    Write-Host "Title DNS links ($Year)"
    & $Python @linkArgs
    if ($LASTEXITCODE -ne 0) {
        throw "title link build failed ($LASTEXITCODE)"
    }
    return
}

Write-Host "Title DNS build ($Year)"
Write-Host "wiki_md: D:\wiki_md\$Year  (override with WIKI_ROOT)"
Write-Host "index:   I:\EMPIRE_DATA\wiki-reports\$Year\title-index.sqlite"
& $Python @args
if ($LASTEXITCODE -ne 0) {
    throw "title index build failed ($LASTEXITCODE)"
}
