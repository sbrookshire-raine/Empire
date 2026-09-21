$ErrorActionPreference = "Stop"
schtasks.exe /Run /TN "EMPIRE-AmbientMemoryWatchdog" | Out-Host
if ($LASTEXITCODE -ne 0) { throw "Task EMPIRE-AmbientMemoryWatchdog is not registered. Run install-upgrade-workers.ps1." }