$ErrorActionPreference = "Stop"
schtasks.exe /Run /TN "EMPIRE-ResearchScavenger" | Out-Host
if ($LASTEXITCODE -ne 0) { throw "Task EMPIRE-ResearchScavenger is not registered. Run install-upgrade-workers.ps1." }