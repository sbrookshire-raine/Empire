$ErrorActionPreference = "SilentlyContinue"
foreach ($name in @("EMPIRE-AmbientMemoryWatchdog", "EMPIRE-ResearchScavenger")) {
    schtasks.exe /Query /TN $name /FO LIST /V | Select-String "TaskName:|Status:|Task To Run:|Run As User:|Run Level:"
    Write-Host ""
}