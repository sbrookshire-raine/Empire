# Scrape a documentation site to harvest_cache (local Tool Forge).
param(
    [Parameter(Mandatory = $true)][string]$Url,
    [int]$MaxPages = 80,
    [switch]$DiscoverOnly,
    [string]$Note = ""
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$py = Join-Path $root "venv\Scripts\python.exe"
$args = @("-m", "pipeline.docs_guide_scraper", $Url, "--max-pages", $MaxPages)
if ($DiscoverOnly) { $args += "--discover-only" }
if ($Note) { $args += @("--note", $Note) }
& $py @args
