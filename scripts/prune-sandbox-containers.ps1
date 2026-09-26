# Reap dead Eve sandbox containers and their leftover volumes.
#
# She creates a Docker sandbox per session; nothing removes them, so exited
# "eve-sbx-ses-*" containers accumulate (578 of them measured 2026-09-26, ~1.7 GB).
# remote-build-lighten.ps1 only *stops* them, which is what leaves them exited.
#
# Dry run by default — pass -Apply to actually delete.
[CmdletBinding()]
param([switch]$Apply)

$ErrorActionPreference = "Stop"

$containers = @(docker ps -a --filter "name=eve-sbx" --filter "status=exited" --format "{{.ID}} {{.Names}}")
$volumes = @(docker volume ls --filter "name=eve-sbx" --format "{{.Name}}")

Write-Host "Exited eve-sbx containers: $($containers.Count)"
$containers | Select-Object -First 5 | ForEach-Object { Write-Host "  $_" }
if ($containers.Count -gt 5) { Write-Host "  ... and $($containers.Count - 5) more" }
Write-Host "eve-sbx volumes:          $($volumes.Count)"

if (-not $Apply) {
    Write-Host ""
    Write-Host "Dry run - nothing removed. Re-run with -Apply to delete."
    exit 0
}

foreach ($line in $containers) {
    $id = ($line -split "\s+")[0]
    docker rm $id | Out-Null
}
foreach ($name in $volumes) {
    docker volume rm $name 2>$null | Out-Null
}
Write-Host "Removed $($containers.Count) container(s) and any unused eve-sbx volumes."
docker system df --format "{{.Type}} active={{.Active}} size={{.Size}} reclaimable={{.Reclaimable}}"
