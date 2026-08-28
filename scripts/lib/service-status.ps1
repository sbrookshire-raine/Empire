# EMPIRE service status and dashboard snapshots (read-only)
$ErrorActionPreference = "Stop"

function Get-EmpireRoot {
    if ($script:EmpireRoot) { return $script:EmpireRoot }
    $script:EmpireRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
    return $script:EmpireRoot
}

function Get-EmpireRuntimeDir {
    $dir = Join-Path $env:LOCALAPPDATA "EMPIRE"
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Force -Path $dir | Out-Null
    }
    return $dir
}

function Get-EmpireServiceConfig {
    $path = Join-Path (Get-EmpireRoot) "config\services.json"
    if (-not (Test-Path $path)) {
        throw "Service config not found: $path"
    }
    return Get-Content $path -Raw | ConvertFrom-Json
}

function Get-EmpireServiceStatePath {
    Join-Path (Get-EmpireRuntimeDir) "services.state.json"
}

function Get-EmpireDashboardStatusPath {
    Join-Path (Get-EmpireRuntimeDir) "dashboard-status.json"
}

function Read-EmpireServiceState {
    $path = Get-EmpireServiceStatePath
    if (-not (Test-Path $path)) {
        return [pscustomobject]@{
            version  = 1
            updated  = $null
            services = @{}
        }
    }
    return Get-Content $path -Raw | ConvertFrom-Json
}

function Test-EmpirePortListening {
    param([int]$Port)
    $conn = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue |
        Select-Object -First 1
    return [bool]$conn
}

function Test-EmpireServiceHealth {
    param(
        $Service,
        [int]$TimeoutSec = 8
    )
    if (-not $Service.healthUrl) {
        return @{ ok = $false; detail = "no healthUrl configured" }
    }
    try {
        $response = Invoke-WebRequest -Uri $Service.healthUrl -UseBasicParsing -TimeoutSec $TimeoutSec
        return @{
            ok         = ($response.StatusCode -ge 200 -and $response.StatusCode -lt 400)
            detail     = "HTTP $($response.StatusCode)"
            statusCode = $response.StatusCode
        }
    }
    catch {
        return @{ ok = $false; detail = $_.Exception.Message }
    }
}

function Get-EmpireServiceStatuses {
    $config = Get-EmpireServiceConfig
    $state = Read-EmpireServiceState
    $items = @()

    foreach ($prop in $config.services.PSObject.Properties) {
        $id = $prop.Name
        $svc = $prop.Value
        $listening = Test-EmpirePortListening -Port ([int]$svc.port)
        $health = Test-EmpireServiceHealth -Service $svc -TimeoutSec 5
        $trackedPid = $null
        if ($state.services -and $state.services.$id -and $state.services.$id.pid) {
            $trackedPid = [int]$state.services.$id.pid
        }

        $items += [pscustomobject]@{
            id           = $id
            label        = $svc.label
            description  = $svc.description
            port         = [int]$svc.port
            managed      = [bool]$svc.managed
            dashboardControl = [bool]($svc.dashboardControl -eq $true)
            startScript  = if ($svc.startScript) { [string]$svc.startScript } else { $null }
            startHint    = if ($svc.startHint) { [string]$svc.startHint } else { $null }
            listening    = $listening
            healthy      = [bool]$health.ok
            healthDetail = $health.detail
            dashboardUrl = $svc.dashboardUrl
            pid          = $trackedPid
        }
    }

    return $items
}

function Write-EmpireDashboardSnapshot {
    param(
        [string]$Phase = "idle",
        [string]$Message = ""
    )

    $config = Get-EmpireServiceConfig
    $services = Get-EmpireServiceStatuses
    $healthyCount = @($services | Where-Object { $_.healthy }).Count
    $total = $services.Count

    $snapshot = [pscustomobject]@{
        version      = 1
        updated      = (Get-Date).ToUniversalTime().ToString("o")
        phase        = $Phase
        message      = $Message
        summary      = [pscustomobject]@{
            healthy    = $healthyCount
            total      = $total
            allHealthy = ($healthyCount -eq $total)
        }
        rollInOrder  = @($config.rollInOrder)
        rollOutOrder = @($config.rollOutOrder)
        services     = $services
        commands     = [pscustomobject]@{
            rollIn  = ".\scripts\roll-in.ps1"
            rollOut = ".\scripts\roll-out.ps1"
            refresh = ".\scripts\refresh-dashboard.ps1"
            status  = ".\scripts\check-status.ps1"
        }
    }

    $runtimePath = Get-EmpireDashboardStatusPath
    $snapshot | ConvertTo-Json -Depth 8 | Set-Content -Path $runtimePath -Encoding UTF8

    $frontendCopy = Join-Path (Get-EmpireRoot) "frontend\dashboard-status.json"
    $snapshot | ConvertTo-Json -Depth 8 | Set-Content -Path $frontendCopy -Encoding UTF8

    $pbCopyDir = Join-Path (Get-EmpireRoot) "backend\pocketbase\pb_public\dashboard"
    if (-not (Test-Path $pbCopyDir)) {
        New-Item -ItemType Directory -Force -Path $pbCopyDir | Out-Null
    }
    $pbCopy = Join-Path $pbCopyDir "status.json"
    $snapshot | ConvertTo-Json -Depth 8 | Set-Content -Path $pbCopy -Encoding UTF8

    return $snapshot
}

function Write-EmpireServiceState {
    param($State)
    $State.updated = (Get-Date).ToUniversalTime().ToString("o")
    $path = Get-EmpireServiceStatePath
    $State | ConvertTo-Json -Depth 8 | Set-Content -Path $path -Encoding UTF8
}
