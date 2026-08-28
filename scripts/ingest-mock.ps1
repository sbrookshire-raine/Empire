param(
    [Parameter(Position = 0)]
    [string]$File = "mock_data_ingest/github_issue.json",
    [switch]$FullGraph
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root
$env:PYTHONPATH = $Root

$argsList = @("-m", "pipeline.ingest_local", "--file", $File)
if ($FullGraph) { $argsList += "--full-graph" }

if ($FullGraph) {
    Write-Host "Ingesting $File with FULL graph extraction (~2 min)..."
} else {
    Write-Host "Ingesting $File in FAST mode (seconds)..."
}

& "$Root\venv\Scripts\python.exe" @argsList
