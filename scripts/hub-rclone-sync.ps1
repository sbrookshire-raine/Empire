#Requires -Version 5.1
<#
.SYNOPSIS
  EMPIRE_HUB cloud sync — optimized for consolidation uploads (E: -> pool:EMPIRE_HUB).

.DESCRIPTION
  Uses config/hub-upload.json for rclone flags and a time-of-day bandwidth table:
  - Midnight–2:00 PM local: maximum throughput (default bwlimit "off")
  - 2:00 PM–midnight: low cap (default 3M) for personal / upstairs use

  Not incremental backup yet — full hub tree copy with excludes (no local_only secrets).

.EXAMPLE
  .\scripts\hub-rclone-sync.ps1 -Action status
  .\scripts\hub-rclone-sync.ps1 -Action copy
  .\scripts\hub-rclone-sync.ps1 -Action check
#>
[CmdletBinding()]
param(
    [ValidateSet('status', 'copy', 'check')]
    [string] $Action = 'status',

    [string] $ConfigPath = '',

    [string] $Label = 'hub sync',

    [switch] $DryRun
)

$ErrorActionPreference = 'Stop'
$EmpireRoot = Split-Path -Parent $PSScriptRoot
if (-not $ConfigPath) {
    $ConfigPath = Join-Path $EmpireRoot 'config\hub-upload.json'
}
if (-not (Test-Path $ConfigPath)) {
    throw "Missing config: $ConfigPath"
}

$config = Get-Content -Raw -Path $ConfigPath | ConvertFrom-Json
$hub = [string]$config.hub_root
$remote = [string]$config.remote
$logDir = Join-Path $hub '99_INDEX'
$uploadLog = Join-Path $logDir 'rclone_upload.log'
$checkLog = Join-Path $logDir 'rclone_check.log'
$pipelineLog = Join-Path $logDir 'pipeline.log'

function Write-PipelineLog {
    param([string]$Message)
    $line = "$(Get-Date -Format s) $Message"
    if (Test-Path $logDir) {
        Add-Content -Path $pipelineLog -Value $line
    }
    Write-Host $line
}

function Get-BwLimitTimetable {
    param($Schedule)
    $night = [string]$Schedule.night_start
    $nightBw = [string]$Schedule.night_bwlimit
    $day = [string]$Schedule.day_start
    $dayBw = [string]$Schedule.day_bwlimit
    if (-not $nightBw) { $nightBw = 'off' }
    if (-not $dayBw) { $dayBw = '3M' }
    return "$night,$nightBw $day,$dayBw"
}

function Get-RcloneExcludeArgs {
    param([string[]]$Patterns)
    $args = @()
    foreach ($p in $Patterns) {
        $args += '--exclude'
        $args += $p
    }
    return $args
}

function Invoke-HubRclone {
    param(
        [string[]]$BaseArgs
    )
    if ($DryRun) {
        Write-Host ('dry-run: rclone ' + ($BaseArgs -join ' '))
        return 0
    }
    & rclone @BaseArgs
    return $LASTEXITCODE
}

if (-not (Get-Command rclone -ErrorAction SilentlyContinue)) {
    throw 'rclone not found on PATH'
}
if (-not (Test-Path $hub)) {
    throw "Hub root not found: $hub"
}

$ex = Get-RcloneExcludeArgs -Patterns @($config.excludes)
$rc = $config.rclone
$bwTable = Get-BwLimitTimetable -Schedule $config.schedule

switch ($Action) {
    'status' {
        Write-Host "Hub:    $hub"
        Write-Host "Remote: $remote"
        Write-Host "Bw:     $bwTable"
        $localGiB = 0.0
        Get-ChildItem -Path $hub -Directory -ErrorAction SilentlyContinue | ForEach-Object {
            $sum = (Get-ChildItem -Path $_.FullName -Recurse -File -ErrorAction SilentlyContinue |
                Measure-Object -Property Length -Sum).Sum
            if ($null -ne $sum) {
                $g = [math]::Round($sum / 1GB, 2)
                $localGiB += $g
                Write-Host ("  local {0,-20} {1,8} GiB" -f $_.Name, $g)
            }
        }
        Write-Host ("  local total (top folders)     {0,8} GiB" -f [math]::Round($localGiB, 2))
        Write-Host ''
        Write-Host 'Cloud (rclone size):'
        rclone size $remote 2>&1
        return
    }

    'copy' {
        Write-PipelineLog "hub-rclone-sync copy: $Label (bwlimit timetable: $bwTable)"
        $copyArgs = @(
            'copy', $hub, $remote
        ) + $ex + @(
            '--transfers', [string]$rc.transfers
            '--checkers', [string]$rc.checkers
            '--drive-chunk-size', [string]$rc.drive_chunk_size
            '--buffer-size', [string]$rc.buffer_size
            '--multi-thread-cutoff', [string]$rc.multi_thread_cutoff
            '--multi-thread-streams', [string]$rc.multi_thread_streams
            '--bwlimit', $bwTable
            '--retries', [string]$rc.retries
            '--low-level-retries', [string]$rc.low_level_retries
            '--stats', [string]$rc.stats_interval
            '--stats-one-line'
            '--log-file', $uploadLog
            '--log-level', 'INFO'
        )
        if ($config.google.stop_on_upload_limit) {
            $copyArgs += '--drive-stop-on-upload-limit'
        }
        $exit = Invoke-HubRclone -BaseArgs $copyArgs
        Write-PipelineLog "hub-rclone-sync copy exit $exit"
        if ($exit -ne 0) { exit $exit }
        return
    }

    'check' {
        Write-PipelineLog 'hub-rclone-sync check (size-only one-way)'
        $checkArgs = @(
            'check', $hub, $remote
        ) + $ex + @(
            '--size-only'
            '--one-way'
            '--log-file', $checkLog
            '--log-level', 'INFO'
        )
        $exit = Invoke-HubRclone -BaseArgs $checkArgs
        Write-PipelineLog "hub-rclone-sync check exit $exit"
        if ($exit -ne 0) { exit $exit }
        return
    }

    default {
        throw "Unknown action: $Action"
    }
}
