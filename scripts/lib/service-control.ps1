# EMPIRE service start/stop control for roll-in and roll-out
$ErrorActionPreference = "Stop"
. (Join-Path $PSScriptRoot "service-status.ps1")

function Resolve-EmpirePath {
    param([string]$RelativePath)
    $root = Get-EmpireRoot
    if ([System.IO.Path]::IsPathRooted($RelativePath)) {
        return $RelativePath
    }
    return Join-Path $root ($RelativePath -replace '/', '\')
}

function Get-EmpirePortOwnerPid {
    param([int]$Port)
    $conn = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if ($conn) { return [int]$conn.OwningProcess }
    return $null
}

function Resolve-EmpireExecutable {
    param([string]$ExeName)
    if ($ExeName -like "npm*") {
        $resolved = Get-Command npm.cmd -ErrorAction SilentlyContinue
        if ($resolved) { return $resolved.Source }
    }
    if ($ExeName -like "python*") {
        $resolved = Get-Command python -ErrorAction SilentlyContinue
        if ($resolved) { return $resolved.Source }
    }
    return Resolve-EmpirePath $ExeName
}

function Wait-EmpireServiceHealthy {
    param(
        [string]$Name,
        $Service,
        $Defaults
    )
    $retries = [int]$Defaults.healthRetries
    $delay = [int]$Defaults.healthRetrySec
    $timeout = [int]$Defaults.healthTimeoutSec
    $health = @{ ok = $false; detail = "not checked" }

    for ($i = 1; $i -le $retries; $i++) {
        $health = Test-EmpireServiceHealth -Service $Service -TimeoutSec $timeout
        if ($health.ok) { return $health }
        if ($i -lt $retries) { Start-Sleep -Seconds $delay }
    }
    throw "Health check failed for '$Name' after $retries attempts: $($health.detail)"
}

function Start-EmpireManagedService {
    param(
        [string]$Name,
        $Service,
        $Defaults,
        $State
    )

    if (-not $Service.managed) {
        Write-Host "  [$Name] external - verifying health only"
        $null = Wait-EmpireServiceHealthy -Name $Name -Service $Service -Defaults $Defaults
        return
    }

    if (Test-EmpirePortListening -Port ([int]$Service.port)) {
        Write-Host "  [$Name] already listening on port $($Service.port)"
        $null = Wait-EmpireServiceHealthy -Name $Name -Service $Service -Defaults $Defaults
        return
    }

    $start = $Service.start
    if ($start.prepare) {
        $prepare = $start.prepare
        $prepareExe = Resolve-EmpireExecutable ([string]$prepare.exe)
        $prepareCwd = Resolve-EmpirePath ([string]$prepare.cwd)
        $prepareArgs = @($prepare.args | ForEach-Object { [string]$_ })
        Write-Host "  [$Name] preparing runtime..."
        Push-Location $prepareCwd
        try {
            & $prepareExe @prepareArgs
            if ($LASTEXITCODE -ne 0) {
                throw "Runtime preparation failed for '$Name' (exit $LASTEXITCODE)"
            }
        }
        finally {
            Pop-Location
        }
    }
    $exe = Resolve-EmpireExecutable $start.exe
    if (-not (Test-Path $exe) -and $start.exe -notmatch '^(npm|python)') {
        throw "Start executable not found for '$Name': $exe"
    }

    $cwd = Resolve-EmpirePath $start.cwd
    $argList = @($start.args | ForEach-Object { [string]$_ })
    $windowStyle = if ($start.hidden) { "Hidden" } else { "Normal" }

    $envBlock = @{}
    if ($start.env) {
        $start.env.PSObject.Properties | ForEach-Object {
            $value = [string]$_.Value
            $value = $value.Replace("{{EMPIRE_ROOT}}", (Get-EmpireRoot))
            $envBlock[$_.Name] = $value
        }
    }

    Write-Host "  [$Name] starting (port $($Service.port))..."

    if ($envBlock.Count -gt 0) {
        $launcher = Join-Path (Get-EmpireRuntimeDir) ("start-{0}.ps1" -f $Name)
        $envLines = ($envBlock.GetEnumerator() | ForEach-Object {
            '$env:{0} = "{1}"' -f $_.Key, ($_.Value -replace '"', '`"')
        }) -join "`n"
        $argItems = ($argList | ForEach-Object { "'{0}'" -f ($_ -replace "'", "''") }) -join ", "
        $launcherContent = @(
            $envLines
            "Set-Location -LiteralPath '$($cwd -replace "'", "''")'"
            "`$serviceArgs = @($argItems)"
            "& '$($exe -replace "'", "''")' @serviceArgs"
        ) -join "`n"
        Set-Content -Path $launcher -Value $launcherContent -Encoding UTF8
        $proc = Start-Process -FilePath "powershell.exe" `
            -ArgumentList "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $launcher `
            -WorkingDirectory $cwd -WindowStyle $windowStyle -PassThru
    }
    else {
        $proc = Start-Process -FilePath $exe -ArgumentList $argList `
            -WorkingDirectory $cwd -WindowStyle $windowStyle -PassThru
    }

    if (-not $State.services) {
        Add-Member -InputObject $State -NotePropertyName services -NotePropertyValue @{} -Force
    }
    if (-not $State.services.$Name) {
        Add-Member -InputObject $State.services -NotePropertyName $Name -NotePropertyValue @{} -Force
    }
    $State.services.$Name | Add-Member -NotePropertyName pid -NotePropertyValue $proc.Id -Force
    $State.services.$Name | Add-Member -NotePropertyName started -NotePropertyValue ((Get-Date).ToUniversalTime().ToString("o")) -Force
    $State.services.$Name | Add-Member -NotePropertyName port -NotePropertyValue ([int]$Service.port) -Force

    $null = Wait-EmpireServiceHealthy -Name $Name -Service $Service -Defaults $Defaults
    Write-Host "  [$Name] healthy"
}

function Stop-EmpireManagedService {
    param(
        [string]$Name,
        $Service,
        $Defaults,
        $State
    )

    if (-not $Service.managed) {
        Write-Host "  [$Name] external - left running"
        return
    }

    $grace = [int]$Defaults.stopGraceSec
    $forceAfter = [int]$Defaults.stopForceSec
    $targetPid = $null

    $targetPid = Get-EmpirePortOwnerPid -Port ([int]$Service.port)
    if (-not $targetPid -and $State.services -and $State.services.$Name -and $State.services.$Name.pid) {
        $targetPid = [int]$State.services.$Name.pid
    }

    if (-not $targetPid) {
        Write-Host "  [$Name] not running"
        if ($State.services -and $State.services.$Name) {
            $State.services.PSObject.Properties.Remove($Name)
        }
        return
    }

    Write-Host "  [$Name] stopping pid $targetPid (grace ${grace}s)..."
    $proc = Get-Process -Id $targetPid -ErrorAction SilentlyContinue
    if ($proc) {
        $proc.CloseMainWindow() | Out-Null
        Start-Sleep -Seconds 1
        if (-not $proc.HasExited) {
            Stop-Process -Id $targetPid -ErrorAction SilentlyContinue
        }
    }

    $deadline = (Get-Date).AddSeconds($grace)
    while ((Get-Date) -lt $deadline) {
        if (-not (Get-Process -Id $targetPid -ErrorAction SilentlyContinue)) { break }
        if (-not (Test-EmpirePortListening -Port ([int]$Service.port))) { break }
        Start-Sleep -Milliseconds 400
    }

    if (Get-Process -Id $targetPid -ErrorAction SilentlyContinue) {
        Write-Host "  [$Name] forcing stop..."
        Stop-Process -Id $targetPid -Force -ErrorAction SilentlyContinue
        Start-Sleep -Seconds $forceAfter
    }

    if ($State.services -and $State.services.$Name) {
        $State.services.PSObject.Properties.Remove($Name)
    }
    Write-Host "  [$Name] stopped"
}

function Invoke-EmpireRollIn {
    param(
        [string[]]$Only = @(),
        [switch]$SkipExternalCheck
    )

    $config = Get-EmpireServiceConfig
    $state = Read-EmpireServiceState
    $order = @($config.rollInOrder)
    if ($Only.Count -gt 0) {
        $order = @($order | Where-Object { $_ -in $Only })
    }

    Write-Host "EMPIRE roll-in"
    Write-Host "=============="
    Write-EmpireDashboardSnapshot -Phase "rolling-in" -Message "Starting services"

    foreach ($name in $order) {
        $svc = $config.services.$name
        if (-not $svc) { continue }
        if ($SkipExternalCheck -and -not $svc.managed) {
            Write-Host "  [$name] skipped (external)"
            continue
        }
        Start-EmpireManagedService -Name $name -Service $svc -Defaults $config.defaults -State $state
        Write-EmpireServiceState -State $state
    }

    $snap = Write-EmpireDashboardSnapshot -Phase "idle" -Message "Roll-in complete"
    Write-Host ""
    Write-Host "Roll-in complete: $($snap.summary.healthy)/$($snap.summary.total) healthy"
}

function Invoke-EmpireRollOut {
    param(
        [string[]]$Only = @(),
        [switch]$KeepExternal
    )

    $config = Get-EmpireServiceConfig
    $state = Read-EmpireServiceState
    $order = @($config.rollOutOrder)
    if ($Only.Count -gt 0) {
        $order = @($order | Where-Object { $_ -in $Only })
    }

    Write-Host "EMPIRE roll-out"
    Write-Host "==============="
    Write-EmpireDashboardSnapshot -Phase "rolling-out" -Message "Stopping services"

    foreach ($name in $order) {
        $svc = $config.services.$name
        if (-not $svc) { continue }
        if ($KeepExternal -and -not $svc.managed) { continue }
        Stop-EmpireManagedService -Name $name -Service $svc -Defaults $config.defaults -State $state
        Write-EmpireServiceState -State $state
    }

    $snap = Write-EmpireDashboardSnapshot -Phase "idle" -Message "Roll-out complete"
    Write-Host ""
    Write-Host "Roll-out complete: $($snap.summary.healthy)/$($snap.summary.total) still healthy"
}
