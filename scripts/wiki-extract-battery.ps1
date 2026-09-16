# Wiki extract regression battery (CLI; optional -Live for Eve).
param(
    [switch]$Live
)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not $Root) { $Root = "C:\EMPIRE" }
$py = Join-Path $Root "venv\Scripts\python.exe"
if (-not (Test-Path $py)) {
    Write-Error "Missing venv python at $py"
}
$env:PYTHONPATH = $Root
$args = @((Join-Path $Root "scripts\wiki_extract_battery.py"))
if ($Live) { $args += "--live" }
& $py @args
exit $LASTEXITCODE
