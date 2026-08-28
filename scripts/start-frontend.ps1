# Serve Eve Workbench + local APIs on http://127.0.0.1:8080
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$python = Join-Path $Root "venv\Scripts\python.exe"

if (-not (Test-Path $python)) {
    Write-Error "venv Python not found."
}

Write-Host "EMPIRE Eve Workbench: http://127.0.0.1:8080/eve.html"
Write-Host "Dashboard:        http://127.0.0.1:8080/dashboard.html"
Write-Host "Control API:      http://127.0.0.1:8080/api/services/*"
Write-Host "Health API:       http://127.0.0.1:8080/api/memory/status"
Write-Host "PocketBase API:   http://127.0.0.1:8090"
Write-Host "Press Ctrl+C to stop."
Write-Host ""

Set-Location $Root
$arguments = @("-m", "frontend.serve")
& $python @arguments
