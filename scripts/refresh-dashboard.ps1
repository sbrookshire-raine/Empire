# Refresh dashboard status snapshot (no start/stop)
param(
    [string]$Phase = "idle",
    [string]$Message = "Manual refresh"
)

$ErrorActionPreference = "Stop"
. (Join-Path $PSScriptRoot "lib\service-status.ps1")

$snap = Write-EmpireDashboardSnapshot -Phase $Phase -Message $Message
Write-Host "Dashboard snapshot updated"
Write-Host "  Healthy: $($snap.summary.healthy)/$($snap.summary.total)"
Write-Host "  Runtime: $(Get-EmpireDashboardStatusPath)"
Write-Host "  UI copy: frontend/dashboard-status.json"
Write-Host "  API copy: backend/pocketbase/pb_public/dashboard/status.json"
