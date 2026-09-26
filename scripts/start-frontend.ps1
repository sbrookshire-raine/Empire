# Serve Eve Workbench + local APIs on http://127.0.0.1:8080
param(
    # Write per-turn trace records to eve-audit/eve-trace.jsonl so the research
    # bench and wiki calibrate can grade real turns. Without it those tools see
    # no records and grade pessimistically ("tools=none" is not a verdict).
    [switch]$Trace
)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$python = Join-Path $Root "venv\Scripts\python.exe"

if (-not (Test-Path $python)) {
    Write-Error "venv Python not found."
}

if ($Trace) {
    $env:EMPIRE_TRACE = "1"
    Write-Host "Tracing: ON  (eve-audit/eve-trace.jsonl)"
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
