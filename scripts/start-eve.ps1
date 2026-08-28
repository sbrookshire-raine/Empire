# Start Eve in headless API mode (port 2000). Run from EMPIRE repo root.
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$AgentDir = Join-Path $Root "agents\empire-task-agent"

if (-not (Test-Path (Join-Path $AgentDir "package.json"))) {
    Write-Error "agents/empire-task-agent not found. Run Phase 5 scaffold first."
}

$env:EMPIRE_ROOT = $Root
$env:POCKETBASE_URL = if ($env:POCKETBASE_URL) { $env:POCKETBASE_URL } else { "http://127.0.0.1:8090" }
$env:OLLAMA_BASE_URL = if ($env:OLLAMA_BASE_URL) { $env:OLLAMA_BASE_URL } else { "http://localhost:11434/v1" }
$env:OLLAMA_MODEL = if ($env:OLLAMA_MODEL) { $env:OLLAMA_MODEL } else { "llama3.1:8b" }

Write-Host "EMPIRE Eve agent (production API on 127.0.0.1:2000)"
Write-Host "  Run from repo root: cd $Root"
Write-Host "  Interactive REPL:   cd agents\empire-task-agent; npm run dev"
Write-Host ""
Write-Host "  EMPIRE_ROOT:      $Root"
Write-Host "  OLLAMA_BASE_URL:  $env:OLLAMA_BASE_URL"
Write-Host "  OLLAMA_MODEL:     $env:OLLAMA_MODEL"
Write-Host "  POCKETBASE_URL:   $env:POCKETBASE_URL"
Write-Host ""
Write-Host "Preparing the Eve production build..."
Write-Host ""

Set-Location $AgentDir
& (Join-Path $Root "venv\Scripts\python.exe") `
    (Join-Path $Root "scripts\ensure-eve-build.py")
if ($LASTEXITCODE -ne 0) {
    throw "Eve production build preparation failed."
}

Write-Host "Starting built Eve server (Ctrl+C to stop)..."
$arguments = @("exec", "--", "eve", "start", "--host", "127.0.0.1", "--port", "2000")
& npm.cmd @arguments
