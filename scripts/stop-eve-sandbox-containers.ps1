#Requires -Version 5.1
<#
.SYNOPSIS
  Stop or kill all Eve sandbox Docker containers in one docker CLI call (not one-by-one).

.EXAMPLE
  .\scripts\stop-eve-sandbox-containers.ps1
  .\scripts\stop-eve-sandbox-containers.ps1 -Kill -Remove
#>
param(
    [switch]$Kill,
    [switch]$Remove,
    [switch]$Quiet
)

$ErrorActionPreference = "Continue"

docker info *>$null 2>&1
if ($LASTEXITCODE -ne 0) {
    if (-not $Quiet) {
        Write-Host "  Docker not running - no Eve sandboxes to stop"
    }
    exit 0
}

$ids = @(docker ps -aq --filter "name=eve-sbx" 2>$null)
if ($ids.Count -eq 0) {
    if (-not $Quiet) {
        Write-Host "  Eve sandbox containers: none"
    }
    exit 0
}

$running = @(docker ps -q --filter "name=eve-sbx" 2>$null)
if (-not $Quiet) {
    Write-Host ("  Eve sandbox containers: {0} total ({1} running)" -f $ids.Count, $running.Count)
}

if ($running.Count -gt 0) {
    $verb = if ($Kill) { "kill" } else { "stop" }
    $argList = @($verb) + $running
    & docker @argList 2>$null | Out-Null
    if (-not $Quiet) {
        Write-Host ("  docker {0} issued for {1} running container(s)" -f $verb, $running.Count)
    }
}

if ($Remove) {
    & docker rm -f @ids 2>$null | Out-Null
    if (-not $Quiet) {
        Write-Host ("  docker rm removed {0} container(s)" -f $ids.Count)
    }
}

exit 0
