# Build the EMPIRE-owned Ollama models (baked parameters, since the OpenAI-compat endpoint
# ignores per-request options.num_ctx / num_predict).
#
# Run from the repo root:  .\scripts\build-empire-ollama-models.ps1
param(
    [string]$ModelfileDir = "",
    [switch]$SkipStart
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not $ModelfileDir) { $ModelfileDir = Join-Path $Root "config\ollama" }

if (-not (Get-Command ollama -ErrorAction SilentlyContinue)) {
    throw "ollama is not on PATH"
}

$models = @(
    @{ Name = "empire-fast:14b"; File = "Modelfile.empire-fast" }
    @{ Name = "empire-fast:7b"; File = "Modelfile.empire-fast-7b" }
)

foreach ($model in $models) {
    $file = Join-Path $ModelfileDir $model.File
    if (-not (Test-Path -LiteralPath $file)) {
        Write-Warning "Modelfile missing: $file"
        continue
    }
    Write-Host "Building $($model.Name) from $($model.File) ..."
    & ollama create $model.Name -f $file
    if ($LASTEXITCODE -ne 0) {
        throw "ollama create failed for $($model.Name)"
    }
    & ollama show $model.Name --parameters
    Write-Host ""
}

Write-Host "Done. Fast mode uses empire-fast:14b (see ollama-config.ts); empire-fast:7b is the A/B alternate."
