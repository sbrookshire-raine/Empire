# Reap stale ingestion_jobs stuck in "running" (P3: requeue or quarantine — never just "close as failed").
#
# This wrapper is kept because it is the documented command. The decision logic moved to
# scripts/requeue-stale-jobs.py + pipeline/job_schedule.py so the policy is testable in Python and shared, rather
# than living only in this file. The old behaviour — mark every stale row "failed" — is gone on purpose: an
# interrupted job is not a failure, and closing it terminally discarded work a retry could finish.
param(
    [int]$OlderThanMinutes = 10,
    [switch]$Apply
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$pyArgs = @("scripts/requeue-stale-jobs.py", "--older-than-minutes", "$OlderThanMinutes")
if ($Apply) {
    $pyArgs += "--apply"
} else {
    Write-Host "Review mode (no writes). Use -Apply to requeue/quarantine." -ForegroundColor Yellow
}

& "$Root\venv\Scripts\python.exe" @pyArgs
exit $LASTEXITCODE

