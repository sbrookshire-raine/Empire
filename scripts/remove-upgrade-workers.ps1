# Remove EMPIRE ambient worker scheduled tasks for the current user.
$ErrorActionPreference = "Stop"
foreach ($name in @("EMPIRE-AmbientMemoryWatchdog", "EMPIRE-ResearchScavenger")) {
    schtasks.exe /Delete /TN $name /F 2>$null | Out-Host
}
Write-Host "Removed EMPIRE ambient worker tasks where present."