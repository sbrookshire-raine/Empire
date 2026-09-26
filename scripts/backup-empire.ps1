#Requires -Version 5.1
<#
.SYNOPSIS
  Back up the irreplaceable data with restic, and prove the backup by restoring from it.
.DESCRIPTION
  We hold a MANIFEST of the vault (14,652 files / 2,814.8 MB / 0 errors), not a copy of it
  (docs/LENS_A_LANDSCAPE.md section 6). This closes that gap.

  Target chosen by evidence, not assumption: `Get-Volume` shows I: = "T7 Shield", 3725.7 GB,
  2327.6 GB free - a separate physical device from C: = "Windows-SSD". Note I: is exFAT (no
  journaling), which is why -VerifyRestore exists rather than trust.

  Password: %LOCALAPPDATA%\EMPIRE\restic-pass.txt - outside the repo and never committed.
  Losing it means losing every backup, so it is the system's real single point of failure and
  should be escrowed somewhere physical.

  A backup that has never been restored from is not a backup, so the acceptance run is:
      .\scripts\backup-empire.ps1 -VerifyRestore
.PARAMETER VerifyRestore
  After backing up, restore the newest snapshot to a scratch folder and compare file counts.
.PARAMETER Source
  What to protect. Default is the workbench vault (the only copy of it anywhere).
.EXAMPLE
  .\scripts\backup-empire.ps1
.EXAMPLE
  .\scripts\backup-empire.ps1 -VerifyRestore
#>
param(
    [switch]$VerifyRestore,
    [string]$Source = 'C:\Empire_Workbench',
    [string]$Repo = 'I:\EMPIRE_BACKUP\restic',
    [string]$Scratch = 'I:\EMPIRE_BACKUP\restore-test'
)

$ErrorActionPreference = 'Stop'

function Resolve-Restic {
    $cmd = Get-Command restic -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    $base = Join-Path $env:LOCALAPPDATA 'Microsoft\WinGet\Packages'
    if (Test-Path $base) {
        $hit = Get-ChildItem $base -Recurse -Filter 'restic*.exe' -ErrorAction SilentlyContinue |
            Select-Object -First 1
        if ($hit) { return $hit.FullName }
    }
    throw 'restic not found: winget install restic.restic'
}

$passFile = Join-Path $env:LOCALAPPDATA 'EMPIRE\restic-pass.txt'
if (-not (Test-Path $passFile)) { throw "Missing restic password file: $passFile" }
if (-not (Test-Path 'I:\')) { throw 'I: (T7) not mounted - connect the external drive before backing up.' }
if (-not (Test-Path $Repo)) { throw "No restic repository at $Repo - run: restic -r $Repo init" }

$env:RESTIC_PASSWORD_FILE = $passFile
$restic = Resolve-Restic

Write-Host "Backing up $Source -> $Repo"
& $restic -r $Repo backup $Source --exclude-caches --tag empire-vault
if ($LASTEXITCODE -ne 0) { throw "restic backup failed ($LASTEXITCODE)" }

Write-Host ''
Write-Host 'Snapshots:'
& $restic -r $Repo snapshots --compact

if ($VerifyRestore) {
    Write-Host ''
    Write-Host '=== restore test: a backup that has never been restored from is not a backup ==='
    if (Test-Path $Scratch) { Remove-Item $Scratch -Recurse -Force }
    New-Item -ItemType Directory -Force -Path $Scratch | Out-Null
    & $restic -r $Repo restore latest --target $Scratch --tag empire-vault
    if ($LASTEXITCODE -ne 0) { throw "restic restore failed ($LASTEXITCODE)" }

    $sourceCount = @(Get-ChildItem $Source -Recurse -File -ErrorAction SilentlyContinue).Count
    $restoredCount = @(Get-ChildItem $Scratch -Recurse -File -ErrorAction SilentlyContinue).Count
    Write-Host "  source files:   $sourceCount"
    Write-Host "  restored files: $restoredCount"
    if ($restoredCount -lt $sourceCount) {
        Write-Host '  MISMATCH - the restore is incomplete. Investigate before trusting this backup.' -ForegroundColor Red
        exit 1
    }
    Write-Host '  restore verified (file counts match or exceed)' -ForegroundColor Green
    Write-Host "  scratch copy left at $Scratch for spot checking; delete it when satisfied."
}

Write-Host ''
Write-Host 'backup-empire: done' -ForegroundColor Green
