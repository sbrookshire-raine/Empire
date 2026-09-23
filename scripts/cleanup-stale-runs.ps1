#Requires -Version 5.1
<#
.SYNOPSIS
  Mark orphaned Eve workflow runs as failed so they do not re-enqueue on startup.

.DESCRIPTION
  Eve's local durable world (agents/empire-task-agent/.eve/.workflow-data/runs)
  can leave runs stuck in "running" after a crash or forced shutdown. On the next
  boot Eve re-enqueues every non-terminal run, flooding the log with
  "[world-local] Re-enqueued N active run(s) on startup" and a burst of
  "TypeError: fetch failed" retries.

  This sweep rewrites any *.json whose status is "running" to "failed", stamps
  errorCode = "PURGED_STALE" and completedAt = now (UTC ISO-8601). It is intended
  to run while Eve is STOPPED — the call site is immediately before launching the
  Eve agent in scripts/start-stack.ps1.

.EXAMPLE
  .\scripts\cleanup-stale-runs.ps1
#>

$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$RunsDir = Join-Path $Root "agents\empire-task-agent\.eve\.workflow-data\runs"

if (-not (Test-Path -LiteralPath $RunsDir)) {
    Write-Host "  Eve runs: directory not found (nothing to sweep): $RunsDir"
    exit 0
}

$files = @(Get-ChildItem -LiteralPath $RunsDir -Filter "*.json" -File -ErrorAction SilentlyContinue)
if ($files.Count -eq 0) {
    Write-Host "  Eve runs: no run files present (clean)."
    exit 0
}

# UTC ISO-8601 with milliseconds, matching the format Eve writes itself (e.g. 2026-08-27T03:57:45.814Z).
$timestamp = [System.DateTime]::UtcNow.ToString("yyyy-MM-ddTHH:mm:ss.fffZ")
# BOM-free UTF-8 so Node's JSON.parse never trips on a leading BOM.
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

$purged = 0
$skipped = 0
$errors = 0

foreach ($file in $files) {
    try {
        $run = [System.IO.File]::ReadAllText($file.FullName) | ConvertFrom-Json
    }
    catch {
        Write-Warning "  Skipped unreadable run file: $($file.Name)"
        $errors++
        continue
    }

    if ($run.status -ne "running") {
        $skipped++
        continue
    }

    # Add-Member -Force sets existing properties and adds missing ones; running
    # runs often lack `completedAt` (and occasionally `errorCode`), and PS 5.1
    # PSCustomObject rejects direct assignment to an absent property.
    $run | Add-Member -MemberType NoteProperty -Name "status" -Value "failed" -Force
    $run | Add-Member -MemberType NoteProperty -Name "errorCode" -Value "PURGED_STALE" -Force
    $run | Add-Member -MemberType NoteProperty -Name "completedAt" -Value $timestamp -Force
    $run | Add-Member -MemberType NoteProperty -Name "updatedAt" -Value $timestamp -Force

    try {
        $json = $run | ConvertTo-Json -Depth 64
        [System.IO.File]::WriteAllText($file.FullName, $json, $utf8NoBom)
        $purged++
    }
    catch {
        Write-Warning "  Failed to write run file: $($file.Name) ($($_.Exception.Message))"
        $errors++
    }
}

Write-Host ("  Eve runs sweep: purged {0} stale run(s), skipped {1}, {2} error(s)." -f $purged, $skipped, $errors)
