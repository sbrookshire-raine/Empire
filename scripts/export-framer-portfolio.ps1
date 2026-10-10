#Requires -Version 5.1
<#
.SYNOPSIS
  Verify Framer portfolio CSV pack exists (data/framer-portfolio/).

.EXAMPLE
  .\scripts\export-framer-portfolio.ps1
#>
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$dir = Join-Path $root 'data\framer-portfolio'
$required = @(
    'README.md',
    'site-meta.csv',
    'eras.csv',
    'timeline.csv',
    'slides.csv',
    'case-studies.csv',
    'lessons.csv',
    'skills.csv',
    'portfolio-import.json'
)
Write-Host "Framer import pack: $dir"
foreach ($f in $required) {
    $p = Join-Path $dir $f
    if (-not (Test-Path $p)) { throw "Missing: $p" }
    $n = (Import-Csv $p -ErrorAction SilentlyContinue).Count
    if ($f -eq 'site-meta.csv') { $n = 1 }
    if ($f -eq 'portfolio-import.json' -or $f -eq 'README.md') {
        Write-Host "  OK $f"
    } else {
        Write-Host "  OK $f ($n rows)"
    }
}
Write-Host ""
Write-Host "Import in Framer: CMS -> Import CSV from data/framer-portfolio/"
Write-Host "Guide: data/framer-portfolio/README.md"
