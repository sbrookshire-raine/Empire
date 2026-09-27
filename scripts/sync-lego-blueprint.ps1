#Requires -Version 5.1
<#
.SYNOPSIS
  Keep the Desktop copy of the LEGO blueprint current, with rolling backups and a staleness warning.
.DESCRIPTION
  The Desktop manifest (EMPIRE_LEGO_BLUEPRINT.MD) is what gets pasted into external models. If it drifts from
  the canonical `docs/LEGO_BLUEPRINT.md`, every outside proposal is written against a stale inventory — which is
  exactly how three of four bricks in the first round came to describe capabilities we already have.

  Behaviour:
    * identical content  -> no action, no backup churn
    * changed content    -> back up the current Desktop copy, then replace it
    * rolling backups    -> keep the newest -KeepBackups (default 3), delete the rest (oldest first)
    * staleness warning  -> if the structural inventories are newer than the blueprint, say so: the document is
                            probably out of date and needs its §2 sections refreshed before the next handoff

  Wired into pre-commit (see .pre-commit-config.yaml) so it runs when the blueprint or a structural inventory
  changes. Run it by hand any time:  .\scripts\sync-lego-blueprint.ps1
.PARAMETER Check
  Report status and staleness only; never copy or delete.
.PARAMETER Dest
  Desktop target. Defaults to the OneDrive Desktop path used since 2026-09-27.
.PARAMETER KeepBackups
  How many timestamped backups to retain (default 3).
.EXAMPLE
  .\scripts\sync-lego-blueprint.ps1
.EXAMPLE
  .\scripts\sync-lego-blueprint.ps1 -Check
#>
param(
    [switch]$Check,
    [string]$Dest = "$env:USERPROFILE\OneDrive\Desktop\EMPIRE_LEGO_BLUEPRINT.MD",
    [int]$KeepBackups = 3
)

$ErrorActionPreference = 'Continue'
$Root = Split-Path -Parent $PSScriptRoot
$Source = Join-Path $Root 'docs\LEGO_BLUEPRINT.md'

if (-not (Test-Path $Source)) { throw "Canonical blueprint missing: $Source" }

# Structural inventories: when one of these is newer than the blueprint, the inventory likely needs refreshing.
$Inventory = @(
    'config\lego-bricks.json',
    'config\capability-manifest.json',
    'config\library.json',
    'config\foundation.json'
) | ForEach-Object { Join-Path $Root $_ } | Where-Object { Test-Path $_ }

$sourceHash = (Get-FileHash $Source -Algorithm SHA256).Hash
$destHash = if (Test-Path $Dest) { (Get-FileHash $Dest -Algorithm SHA256).Hash } else { '' }
$sourceTime = (Get-Item $Source).LastWriteTime
$stale = @($Inventory | Where-Object { (Get-Item $_).LastWriteTime -gt $sourceTime })

Write-Host "blueprint : $Source"
Write-Host "desktop   : $Dest"

if ($sourceHash -eq $destHash) {
    Write-Host 'status    : already current (identical content, nothing copied)' -ForegroundColor Green
} elseif ($Check) {
    Write-Host 'status    : DIFFERS from the desktop copy (run without -Check to sync)' -ForegroundColor Yellow
} else {
    $dir = Split-Path $Dest -Parent
    if (-not (Test-Path $dir)) { throw "Desktop folder not found: $dir" }
    if (Test-Path $Dest) {
        $stamp = (Get-Item $Dest).LastWriteTime.ToString('yyyyMMdd-HHmmss')
        $backup = Join-Path $dir ("EMPIRE_LEGO_BLUEPRINT.{0}.bak.md" -f $stamp)
        if (Test-Path $backup) { $backup = Join-Path $dir ("EMPIRE_LEGO_BLUEPRINT.{0}-b.bak.md" -f $stamp) }
        Copy-Item $Dest $backup -Force
        Write-Host "backup    : $(Split-Path $backup -Leaf)"
    }
    Copy-Item $Source $Dest -Force
    Write-Host 'status    : desktop copy updated' -ForegroundColor Green

    # Rolling backups: keep the newest N, delete the rest (oldest first).
    $backups = Get-ChildItem $dir -Filter 'EMPIRE_LEGO_BLUEPRINT*.bak.md' -File -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending
    if ($backups.Count -gt $KeepBackups) {
        foreach ($old in $backups[$KeepBackups..($backups.Count - 1)]) {
            Remove-Item $old.FullName -Force -ErrorAction SilentlyContinue
            Write-Host "pruned    : $($old.Name) (keeping newest $KeepBackups)" -ForegroundColor DarkGray
        }
    }
    Write-Host "backups   : $([Math]::Min($backups.Count, $KeepBackups)) kept of $($backups.Count) present"
}

if ($stale.Count) {
    Write-Host ''
    Write-Host 'STALENESS WARNING - these structural files changed after the blueprint:' -ForegroundColor Yellow
    foreach ($f in $stale) {
        Write-Host "  ! $([IO.Path]::GetFileName($f))  ($((Get-Item $f).LastWriteTime))"
    }
    Write-Host '  -> refresh section 2 (what exists) / section 4 (what is open) before the next handoff.' -ForegroundColor Yellow
}

Write-Host 'verification tip: the desktop copy must hash-match the canonical file after a sync.'
exit 0