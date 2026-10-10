#Requires -Version 5.1
<#
.SYNOPSIS
  Kiwix / ZIM library cloud sync (F: knowledge_bases -> pool:ZIM_RESOURCES).

.DESCRIPTION
  Uses config/zim-upload.json — same day/night bandwidth table as hub-upload.
  Logs to E:\EMPIRE_HUB\99_INDEX\zim_rclone_upload.log and zim_pipeline.log.

.EXAMPLE
  .\scripts\zim-rclone-sync.ps1 -Action status
  .\scripts\zim-rclone-sync.ps1 -Action copy
  .\scripts\zim-rclone-sync.ps1 -Action check
#>
[CmdletBinding()]
param(
    [ValidateSet('status', 'copy', 'check')]
    [string] $Action = 'status',

    [string] $ConfigPath = '',

    [string] $Label = 'zim sync',

    [switch] $DryRun
)

$ErrorActionPreference = 'Stop'
$EmpireRoot = Split-Path -Parent $PSScriptRoot
if (-not $ConfigPath) {
    $ConfigPath = Join-Path $EmpireRoot 'config\zim-upload.json'
}
if (-not (Test-Path $ConfigPath)) {
    throw "Missing config: $ConfigPath"
}

$config = Get-Content -Raw -Path $ConfigPath | ConvertFrom-Json
$source = [string]$config.source_root
$remote = [string]$config.remote
$logDir = [string]$config.log_dir
if (-not $logDir) {
    $logDir = 'E:\EMPIRE_HUB\99_INDEX'
}
$uploadLog = Join-Path $logDir 'zim_rclone_upload.log'
$checkLog = Join-Path $logDir 'zim_rclone_check.log'
$pipelineLog = Join-Path $logDir 'zim_pipeline.log'

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

function Invoke-ZimRclone {
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
if (-not (Test-Path $source)) {
    throw "ZIM source not found: $source"
}

$ex = Get-RcloneExcludeArgs -Patterns @($config.excludes)
$rc = $config.rclone
$bwTable = Get-BwLimitTimetable -Schedule $config.schedule

switch ($Action) {
    'status' {
        Write-Host "Source: $source"
        Write-Host "Remote: $remote"
        Write-Host "Bw:     $bwTable"
        Write-Host ''
        Write-Host 'Local (rclone size):'
        rclone size $source 2>&1
        Write-Host ''
        Write-Host 'Cloud (rclone size):'
        rclone size $remote 2>&1
        return
    }

    'copy' {
        Write-PipelineLog "zim-rclone-sync copy: $Label (bwlimit timetable: $bwTable)"
        $copyArgs = @(
            'copy', $source, $remote
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
        $exit = Invoke-ZimRclone -BaseArgs $copyArgs
        Write-PipelineLog "zim-rclone-sync copy exit $exit"
        if ($exit -ne 0) { exit $exit }
        return
    }

    'check' {
        Write-PipelineLog 'zim-rclone-sync check (size-only one-way)'
        $checkArgs = @(
            'check', $source, $remote
        ) + $ex + @(
            '--size-only'
            '--one-way'
            '--log-file', $checkLog
            '--log-level', 'INFO'
        )
        $exit = Invoke-ZimRclone -BaseArgs $checkArgs
        Write-PipelineLog "zim-rclone-sync check exit $exit"
        if ($exit -ne 0) { exit $exit }
        return
    }

    default {
        throw "Unknown action: $Action"
    }
}
