# Start PocketBase in the background (detached) — uses shared service orchestrator
$ErrorActionPreference = "Stop"
. (Join-Path $PSScriptRoot "lib\service-control.ps1")
Invoke-EmpireRollIn -Only @("pocketbase")
