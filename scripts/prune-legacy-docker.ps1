#Requires -Version 5.1
<#
.SYNOPSIS
  Audit Docker and remove non-EMPIRE legacy containers/images (Dify v2-archive, old Weaviate, Eve sandbox templates).

.DESCRIPTION
  KEEP (EMPIRE operational):
    - empire-cognee-postgres  (+ volume empire_empire_cognee_pgdata — never deleted here)
    - empire-weaviate-heist-2017  (Wiki Local)
    - empire-speaches  (voice on demand)
    - empire-searxng  (Web Research / searxng_search)

  REMOVE when -Apply:
    - Exited containers whose names are NOT in the keep list (v2-archive-*, old weaviate stacks, etc.)
    - Unused eve-sandbox-template / ghcr.io/vercel/eve images (legacy Eve Docker sandbox)

  Legacy volumes (n8n, agent-zero, ai_factory) are listed in the audit only unless -RemoveLegacyVolumes.

.EXAMPLE
  .\scripts\prune-legacy-docker.ps1
  .\scripts\prune-legacy-docker.ps1 -Apply
  .\scripts\prune-legacy-docker.ps1 -Apply -RemoveLegacyVolumes
#>
param(
    [switch]$Apply,
    [switch]$RemoveLegacyVolumes
)

$ErrorActionPreference = "Continue"

$KeepContainers = @(
    "empire-cognee-postgres"
    "empire-weaviate-heist-2017"
    "empire-speaches"
    "empire-searxng"
)

$KeepVolumePatterns = @(
    "empire_empire_cognee_pgdata"
    "empire-speaches"
    "empire_cognee"
)

$LegacyVolumePatterns = @(
    "n8n"
    "agent-zero"
    "ai_factory"
    "open-webui"
    "docker_postgres_data"
    "docker_plugin_daemon"
    "v2-markdown-pipeline"
    "v2_dify"
    "cursor_hol_weaviate"
)

docker info *>$null 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Warning "Docker is not running."
    exit 1
}

Write-Host "EMPIRE Docker audit"
Write-Host "==================="
Write-Host ""
Write-Host "KEEP containers: $($KeepContainers -join ', ')"
Write-Host ""

$all = @(docker ps -a --format "{{.Names}}|{{.Status}}|{{.ID}}")
$toRemove = @()
foreach ($line in $all) {
    $parts = $line -split "\|", 3
    if ($parts.Count -lt 3) { continue }
    $name = $parts[0]
    $status = $parts[1]
    $id = $parts[2]
    if ($KeepContainers -contains $name) {
        Write-Host ("  KEEP  {0,-40} {1}" -f $name, $status)
        continue
    }
    Write-Host ("  LEGACY {0,-39} {1}" -f $name, $status)
    if ($status -match "Exited|Created|Dead") {
        $toRemove += $id
    }
    elseif ($status -match "Up") {
        Write-Host '         ^ still RUNNING - stop manually if you intend to remove it'
    }
}

Write-Host ""
$tplImages = @(docker images "eve-sandbox-template" -q 2>$null)
$eveBase = @(docker images "ghcr.io/vercel/eve" -q 2>$null)
Write-Host ("Legacy Eve sandbox template images: {0}" -f $tplImages.Count)
Write-Host ("ghcr.io/vercel/eve images:          {0}" -f $eveBase.Count)

Write-Host ""
Write-Host "Named volumes (sample):"
docker volume ls --format "  {{.Name}}" | Select-Object -First 50

$legacyVol = @()
foreach ($v in (docker volume ls -q 2>$null)) {
    $vn = [string]$v
    foreach ($pat in $LegacyVolumePatterns) {
        if ($vn -match [regex]::Escape($pat) -or $vn -like "*$pat*") {
            $legacyVol += $vn
            break
        }
    }
}
if ($legacyVol.Count -gt 0) {
    Write-Host ""
    Write-Host "Legacy project volumes (not removed unless -RemoveLegacyVolumes):"
    $legacyVol | ForEach-Object { Write-Host "  $_" }
}

Write-Host ""
docker system df

if (-not $Apply) {
    Write-Host ""
    Write-Host "Dry run. Re-run with -Apply to remove exited legacy containers + sandbox template images."
    Write-Host "Add -RemoveLegacyVolumes to delete listed n8n/agent-zero/ai_factory volumes (data loss)."
    exit 0
}

Write-Host ""
Write-Host "Applying..."

if ($toRemove.Count -gt 0) {
    docker rm -f @toRemove 2>$null | Out-Null
    Write-Host ("Removed {0} exited legacy container(s)." -f $toRemove.Count)
}

& (Join-Path $PSScriptRoot "stop-eve-sandbox-containers.ps1") -Kill -Remove -Quiet | Out-Null

foreach ($img in ($tplImages + $eveBase)) {
    if ($img) {
        docker rmi -f $img 2>$null | Out-Null
    }
}

Write-Host "Removed Eve sandbox template / base images where unused."

if ($RemoveLegacyVolumes) {
    foreach ($vn in $legacyVol) {
        $skip = $false
        foreach ($keep in $KeepVolumePatterns) {
            if ($vn -like "*$keep*") { $skip = $true; break }
        }
        if (-not $skip) {
            docker volume rm $vn 2>$null | Out-Null
            Write-Host "  volume rm $vn"
        }
    }
}

Write-Host ""
Write-Host "After cleanup:"
docker ps -a --format 'table {{.Names}}\t{{.Status}}'
Write-Host ""
docker system df
