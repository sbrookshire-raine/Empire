#Requires -Version 5.1
<#
.SYNOPSIS
  Report which embedding model EMPIRE uses (Ollama + Weaviate wiki scout).
#>
$ErrorActionPreference = "Continue"
$Root = Split-Path -Parent $PSScriptRoot

Write-Host "EMPIRE Embedding Stack Audit"
Write-Host "============================="
Write-Host ""

$wikiEmbed = $env:EMPIRE_WIKI_EMBED_MODEL
if (-not $wikiEmbed) { $wikiEmbed = "nomic-embed-text" }
Write-Host "Wiki scout (pipeline/wiki_scout.py):"
Write-Host "  EMPIRE_WIKI_EMBED_MODEL = $wikiEmbed"
Write-Host "  Ollama URL              = $(if ($env:EMPIRE_OLLAMA_URL) { $env:EMPIRE_OLLAMA_URL } else { 'http://127.0.0.1:11434' })"
Write-Host ""

Write-Host "Cognee / ingest:"
Write-Host "  Production embed: nomic-embed-text (see docs/manifest/15-glossary.md)"
Write-Host "  A/B test only:    qwen3-embedding:0.6b (pipeline/embedding_ab.py)"
Write-Host ""

$ollama = Get-Command ollama -ErrorAction SilentlyContinue
if ($ollama) {
    Write-Host "Ollama local models (embedding-related):"
    & ollama list 2>$null | Select-String -Pattern "embed|nomic|bge" -CaseSensitive:$false
    Write-Host ""
}
else {
    Write-Host "Ollama CLI not on PATH — skip local model list."
    Write-Host ""
}

$weaviateUrl = if ($env:WEAVIATE_URL) { $env:WEAVIATE_URL } else { "http://127.0.0.1:8091" }
try {
    $ready = Invoke-RestMethod -Uri "$weaviateUrl/v1/.well-known/ready" -TimeoutSec 3
    Write-Host "Weaviate: reachable at $weaviateUrl"
    Write-Host "  Note: vectors were built with nomic-embed-text at index time."
    Write-Host "  Do NOT re-embed snapshots unless calibrate proves embedder failure."
}
catch {
    Write-Host "Weaviate: not reachable at $weaviateUrl (start with .\scripts\start-weaviate.ps1)"
}

Write-Host ""
Write-Host "Gap analysis verdict: audit complete — nomic-embed-text is production default."
Write-Host "See docs/RESEARCH_CLOSURE.md"
