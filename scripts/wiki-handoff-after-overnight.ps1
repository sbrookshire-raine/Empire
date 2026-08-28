<#
.SYNOPSIS
    Wait for overnight wiki ingest to exit, then run maintenance and start the next overnight.

.DESCRIPTION
    Durable handoff for leave-the-machine scenarios:
      1) Poll PID file / process until overnight for -Year is STOPPED
      2) .\scripts\wiki-maintenance.ps1 -Year <Year>  (same process; no nested powershell -File)
      3) Launch start-wiki-ingest-overnight.ps1 detached (priority drain is built into overnight)

    Does NOT kill a live overnight. Safe when overnight is already STOPPED (runs immediately).

.PARAMETER Year
    Snapshot year (default 2017).

.PARAMETER PollSeconds
    How often to re-check overnight PID (default 30).

.PARAMETER FileLimit / MaxSlices / MaxHours / FlushEvery
    Forwarded to start-wiki-ingest-overnight.ps1 (MaxHours default 24 for this handoff).
#>
param(
    [string]$Year = "2017",
    [int]$PollSeconds = 30,
    [int]$FileLimit = 200,
    [int]$MaxSlices = 300,
    [double]$MaxHours = 24.0,
    [int]$FlushEvery = 50
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$LogDir = "I:\EMPIRE_DATA\logs"
$Python = Join-Path $Root "venv\Scripts\python.exe"
$PidFile = Join-Path $LogDir "wiki-ingest-overnight-$Year.pid"
$HandoffPidFile = Join-Path $LogDir "wiki-handoff-after-overnight-$Year.pid"
$MaintScript = Join-Path $PSScriptRoot "wiki-maintenance.ps1"
$OvernightScript = Join-Path $PSScriptRoot "start-wiki-ingest-overnight.ps1"

New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$ts = Get-Date -Format "yyyyMMdd-HHmmss"
$LogFile = Join-Path $LogDir "wiki-handoff-after-overnight-$Year-$ts.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-ddTHH:mm:ss"), $Message
    Write-Host $line
    Add-Content -Path $LogFile -Value $line
}

function Test-OvernightAlive {
    if (Test-Path $Python) {
        $env:PYTHONPATH = $Root
        $code = "from pipeline.wiki_ops_paths import overnight_pid_alive; print('ALIVE' if overnight_pid_alive(r'" + $Year + "') else 'STOPPED')"
        $out = & $Python -c $code
        if ($out -match 'ALIVE') { return $true }
        if ($out -match 'STOPPED') { return $false }
    }
    if (-not (Test-Path $PidFile)) { return $false }
    $existingPid = 0
    try {
        $existingPid = [int]((Get-Content $PidFile -Raw).Trim().Split("`n")[0].Trim())
    }
    catch {
        $existingPid = 0
    }
    if ($existingPid -le 0) { return $false }
    $alive = Get-Process -Id $existingPid -ErrorAction SilentlyContinue
    return [bool]$alive
}

if (-not (Test-Path $MaintScript)) {
    throw "Missing maintenance script: $MaintScript"
}
if (-not (Test-Path $OvernightScript)) {
    throw "Missing overnight script: $OvernightScript"
}

if (Test-Path $HandoffPidFile) {
    $existingHandoff = 0
    try {
        $existingHandoff = [int]((Get-Content $HandoffPidFile -Raw).Trim().Split("`n")[0].Trim())
    }
    catch {
        $existingHandoff = 0
    }
    if ($existingHandoff -gt 0 -and $existingHandoff -ne $PID) {
        $other = Get-Process -Id $existingHandoff -ErrorAction SilentlyContinue
        if ($other) {
            throw "Handoff watcher already running for year=$Year (PID $existingHandoff). Refusing duplicate."
        }
        Write-Log "Stale handoff PID file for $existingHandoff - removing"
        Remove-Item $HandoffPidFile -ErrorAction SilentlyContinue
    }
}
$PID | Set-Content $HandoffPidFile

Write-Log "=== wiki-handoff-after-overnight year=$Year ==="
Write-Log "Log: $LogFile"
Write-Log "Handoff PID: $PID -> $HandoffPidFile"
Write-Log "Next overnight: FileLimit=$FileLimit MaxSlices=$MaxSlices MaxHours=$MaxHours FlushEvery=$FlushEvery"
Write-Log "Sequence: wait overnight STOPPED -> wiki-maintenance.ps1 -> start-wiki-ingest-overnight.ps1 (drain-priorities at window start)"

$handoffExit = 0
try {
    $waited = $false
    while (Test-OvernightAlive) {
        $pidHint = "(no pid file)"
        if (Test-Path $PidFile) {
            $pidHint = "pidfile=" + ((Get-Content $PidFile -Raw).Trim().Split("`n")[0].Trim())
        }
        Write-Log "Overnight still RUNNING ($pidHint) - polling every ${PollSeconds}s (will not kill)"
        $waited = $true
        Start-Sleep -Seconds $PollSeconds
    }

    if ($waited) {
        Write-Log "Overnight exited - beginning maintenance"
    }
    else {
        Write-Log "Overnight already STOPPED - beginning maintenance immediately"
    }

    # Nested powershell.exe so wiki-maintenance.ps1 "exit" does not terminate this handoff.
    # Single ArgumentList string - PS 5.1 Start-Process / array joining mangles -File paths.
    Write-Log "STEP 1/2: wiki-maintenance.ps1 -Year $Year"
    $maintArgs = "-NoProfile -ExecutionPolicy Bypass -File `"$MaintScript`" -Year $Year"
    Write-Log "Invoke: powershell.exe $maintArgs"
    $maintProc = Start-Process -FilePath "powershell.exe" -ArgumentList $maintArgs -WorkingDirectory $Root -Wait -PassThru -NoNewWindow
    $maintExit = $maintProc.ExitCode
    if ($maintExit -ne 0) {
        throw "wiki-maintenance.ps1 failed with exit $maintExit"
    }
    Write-Log "Maintenance complete (exit 0)"

    Write-Log "STEP 2/2: launch-wiki-ingest-overnight.cmd MaxHours=$MaxHours (priority drain at window start)"
    # Prefer the .cmd launcher: correct cmd start TITLE quoting + ensures Ollama parallel.
    $launcher = Join-Path $PSScriptRoot "launch-wiki-ingest-overnight.cmd"
    if (Test-Path $launcher) {
        Write-Log "Invoke: cmd /c `"$launcher`" $Year $FileLimit $MaxSlices $MaxHours $FlushEvery"
        & cmd.exe /c "`"$launcher`" $Year $FileLimit $MaxSlices $MaxHours $FlushEvery"
        if ($LASTEXITCODE -ne 0) {
            throw "launch-wiki-ingest-overnight.cmd failed with exit $LASTEXITCODE"
        }
    }
    else {
        $argLine = "-NoProfile -ExecutionPolicy Bypass -File `"$OvernightScript`" -Year $Year -FileLimit $FileLimit -MaxSlices $MaxSlices -MaxHours $MaxHours -FlushEvery $FlushEvery"
        Write-Log "Launcher missing; Start-Process powershell.exe ArgumentList=$argLine"
        $proc = Start-Process -FilePath "powershell.exe" -ArgumentList $argLine -WorkingDirectory $Root -WindowStyle Minimized -PassThru
        if (-not $proc) {
            throw "Start-Process failed to launch overnight"
        }
        Write-Log "Launched overnight PowerShell PID $($proc.Id)"
    }
    # Verify overnight actually armed (live PID). Earlier handoffs logged "complete"
    # after Start-Process even when the child died on parse/name errors before writing PID.
    $armed = $false
    $deadlineVerify = (Get-Date).AddSeconds(90)
    while ((Get-Date) -lt $deadlineVerify) {
        if (Test-OvernightAlive) {
            $armed = $true
            break
        }
        Start-Sleep -Seconds 3
    }
    if (-not $armed) {
        throw "Overnight failed to arm within 90s (no live PID for year=$Year). Check I:\EMPIRE_DATA\logs\wiki-ingest-overnight-$Year-*.log and wiki-overnight-boot-*.log.err"
    }
    if (Test-Path $PidFile) {
        Write-Log "Overnight PID file: $((Get-Content $PidFile -Raw).Trim())"
    }
    Write-Log "=== handoff complete - next overnight started (armed) ==="
    $handoffExit = 0
}
catch {
    Write-Log "ERROR: $($_.Exception.Message)"
    $handoffExit = 1
}
finally {
    Remove-Item $HandoffPidFile -ErrorAction SilentlyContinue
}

exit $handoffExit
