# Register EMPIRE ambient workers at user logon without elevation.
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root "venv\Scripts\python.exe"
$Watchdog = Join-Path $Root "config\eve-capabilities\ambient_memory_watchdog.py"
$Scavenger = Join-Path $Root "config\eve-capabilities\research_scavenger.py"
$User = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name

if (-not (Test-Path $Python)) { throw "Missing venv Python: $Python" }
foreach ($path in @($Watchdog, $Scavenger)) {
    if (-not (Test-Path $path)) { throw "Missing worker: $path" }
}

$principal = New-ScheduledTaskPrincipal -UserId $User -LogonType Interactive -RunLevel Limited
$settings = New-ScheduledTaskSettingsSet -Hidden -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Days 3650)
$trigger = New-ScheduledTaskTrigger -AtLogOn -User $User
$watchdogAction = New-ScheduledTaskAction -Execute $Python -Argument ('"{0}"' -f $Watchdog) -WorkingDirectory $Root
$scavengerAction = New-ScheduledTaskAction -Execute $Python -Argument ('"{0}"' -f $Scavenger) -WorkingDirectory $Root
Register-ScheduledTask -TaskName "EMPIRE-AmbientMemoryWatchdog" -Action $watchdogAction -Trigger $trigger -Settings $settings -Principal $principal -Description "EMPIRE ambient memory watchdog; writes bounded facts to eve_ambient." -Force | Out-Null
Register-ScheduledTask -TaskName "EMPIRE-ResearchScavenger" -Action $scavengerAction -Trigger $trigger -Settings $settings -Principal $principal -Description "EMPIRE local research metadata scavenger; stores arXiv abstracts in catalog.db." -Force | Out-Null
Write-Host "Registered both EMPIRE ambient workers for user logon under $User."