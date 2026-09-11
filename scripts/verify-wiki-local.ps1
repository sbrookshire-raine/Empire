#Requires -Version 5.1
<#
.SYNOPSIS
  Preflight Wiki Local: Docker, Weaviate :8091, optional Stranger Things lookup smoke.

.EXAMPLE
  .\scripts\verify-wiki-local.ps1
  .\scripts\verify-wiki-local.ps1 -ArchivePath "I:\EMPIRE_DATA\weaviate_v2_archive\weaviate"
  .\scripts\verify-wiki-local.ps1 -StartIfDown
#>
param(
    [string]$ArchivePath = "D:\weaviate_v2_archive\weaviate",
    [switch]$StartIfDown,
    [switch]$SkipSearch
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root "venv\Scripts\python.exe"
$ApiKey = "WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih"
$fail = 0

function Test-WeaviateReady {
    try {
        $headers = @{ Authorization = "Bearer $ApiKey" }
        $r = Invoke-WebRequest -Uri "http://127.0.0.1:8091/v1/.well-known/ready" `
            -Headers $headers -UseBasicParsing -TimeoutSec 5
        return $r.StatusCode -ge 200 -and $r.StatusCode -lt 400
    }
    catch { return $false }
}

Write-Host "Wiki Local preflight"
Write-Host "===================="

$docker = Get-Command docker -ErrorAction SilentlyContinue
if (-not $docker) {
    Write-Host "FAIL  Docker not on PATH"
    exit 1
}
Write-Host "OK    Docker on PATH"

if (-not (Test-Path -LiteralPath $ArchivePath)) {
    Write-Host "FAIL  Weaviate archive missing: $ArchivePath"
    Write-Host "      Pass -ArchivePath if your copy lives on I: (external drive)."
    exit 1
}
Write-Host "OK    Archive path exists: $ArchivePath"

if (-not (Test-WeaviateReady)) {
    if ($StartIfDown) {
        Write-Host "WARN  Weaviate not ready — starting..."
        & (Join-Path $PSScriptRoot "start-weaviate.ps1") -ArchivePath $ArchivePath
    }
    else {
        Write-Host "FAIL  Weaviate not ready on http://127.0.0.1:8091"
        Write-Host "      Run: .\scripts\start-weaviate.ps1 -ArchivePath '$ArchivePath'"
        Write-Host "      Or:  .\scripts\verify-wiki-local.ps1 -StartIfDown"
        exit 1
    }
}

if (-not (Test-WeaviateReady)) {
    Write-Host "FAIL  Weaviate still not ready after start attempt"
    exit 1
}
Write-Host "OK    Weaviate ready on :8091"

if (-not (Test-Path $Python)) {
    Write-Host "WARN  Skip search smoke — venv python missing"
    exit 0
}

if ($SkipSearch) {
    Write-Host ""
    Write-Host "PASS  Wiki Local preflight (search skipped)"
    exit 0
}

Write-Host ""
Write-Host "Smoke  Weaviate search (Stranger Things 80s song)..."
$code = @"
import sys
from pipeline.wiki_scout import search
q = "what 80s song was popularized again in Stranger Things"
r = search(q, year="2026", write_files=False, interpret=True, use_rerank=False)
if not r.get("ok"):
    print("SEARCH_FAIL", r.get("error"))
    sys.exit(1)
titles = r.get("titles") or []
blob = " | ".join(titles).casefold()
if "running up that hill" not in blob:
    print("SEARCH_WARN top titles:", titles[:5])
    sys.exit(2)
print("SEARCH_OK", titles[0] if titles else "?")
"@

$env:PYTHONPATH = $Root
& $Python -c $code
$searchExit = $LASTEXITCODE
if ($searchExit -eq 0) {
    Write-Host "OK    Search returned Running Up That Hill class hit"
    Write-Host ""
    Write-Host "PASS  Wiki Local ready for Eve testing"
    Write-Host "      Enable Toolbelt: Wiki Local  |  http://127.0.0.1:8080/eve.html"
    exit 0
}
if ($searchExit -eq 2) {
    Write-Host "WARN  Weaviate up but top titles unexpected — check archive year / embed"
    exit 2
}
Write-Host "FAIL  Search smoke failed (Weaviate up but query failed)"
exit 1
