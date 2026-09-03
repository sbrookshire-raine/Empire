#Requires -Version 5.1
<#
.SYNOPSIS
    Stop EMPIRE via Stop-EMPIRE.bat (batch-only; avoids AV blocks on PowerShell stop scripts).

.PARAMETER SkipOllama
    Passes /keep-ollama to Stop-EMPIRE.bat.

.PARAMETER SkipDocker
    Passes /keep-docker to Stop-EMPIRE.bat.
#>
param(
    [switch]$SkipOllama,
    [switch]$SkipDocker
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$bat = Join-Path $Root "Stop-EMPIRE.bat"
if (-not (Test-Path -LiteralPath $bat)) {
    throw "Missing launcher: $bat"
}

$batArgs = @()
if ($SkipOllama) { $batArgs += "/keep-ollama" }
if ($SkipDocker) { $batArgs += "/keep-docker" }

$env:STOP_EMPIRE_NO_PAUSE = "1"
try {
    & cmd.exe /c "`"$bat`" $($batArgs -join ' ')"
    exit $LASTEXITCODE
}
finally {
    Remove-Item Env:STOP_EMPIRE_NO_PAUSE -ErrorAction SilentlyContinue
}
