<#
.SYNOPSIS
    Post-ingest maintenance: gate overnight PID -> ANALYZE/VACUUM -> titles export -> priority resolve.

.DESCRIPTION
    Runs until done (no hard 1h cap). Soft-warns if wall clock exceeds 2h.
    Refuses to start while overnight PID is alive (no VACUUM during ingest).
    Never runs VACUUM FULL unless -AllowVacuumFull.

.PARAMETER Year
    Snapshot year (default 2017).

.PARAMETER SkipAnalyze / SkipVacuum / SkipTitles / SkipPriorityResolve
    Optional step skips.

.PARAMETER SeedCodex
    Append pending Master Codex subjects (planning only).

.PARAMETER AllowVacuumFull
    Explicit opt-in for VACUUM FULL (not used by default).
#>
param(
    [string]$Year = "2017",
    [switch]$SkipAnalyze,
    [switch]$SkipVacuum,
    [switch]$SkipTitles,
    [switch]$SkipPriorityResolve,
    [switch]$SeedCodex,
    [switch]$AllowVacuumFull
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root "venv\Scripts\python.exe"
$LogDir = "I:\EMPIRE_DATA\logs"
$env:PYTHONPATH = $Root

New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$ts = Get-Date -Format "yyyyMMdd-HHmmss"
$LogFile = Join-Path $LogDir "wiki-maintenance-$Year-$ts.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-ddTHH:mm:ss"), $Message
    Write-Host $line
    Add-Content -Path $LogFile -Value $line
}

# --- Gate: refuse if overnight alive ---
$gateOut = & $Python -c "from pipeline.wiki_ops_paths import overnight_pid_alive; print('ALIVE' if overnight_pid_alive('$Year') else 'STOPPED')"
if ($gateOut -match 'ALIVE') {
    Write-Log "REFUSED: overnight ingest PID is alive for year=$Year. Skip VACUUM/maintenance until stopped."
    Write-Log "After overnight ends, re-run: .\scripts\wiki-maintenance.ps1 -Year $Year"
    exit 2
}

$started = Get-Date
Write-Log "=== wiki-maintenance year=$Year log=$LogFile ==="

$analyzeRan = $false
$vacuumTables = @()
$vacuumSkipped = @()
$hotTables = @(
    "data", "graph_node", "graph_edge", "DocumentChunk_text",
    "EdgeType_relationship_name", "pipeline_runs", "TextDocument_name", "dataset_data"
)

function Invoke-PgSql {
    param([string]$Sql)
    $cmd = @(
        "docker", "exec", "empire-cognee-postgres",
        "psql", "-U", "cognee", "-d", "cognee_db", "-v", "ON_ERROR_STOP=1", "-c", $Sql
    )
    & $cmd[0] $cmd[1..($cmd.Length - 1)] 2>&1 | ForEach-Object { Write-Log "PG: $_" }
    return ($LASTEXITCODE -eq 0)
}

$pgUp = $false
try {
    $null = docker inspect -f "{{.State.Health.Status}}" empire-cognee-postgres 2>$null
    if ($LASTEXITCODE -eq 0) {
        $health = (docker inspect -f "{{.State.Health.Status}}" empire-cognee-postgres 2>$null)
        if ($health -eq "healthy" -or $health -eq "") { $pgUp = $true }
    }
}
catch {
    $pgUp = $false
}

if (-not $pgUp) {
    Write-Log "WARN: Postgres container not healthy - skip ANALYZE/VACUUM; continue reports/resolve"
}
else {
    if (-not $SkipAnalyze) {
        Write-Log "ANALYZE public..."
        if (Invoke-PgSql "ANALYZE;") { $analyzeRan = $true }
    }
    if (-not $SkipVacuum) {
        foreach ($table in $hotTables) {
            # Expandable string for SQL (avoid PowerShell here-strings; PS 5.1 -File mis-tokenizes them).
            $checkSql = "SELECT CASE WHEN COALESCE(n_live_tup,0)=0 THEN 0 ELSE n_dead_tup::float / NULLIF(n_live_tup,0) END AS dead_ratio, n_dead_tup FROM pg_stat_user_tables WHERE relname = '$table';"
            $out = docker exec empire-cognee-postgres psql -U cognee -d cognee_db -t -A -c $checkSql 2>$null
            $deadRatio = 0.0
            $deadTup = 0
            if ($out) {
                $parts = ($out.ToString().Trim() -split '\|')
                if ($parts.Length -ge 2) {
                    [void][double]::TryParse($parts[0], [ref]$deadRatio)
                    [void][int]::TryParse($parts[1], [ref]$deadTup)
                }
            }
            if ($deadRatio -ge 0.05 -or $deadTup -ge 10000) {
                if ($AllowVacuumFull) {
                    Write-Log "VACUUM FULL ANALYZE $table (explicit AllowVacuumFull)"
                    if (Invoke-PgSql "VACUUM FULL ANALYZE `"$table`";") { $vacuumTables += $table }
                }
                else {
                    Write-Log "VACUUM (ANALYZE) $table (dead_ratio=$deadRatio dead=$deadTup)"
                    if (Invoke-PgSql "VACUUM (ANALYZE) `"$table`";") { $vacuumTables += $table }
                }
            }
            else {
                $vacuumSkipped += $table
                Write-Log "Skip VACUUM $table (dead_ratio=$deadRatio dead=$deadTup)"
            }
        }
    }
}

if (-not $SkipTitles) {
    Write-Log "Export report with --rebuild-titles..."
    & $Python -m pipeline.wiki_report_export --year $Year --rebuild-titles --phase maintenance
    if ($LASTEXITCODE -ne 0) { throw "wiki_report_export --rebuild-titles failed" }
    Write-Log "Build FULL A-Z letter index from D:\wiki_md (for selecting not-yet-ingested articles)..."
    & $Python -m pipeline.wiki_titles_by_letter --year $Year --full
    if ($LASTEXITCODE -ne 0) { throw "wiki_titles_by_letter --full failed" }
}
else {
    Write-Log "Export status-only (skip titles)..."
    & $Python -m pipeline.wiki_report_export --year $Year --skip-titles --phase maintenance
}

if ($SeedCodex) {
    Write-Log "Seed Codex subjects (planning only)..."
    & (Join-Path $PSScriptRoot "seed-priority-subjects-from-codex.ps1")
}

if (-not $SkipPriorityResolve) {
    Write-Log "Resolve priority subjects..."
    & $Python -m pipeline.wiki_priority_resolve --year $Year
    if ($LASTEXITCODE -ne 0) { throw "wiki_priority_resolve failed" }
}

$ended = Get-Date
$duration = [math]::Round(($ended - $started).TotalSeconds, 1)
if ($duration -gt 7200) {
    Write-Log "WARN: maintenance exceeded 2h soft warn ($duration sec)"
}

$metaPath = Join-Path $env:TEMP "empire-wiki-maint-meta-$Year-$ts.json"
$meta = @{
    year           = $Year
    started_at     = $started.ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    analyze_ran    = $analyzeRan
    vacuum_tables  = @($vacuumTables)
    vacuum_skipped = @($vacuumSkipped)
    duration_sec   = $duration
    log_path       = $LogFile
} | ConvertTo-Json -Compress -Depth 4
[System.IO.File]::WriteAllText($metaPath, $meta, [System.Text.UTF8Encoding]::new($false))

# Write Python snippet to a temp file (avoid PowerShell here-strings; PS 5.1 -File mis-tokenizes them).
$pyPath = Join-Path $env:TEMP "empire-wiki-maint-status-$Year-$ts.py"
$pyLines = @(
    'import json',
    'from datetime import datetime, timezone',
    'from pathlib import Path',
    'from pipeline.wiki_report_export import write_wiki_status, build_progress_block',
    'from pipeline.wiki_checkpoint import load_checkpoint',
    'from pipeline.wiki_priority_subjects import load_subjects',
    'from pipeline.wiki_priority_resolved import list_awaiting',
    'from pipeline.wiki_ops_paths import subjects_path',
    '',
    ('meta = json.loads(Path(r''{0}'').read_text(encoding=''utf-8''))' -f $metaPath),
    'year = meta[''year'']',
    'cp = load_checkpoint()',
    'progress = build_progress_block(cp, year)',
    'doc = load_subjects()',
    'subjects = doc.get(''subjects'') or []',
    '',
    'def count(status):',
    '    return sum(1 for s in subjects if s.get(''status'') == status)',
    '',
    'awaiting = list_awaiting(year)',
    'now = datetime.now(timezone.utc).strftime(''%Y-%m-%dT%H:%M:%SZ'')',
    'write_wiki_status(',
    '    year,',
    '    phase=''idle'',',
    '    progress=progress,',
    '    maintenance={',
    '        ''started_at'': meta[''started_at''],',
    '        ''ended_at'': now,',
    '        ''complete'': True,',
    '        ''analyze_ran'': bool(meta.get(''analyze_ran'')),',
    '        ''vacuum_tables'': list(meta.get(''vacuum_tables'') or []),',
    '        ''vacuum_skipped'': list(meta.get(''vacuum_skipped'') or []),',
    '        ''duration_sec'': meta.get(''duration_sec''),',
    '        ''log_path'': meta.get(''log_path''),',
    '    },',
    '    priorities={',
    '        ''subjects_path'': str(subjects_path()),',
    '        ''subjects_pending'': count(''pending''),',
    '        ''subjects_needs_confirm'': count(''needs_confirm''),',
    '        ''subjects_unmatched'': count(''unmatched''),',
    '        ''subjects_resolved_done'': count(''resolved_done''),',
    '        ''resolved_awaiting_ingest'': len(awaiting),',
    '        ''updated_at'': now,',
    '    },',
    '    skip_titles=True,',
    ')',
    'print(''maintenance marked complete'')'
)
[System.IO.File]::WriteAllLines($pyPath, $pyLines)
& $Python $pyPath
Remove-Item $pyPath -ErrorAction SilentlyContinue
Remove-Item $metaPath -ErrorAction SilentlyContinue

Write-Log "=== maintenance complete duration=${duration}s ==="
exit 0
