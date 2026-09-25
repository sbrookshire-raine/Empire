<#
.SYNOPSIS
    Start (or restart) the local SearXNG instance that backs the searxng_search tool.

.DESCRIPTION
    E-35: the one capability E-34 measured as missing — a query with no URL and no archive hit.
    This runs SearXNG in Docker on host port 8888 with the repo's settings mounted, which is what
    switches on the JSON output the tool needs. No cloud key, no data leaving the box.

    Then verify:
        .\venv\Scripts\python.exe -m pipeline.search_scout "local first llm tool calling"
        .\venv\Scripts\python.exe scripts\run-research-bench.py --baseline --require-ready

    Docker Desktop must be running. Stop with:  docker rm -f empire-searxng
#>
param(
    [int]$Port = 8888,
    [string]$Image = "searxng/searxng:latest",
    [switch]$Recreate
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Settings = Join-Path $Root "config\searxng"
if (-not (Test-Path $Settings)) { throw "Missing SearXNG settings at $Settings" }
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) { throw "docker is not on PATH (start Docker Desktop)" }

$existing = docker ps -a --filter "name=empire-searxng" --format "{{.Names}}" | Select-Object -First 1
if ($existing -and $Recreate) {
    Write-Host "Recreating empire-searxng..."
    docker rm -f empire-searxng | Out-Null
    $existing = $null
}
if ($existing) {
    Write-Host "empire-searxng already exists - starting it..."
    docker start empire-searxng | Out-Null
} else {
    Write-Host "Pulling $Image (first run only)..."
    docker pull $Image | Out-Null
    Write-Host "Starting empire-searxng on http://127.0.0.1:$Port ..."
    docker run -d --name empire-searxng --restart unless-stopped `
        -p "${Port}:8080" `
        -v "${Settings}:/etc/searxng:rw" `
        -e "SEARXNG_BASE_URL=http://127.0.0.1:$Port/" `
        $Image | Out-Null
}

$ready = $false
for ($i = 0; $i -lt 30; $i++) {
    Start-Sleep -Seconds 2
    try {
        $probe = Invoke-RestMethod -Uri "http://127.0.0.1:$Port/search?q=empire&format=json" -TimeoutSec 10
        if ($probe.results) { $ready = $true; break }
    } catch { }
}
if ($ready) {
    Write-Host "SearXNG ready on http://127.0.0.1:$Port (JSON enabled, $($probe.results.Count) results for 'empire')." -ForegroundColor Green
    Write-Host "Tool: searxng_search (admits Web Research). Env override: EMPIRE_SEARXNG_URL"
} else {
    Write-Warning "SearXNG did not answer with JSON within 60s. Check: docker logs empire-searxng"
}
