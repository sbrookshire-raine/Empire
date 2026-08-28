# Re-ingest all mock files in FAST mode (seconds each, not minutes).
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root
$env:PYTHONPATH = $Root

$files = @(
    "mock_data_ingest/github_issue.json",
    "mock_data_ingest/slack_thread.json",
    "mock_data_ingest/email_sample.md"
)

Write-Host "Fast re-ingest of $($files.Count) mock files (no slow Ollama graph pass)..."
$started = Get-Date

foreach ($file in $files) {
    Write-Host ""
    Write-Host "=== $file ==="
    & "$Root\venv\Scripts\python.exe" -m pipeline.ingest_local --file $file
    if ($LASTEXITCODE -ne 0) { Write-Error "Ingest failed for $file" }
}

$elapsed = (Get-Date) - $started
Write-Host ""
Write-Host ("All mock files ingested in {0:N0}s total." -f $elapsed.TotalSeconds)
Write-Host "For deep graph extraction later, use: .\scripts\ingest-mock.ps1 -FullGraph <file>"
