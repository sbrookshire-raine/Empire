# EMPIRE idempotent local setup (Windows PowerShell)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

Write-Host "==> EMPIRE setup at $Root"

$dirs = @(
    ".cursor/rules",
    ".cursor/agents",
    "backend/pocketbase/pb_migrations",
    "mcp",
    "pipeline",
    "mock_data_ingest",
    "frontend/partials",
    "cognee",
    "agents",
    "docs"
)
foreach ($d in $dirs) {
    New-Item -ItemType Directory -Force -Path (Join-Path $Root $d) | Out-Null
}

$venvPython = Join-Path $Root "venv/Scripts/python.exe"
if (-not (Test-Path $venvPython)) {
    Write-Host "==> Creating Python venv"
    python -m venv (Join-Path $Root "venv")
}
Write-Host "==> Installing Python dependencies"
& $venvPython -m pip install --upgrade pip -q
& $venvPython -m pip install -r requirements.txt -q

$pbDir = Join-Path $Root "backend/pocketbase"
$pbExe = Join-Path $pbDir "pocketbase.exe"
if (-not (Test-Path $pbExe)) {
    Write-Host "==> Downloading PocketBase for Windows amd64"
    $zipUrl = "https://github.com/pocketbase/pocketbase/releases/download/v0.28.4/pocketbase_0.28.4_windows_amd64.zip"
    $zipPath = Join-Path $pbDir "pocketbase.zip"
    Invoke-WebRequest -Uri $zipUrl -OutFile $zipPath
    Expand-Archive -Path $zipPath -DestinationPath $pbDir -Force
    Remove-Item $zipPath -Force
}

$envExample = Join-Path $Root ".env.example"
$envLocal = Join-Path $Root ".env.local"
if (-not (Test-Path $envLocal)) {
    Copy-Item $envExample $envLocal
    Write-Host "==> Created .env.local from .env.example"
}

Get-Content $envLocal | ForEach-Object {
    if ($_ -match '^\s*([^#][^=]+)=(.*)$') {
        [System.Environment]::SetEnvironmentVariable($matches[1].Trim(), $matches[2].Trim(), "Process")
    }
}

$adminEmail = if ($env:POCKETBASE_ADMIN_EMAIL) { $env:POCKETBASE_ADMIN_EMAIL } else { "admin@empire.local" }
$adminPassword = if ($env:POCKETBASE_ADMIN_PASSWORD) { $env:POCKETBASE_ADMIN_PASSWORD } else { "empire-admin-change-me" }

# Cognee databases (lancedb + kuzu + sqlite) require NTFS semantics. The 4TB I: drive is
# exFAT, where lancedb fails ("Incorrect function", os error 1). To keep heavy storage off
# C:, the graph/vector DB lives on an NTFS VHDX backed by I: (I:\EMPIRE_VHDX\empire_cognee.vhdx)
# mounted at V:, so default to V:\Cognee. Override with EMPIRE_COGNEE_ROOT for any NTFS volume.
# Create the VHDX once (admin): scripts\create-cognee-vhdx.ps1 ; mount: scripts\mount-cognee-vhdx.ps1
$cogneeSystemDir = if ($env:EMPIRE_COGNEE_ROOT) { $env:EMPIRE_COGNEE_ROOT } else { "V:\Cognee" }
if (Test-Path (Split-Path $cogneeSystemDir -Qualifier)) {
    New-Item -ItemType Directory -Force -Path $cogneeSystemDir | Out-Null
} else {
    Write-Warning "Cognee target drive $(Split-Path $cogneeSystemDir -Qualifier) is not mounted. Run scripts\mount-cognee-vhdx.ps1 (as admin) before ingesting."
}
$cogneeEnv = Join-Path $Root "config\cognee.env"
@(
    "LLM_PROVIDER=ollama",
    "LLM_MODEL=llama3.1:latest",
    "LLM_ENDPOINT=http://localhost:11434/v1",
    "LLM_API_KEY=ollama",
    "",
    "EMBEDDING_PROVIDER=ollama",
    "EMBEDDING_MODEL=nomic-embed-text:latest",
    "EMBEDDING_ENDPOINT=http://localhost:11434/api/embed",
    "EMBEDDING_DIMENSIONS=768",
    "HUGGINGFACE_TOKENIZER=nomic-ai/nomic-embed-text-v1.5",
    "",
    "ENABLE_BACKEND_ACCESS_CONTROL=false",
    "SYSTEM_ROOT_DIRECTORY=$cogneeSystemDir"
) | Set-Content -Path $cogneeEnv -Encoding UTF8
Write-Host "==> Cognee storage (NTFS, required for lancedb/kuzu): $cogneeSystemDir"

Write-Host "==> Upserting PocketBase superuser ($adminEmail)"
Push-Location $pbDir
& $pbExe superuser upsert $adminEmail $adminPassword
Pop-Location

Write-Host "==> Setup complete."
Write-Host "    Start PocketBase: scripts/start-pocketbase.ps1"
Write-Host "    Admin UI:         http://127.0.0.1:8090/_/"

