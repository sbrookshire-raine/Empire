#Requires -Version 5.1
<#
.SYNOPSIS
  Ingest curated primitives Fuel into Cognee dataset primitives_test (full cognify).
#>
param(
    [string]$LlmModel = "huihui_ai/qwen2.5-coder-abliterate:14b",
    [switch]$SkipCognify,
    [switch]$CognifyOnly
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root "venv\Scripts\python.exe"
$Raw = Join-Path $Root "data\curated_primitives\raw_materials"
$Directives = Join-Path $Root "data\curated_primitives\directives"

if (-not (Test-Path $Python)) { throw "Missing venv python: $Python" }
if (-not (Test-Path $Raw)) { throw "Missing Fuel folder: $Raw" }
if (-not (Test-Path (Join-Path $Directives "SYSTEM.md"))) {
    Write-Warning "directives/SYSTEM.md missing — query lens not ready"
}

$alive = & $Python -c "from pipeline.wiki_ops_paths import overnight_pid_alive; print(overnight_pid_alive('2017'))"
if ($alive -match "True") {
    throw "Wikipedia overnight still running — stop it before curated 14b cognify."
}

Write-Host "Checking Ollama models..."
$models = & ollama list 2>$null | Out-String
if ($models -notmatch [regex]::Escape($LlmModel) -and $models -notmatch "qwen2.5-coder-abliterate") {
    Write-Warning "LLM model $LlmModel not clearly listed in ollama list — continuing anyway if already pulled."
}
if ($models -notmatch "nomic-embed-text") {
    throw "nomic-embed-text required for Cognee embeddings. Run: ollama pull nomic-embed-text"
}

$env:EMPIRE_PRIMITIVES_LLM_MODEL = $LlmModel
$env:PYTHONPATH = $Root
$env:PYTHONUNBUFFERED = "1"
$env:PYTHONIOENCODING = "utf-8"
# Avoid session-cache LLM pulls that pin 14b in VRAM during CHUNKS recall.
$env:CACHING = "false"

$argsList = @("-u", "-m", "pipeline.ingest_curated")
if ($SkipCognify) { $argsList += "--skip-cognify" }
if ($CognifyOnly) { $argsList += "--cognify-only" }

Write-Host "Fuel files:"
Get-ChildItem $Raw -File | ForEach-Object { Write-Host ("  - " + $_.Name) }

& $Python @argsList
if ($LASTEXITCODE -ne 0) { throw "ingest_curated failed ($LASTEXITCODE)" }
Write-Host "Done. See data\curated_primitives\status\last_ingest.json"
Write-Host "Query lens: data\curated_primitives\directives\SYSTEM.md"
Write-Host "Dashboard: http://127.0.0.1:8080/primitives.html"
