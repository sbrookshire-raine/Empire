<#
.SYNOPSIS
  Prune old Eve workflow-data chunks. Dry run unless -Apply.

.DESCRIPTION
  agents/empire-task-agent/.eve/.workflow-data measured 168,805 files / 0.85 GB on 2026-09-24
  (122,014 stream chunks, 21,154 event files, 12,478 hook files). The startup sweep stops dead runs
  being re-enqueued; it does not stop growth (queue row E-04).

  Removes *chunk* files older than -OlderThanDays under streams/, events/, steps/ and hooks/.
  Never touches runs/ (the index the Workbench reads) or locks/.

  Dry run by default: it prints what it would free and changes nothing. Pass -Apply to delete.
  Refuses to run while Eve is listening on port 2000 unless -Force (a live run may still be writing).

.EXAMPLE
  .\scripts\prune-workflow-data.ps1
  .\scripts\prune-workflow-data.ps1 -OlderThanDays 14 -Apply
#>
param(
  [int]$OlderThanDays = 7,
  [switch]$Apply,
  [switch]$Force
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$DataRoot = Join-Path $Root "agents\empire-task-agent\.eve\.workflow-data"

if (-not (Test-Path $DataRoot)) {
  Write-Host "No workflow-data at $DataRoot - nothing to prune."
  exit 0
}

$listening = Get-NetTCPConnection -LocalPort 2000 -State Listen -ErrorAction SilentlyContinue
if ($listening -and -not $Force) {
  Write-Warning "Eve is listening on 127.0.0.1:2000. Stop her, or pass -Force to prune anyway."
  exit 1
}

if ($OlderThanDays -lt 1) {
  Write-Warning "-OlderThanDays must be at least 1 (use a bigger window, not zero)."
  exit 1
}

$cutoff = (Get-Date).AddDays(-1 * $OlderThanDays)
$mode = if ($Apply) { "APPLY" } else { "DRY RUN" }
Write-Host "prune-workflow-data [$mode]  root=$DataRoot  older-than=${OlderThanDays}d (before $($cutoff.ToString('yyyy-MM-dd HH:mm')))"

$totalFiles = 0
$totalBytes = 0
foreach ($sub in @("streams", "events", "steps", "hooks")) {
  $dir = Join-Path $DataRoot $sub
  if (-not (Test-Path $dir)) { continue }
  $old = Get-ChildItem $dir -Recurse -File -ErrorAction SilentlyContinue |
    Where-Object { $_.LastWriteTime -lt $cutoff }
  $bytes = ($old | Measure-Object -Property Length -Sum).Sum
  if (-not $bytes) { $bytes = 0 }
  Write-Host ("  {0,-8} {1,8} files  {2,9:N1} MB" -f $sub, $old.Count, ($bytes / 1MB))
  $totalFiles += $old.Count
  $totalBytes += $bytes
  if ($Apply -and $old.Count -gt 0) {
    $old | Remove-Item -Force -ErrorAction SilentlyContinue
  }
}

Write-Host ("total: {0} files, {1:N1} MB {2}" -f $totalFiles, ($totalBytes / 1MB), $(if ($Apply) { "deleted" } else { "would be freed - rerun with -Apply" }))
if (-not $Apply) {
  Write-Host "Kept: runs/ (Workbench index), locks/."
}
