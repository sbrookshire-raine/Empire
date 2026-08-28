# Mark stale ingestion_jobs stuck in "running" as failed.
param(
    [int]$OlderThanMinutes = 10
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$pbUrl = if ($env:POCKETBASE_URL) { $env:POCKETBASE_URL } else { "http://127.0.0.1:8090" }
$cutoff = (Get-Date).ToUniversalTime().AddMinutes(-1 * $OlderThanMinutes).ToString("yyyy-MM-dd HH:mm:ss.000Z")

Write-Host "Closing ingestion_jobs still 'running' since before $cutoff (UTC)"

$filter = [uri]::EscapeDataString("status='running' && started_at<'$cutoff'")
$listUrl = "$pbUrl/api/collections/ingestion_jobs/records?filter=$filter&perPage=100"
$items = (Invoke-RestMethod -Uri $listUrl).items

if (-not $items -or $items.Count -eq 0) {
    Write-Host "No stale running jobs found."
    exit 0
}

foreach ($job in $items) {
    $body = @{
        status = "failed"
        error = "Auto-closed: job exceeded ${OlderThanMinutes}m running (process likely interrupted)."
        finished_at = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss.000Z")
    } | ConvertTo-Json

    Invoke-RestMethod -Method Patch -Uri "$pbUrl/api/collections/ingestion_jobs/records/$($job.id)" `
        -ContentType "application/json" -Body $body | Out-Null

    $name = [System.IO.Path]::GetFileName($job.source_file)
    Write-Host "  closed: $name ($($job.id))"
}

Write-Host "Done. Closed $($items.Count) stale job(s)."
