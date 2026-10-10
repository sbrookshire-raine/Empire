# Fresh Cognee file root + seed Architect↔Eve language in graph memory.
# Usage: .\scripts\setup-architect-language-memory.ps1
# Requires: Docker Postgres (ensure-cognee-postgres), Ollama with nomic-embed-text for eve_core embed step.

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Py = Join-Path $Root "venv\Scripts\python.exe"

. (Join-Path $PSScriptRoot "lib\cognee-storage.ps1")
$cogneeRoot = Ensure-EmpireCogneeRoot
$env:EMPIRE_COGNEE_ROOT = $cogneeRoot
Write-Host "Cognee file root: $cogneeRoot"

& (Join-Path $PSScriptRoot "ensure-cognee-postgres.ps1")

Write-Host "Harvesting vault voice (static digest if no Obsidian path)..."
& $Py (Join-Path $Root "scripts\harvest-architect-voice-from-vault.py")

$languageFiles = @(
    "data\curated_primitives\raw_materials\architect-intent-vocabulary.md",
    "data\curated_primitives\raw_materials\architect-vault-voice-supplement.md",
    "data\curated_primitives\raw_materials\architect-eve-language-bridge.md"
)

$env:PYTHONPATH = $Root
$env:COGNEE_SKIP_CONNECTION_TEST = "true"
$env:CACHING = "false"

Push-Location $Root
try {
    foreach ($rel in $languageFiles) {
        $path = Join-Path $Root $rel
        if (-not (Test-Path $path)) { throw "Missing $path" }
        $content = Get-Content -Path $path -Raw -Encoding UTF8
        $name = Split-Path -Leaf $path
        Write-Host "remember -> eve_memory : $name"
        & $Py -m pipeline.cognee_worker remember --content $content --dataset eve_memory
        if ($LASTEXITCODE -ne 0) { throw "remember eve_memory failed for $name" }
        Write-Host "remember -> eve_core : $name"
        & $Py -m pipeline.cognee_worker remember --content $content --dataset eve_core
        if ($LASTEXITCODE -ne 0) { throw "remember eve_core failed for $name" }
    }
} finally {
    Pop-Location
}

Write-Host "Language bridge seeded in eve_memory + eve_core."
Write-Host "Optional: .\scripts\optimize-eve-memory.ps1  (workbench harvest into eve_core)"
Write-Host "Done."
