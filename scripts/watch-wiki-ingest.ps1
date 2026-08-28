<#
.SYNOPSIS
    High-signal health peek for overnight wiki ingest (Postgres era).

.DESCRIPTION
    Prints checkpoint, recent DIAG/Slice OK lines, Postgres row counts, container
    CPU, and ollama ps. Use while overnight runs to spot stalls or embed skips.

    SQL note (Windows PowerShell): always pass psql -c in single quotes so
    identifiers like "DocumentChunk_text" survive. Avoid multi-line -c strings
    with backslash-escaped quotes — that yields:
      ERROR: syntax error at or near "\"
#>
$ErrorActionPreference = "Continue"
$pidFile = "I:\EMPIRE_DATA\logs\wiki-ingest-overnight-2017.pid"
$pidVal = if (Test-Path $pidFile) { (Get-Content $pidFile -Raw).Trim() } else { $null }
$alive = $false
if ($pidVal) { $alive = [bool](Get-Process -Id $pidVal -EA SilentlyContinue) }
Write-Host "overnight pid=$pidVal running=$alive"

$cp = (Get-Content "$env:LOCALAPPDATA\EMPIRE\wiki-checkpoint.json" | ConvertFrom-Json).batches.'2017/batch_00000'
Write-Host "checkpoint next_index=$($cp.next_index) processed=$($cp.processed) status=$($cp.status)"

$latest = Get-ChildItem I:\EMPIRE_DATA\logs\wiki-ingest-overnight-2017-*.log -EA SilentlyContinue |
    Sort-Object LastWriteTime -Descending | Select-Object -First 1
if ($latest) {
    Write-Host "log=$($latest.FullName) age_sec=$([int]((Get-Date)-$latest.LastWriteTime).TotalSeconds)"
    Select-String -Path $latest.FullName -Pattern 'Slice OK|DIAG|ERROR:|Exception caught' |
        Select-Object -Last 8 | ForEach-Object { $_.Line }
}

function Get-PgCount {
    param([string]$Sql)
    # -t -A: tuples only, unaligned — safe for Trim()
    $raw = docker exec empire-cognee-postgres psql -U cognee -d cognee_db -t -A -c $Sql 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "WARN: psql failed: $raw"
        return $null
    }
    return ($raw | Out-String).Trim()
}

try {
    $data = Get-PgCount -Sql "SELECT count(*) FROM data;"
    # Single-quoted -c from PowerShell preserves double-quoted PG identifiers.
    $chunks = Get-PgCount -Sql 'SELECT count(*) FROM "DocumentChunk_text";'
    $docs = Get-PgCount -Sql 'SELECT count(*) FROM "TextDocument_name";'
    Write-Host "data=$data chunks=$chunks docs=$docs"
    docker stats empire-cognee-postgres --no-stream --format "pg CPU={{.CPUPerc}} MEM={{.MemUsage}}"
} catch {
    Write-Host "WARN: postgres stats unavailable: $($_.Exception.Message)"
}
try { ollama ps } catch { Write-Host "ollama ps failed" }
