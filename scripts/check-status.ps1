# Quick status check for PocketBase + frontend + dashboard snapshot
$ErrorActionPreference = "Continue"
. (Join-Path $PSScriptRoot "lib\service-status.ps1")

Write-Host "EMPIRE service status"
Write-Host "====================="

$snap = Write-EmpireDashboardSnapshot -Phase "idle" -Message "check-status"

foreach ($svc in $snap.services) {
    $flag = if ($svc.healthy) { "[OK]  " } else { "[DOWN]" }
    $managed = if ($svc.managed) { "managed" } else { "external" }
    Write-Host "$flag $($svc.label.PadRight(14)) :$($svc.port)  ($managed) - $($svc.healthDetail)"
}

Write-Host ""
Write-Host "Summary: $($snap.summary.healthy)/$($snap.summary.total) healthy"
Write-Host ""
Write-Host "Useful URLs:"
Write-Host "  Dashboard:        http://127.0.0.1:8080/dashboard.html"
Write-Host "  PocketBase home:  http://127.0.0.1:8090/"
Write-Host "  PocketBase admin: http://127.0.0.1:8090/_/"
Write-Host "  Tasks app:        http://127.0.0.1:8080/"
Write-Host ""
Write-Host "Orchestration:"
Write-Host "  Roll in:   .\scripts\roll-in.ps1"
Write-Host "  Roll out:  .\scripts\roll-out.ps1"
Write-Host "  Refresh:   .\scripts\refresh-dashboard.ps1"
Write-Host "  Verify:    .\scripts\verify-stack.ps1   # integration checks (communication paths)"
Write-Host "  Handoff:   docs/OPERATIONAL_HANDOFF.md"
