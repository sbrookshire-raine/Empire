#Requires -Version 5.1
<#
.SYNOPSIS
  Start Heptabase desktop (if needed) and wait until Local CLI responds.
.DESCRIPTION
  Run before intake publish or from Start-EMPIRE when you use the disassembly board often.
#>
param(
    [int]$WaitSeconds = 45,
    [switch]$NoLaunch
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Py = Join-Path $Root "venv\Scripts\python.exe"
if (-not (Test-Path $Py)) { throw "venv missing at $Py" }

$argsList = @("-m", "pipeline.heptabase_cli", "ensure-app", "--wait", "$WaitSeconds")
if ($NoLaunch) { $argsList += "--no-launch" }

& $Py @argsList
exit $LASTEXITCODE
