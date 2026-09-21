$ErrorActionPreference = "Stop"
foreach ($name in @("EMPIRE-AmbientMemoryWatchdog", "EMPIRE-ResearchScavenger")) {
    schtasks.exe /End /TN $name 2>$null | Out-Host
}
Write-Host "Stopped EMPIRE ambient worker tasks where running."