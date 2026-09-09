# Embedding A/B eval — Ollama nomic vs qwen3-embedding (fixture only)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root "venv\Scripts\python.exe"

if (-not (Test-Path $Python)) {
    Write-Error "venv not found at $Python — run .\scripts\setup.ps1 first"
}

$cmd = $args[0]
if (-not $cmd) { $cmd = "eval" }

switch ($cmd) {
    "eval" {
        Write-Host "EMPIRE Embedding A/B — fixture eval (does not touch eve_memory)"
        & $Python -m pipeline.embedding_ab eval
        exit $LASTEXITCODE
    }
    "status" {
        & $Python -m pipeline.embedding_ab status
        exit $LASTEXITCODE
    }
    "pull" {
        Write-Host "Pulling candidate embed model (optional trial)..."
        ollama pull qwen3-embedding:0.6b
        exit $LASTEXITCODE
    }
    default {
        Write-Host "Usage: .\scripts\embedding-ab.ps1 [eval|status|pull]"
        Write-Host "  eval   — run data/eval/embedding_ab/cases.json (default)"
        Write-Host "  status — show Ollama model availability"
        Write-Host "  pull   — ollama pull qwen3-embedding:0.6b"
        exit 1
    }
}
