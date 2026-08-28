# Gracefully stop EMPIRE managed services in reverse dependency order
param(
    [string[]]$Only = @()
)

$ErrorActionPreference = "Stop"
. (Join-Path $PSScriptRoot "lib\service-control.ps1")

$params = @{}
if ($Only.Count -gt 0) { $params.Only = $Only }

Invoke-EmpireRollOut @params
