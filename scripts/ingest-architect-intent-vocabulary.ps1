# Remember Architect intent vocabulary in Cognee (eve_memory).
# Usage: .\scripts\ingest-architect-intent-vocabulary.ps1
# Requires: Docker Postgres + Cognee (E:\EMPIRE_COGNEE or EMPIRE_COGNEE_ROOT).

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
. (Join-Path $PSScriptRoot "lib\cognee-storage.ps1")
$sources = @(
    (Join-Path $root "data\curated_primitives\raw_materials\architect-intent-vocabulary.md"),
    (Join-Path $root "data\curated_primitives\raw_materials\architect-vault-voice-supplement.md"),
    (Join-Path $root "data\curated_primitives\raw_materials\architect-eve-language-bridge.md"),
    (Join-Path $root "data\curated_primitives\raw_materials\architect-navigation-profile.md")
)
$py = Join-Path $root "venv\Scripts\python.exe"

foreach ($src in $sources) {
    if (-not (Test-Path $src)) {
        throw "Missing source: $src (run harvest-architect-voice-from-vault.py if supplement missing)"
    }
}

$cogneeRoot = Ensure-EmpireCogneeRoot
$env:EMPIRE_COGNEE_ROOT = $cogneeRoot
Write-Host "Cognee file root: $cogneeRoot"

$env:PYTHONPATH = $root
$env:COGNEE_SKIP_CONNECTION_TEST = "true"
$env:CACHING = "false"

Push-Location $root
try {
    foreach ($src in $sources) {
        $content = Get-Content -Path $src -Raw -Encoding UTF8
        $name = Split-Path -Leaf $src
        Write-Host "Remembering $name -> dataset eve_memory ..."
        & $py -m pipeline.cognee_worker remember --content $content --dataset eve_memory
        if ($LASTEXITCODE -ne 0) {
            throw "cognee_worker remember failed ($LASTEXITCODE) for $name. Is Docker Postgres up?"
        }
    }
} finally {
    Pop-Location
}

Write-Host "Optional: .\scripts\optimize-eve-memory.ps1  (promote highlights to eve_core)"
Write-Host "Done."
