#Requires -Version 5.1
<#
.SYNOPSIS
  Run the REA + Disassembly catalog diagnostic battery.
.EXAMPLE
  .\scripts\diagnostic-rea-disassembly.ps1
  .\scripts\diagnostic-rea-disassembly.ps1 -Fast
  .\scripts\diagnostic-rea-disassembly.ps1 -Full
#>
param(
  [switch]$Fast,
  [switch]$Full
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Py = Join-Path $Root "venv\Scripts\python.exe"
if (-not (Test-Path $Py)) { throw "venv missing: $Py" }

$args = @("-m", "pipeline.rea_disassembly_diagnostic")
if ($Fast) { $args += "--fast" }

Write-Host "=== REA / Disassembly diagnostic ===" -ForegroundColor Cyan
& $Py @args
$diagExit = $LASTEXITCODE

if ($Full) {
  Write-Host "`n=== Unit tests (REA/disassembly slice) ===" -ForegroundColor Cyan
  & $Py -m pytest `
    tests/pipeline/test_disassembly_card.py `
    tests/pipeline/test_disassembly_publish.py `
    tests/pipeline/test_heptabase_cli.py `
    tests/pipeline/test_rea_inbox.py `
    tests/pipeline/test_rea_disassembly_diagnostic.py `
    -q --tb=line
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

exit $diagExit
