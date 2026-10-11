# Reap dead Eve sandbox containers and their leftover volumes.
#
# She creates a Docker sandbox per session when the runtime uses the Docker backend;
# EMPIRE now pins just-bash (no Docker). Legacy eve-sbx containers may still exist.
# remote-build-lighten.ps1 only *stops* them, which is what leaves them exited.
#
# Dry run by default — pass -Apply to actually delete.
[CmdletBinding()]
param(
    [switch]$Apply,
    [switch]$KillRunning
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$StopScript = Join-Path $PSScriptRoot "stop-eve-sandbox-containers.ps1"

$running = @(docker ps -q --filter "name=eve-sbx" 2>$null)
$containers = @(docker ps -a --filter "name=eve-sbx" --filter "status=exited" --format "{{.ID}} {{.Names}}")
$volumes = @(docker volume ls --filter "name=eve-sbx" --format "{{.Name}}")

Write-Host "Running eve-sbx containers: $($running.Count)"
Write-Host "Exited eve-sbx containers:  $($containers.Count)"
$containers | Select-Object -First 5 | ForEach-Object { Write-Host "  $_" }
if ($containers.Count -gt 5) { Write-Host "  ... and $($containers.Count - 5) more" }
Write-Host "eve-sbx volumes:          $($volumes.Count)"

if (-not $Apply) {
    Write-Host ""
    Write-Host "Dry run - nothing removed. Re-run with -Apply to stop running + delete exited."
    Write-Host "Fast stop only: .\scripts\stop-eve-sandbox-containers.ps1 -Kill -Remove"
    exit 0
}

if ($running.Count -gt 0) {
    & $StopScript -Kill -Remove -Quiet
}

foreach ($line in $containers) {
    $id = ($line -split "\s+")[0]
    if ($id) {
        docker rm -f $id 2>$null | Out-Null
    }
}
foreach ($name in $volumes) {
    docker volume rm $name 2>$null | Out-Null
}
Write-Host "Removed exited containers and eve-sbx volumes (running were killed first when present)."
docker system df --format "{{.Type}} active={{.Active}} size={{.Size}} reclaimable={{.Reclaimable}}"
