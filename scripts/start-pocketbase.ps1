# Start PocketBase in the foreground (Ctrl+C to stop)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$pbExe = Join-Path $Root "backend/pocketbase/pocketbase.exe"
if (-not (Test-Path $pbExe)) {
    Write-Error "PocketBase not found. Run scripts/setup.ps1 first."
}
Set-Location (Join-Path $Root "backend/pocketbase")
Write-Host "Starting PocketBase at http://127.0.0.1:8090"
& $pbExe serve --http=127.0.0.1:8090
