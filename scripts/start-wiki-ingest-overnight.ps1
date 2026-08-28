<#
.SYNOPSIS
    Resumable overnight Wikipedia -> Cognee batch ingestion with checkpoints and logging.

.DESCRIPTION
    Processes D:\wiki_md\{Year}\batch_* directories into Cognee datasets (wikipedia_{year})
    using fast mode (frontmatter Truth-Drift edges + embeddings + one cognify per slice).
    Resumes from %LOCALAPPDATA%\EMPIRE\wiki-checkpoint.json automatically.

    Cognify flakes are non-fatal: each failed slice is retried once after a 60s backoff;
    after that the harness skips forward by FileLimit and continues. The run only stops
    after MaxConsecutiveFailures successive skipped slices (default 3).

    Logs and PID files go to I:\EMPIRE_DATA\logs\ (heavy data off C:).

.PARAMETER Year
    Snapshot year folder under D:\wiki_md (default 2017).

.PARAMETER FileLimit
    Max .md files per ingest invocation (default 200). Fast Mode on high-end GPUs
    (e.g. RTX 5080) can sustain 150-200; keep cognify/full mode lower (~30-50).

.PARAMETER MaxSlices
    Stop after this many successful slice runs (default 300).

.PARAMETER MaxHours
    Wall-clock cap in hours (default 23). Script exits cleanly when exceeded.
    Future runs use 23h; do not restart a live overnight just to pick up this default.

.PARAMETER StartBatch
    First batch index to consider (default 0). Skips batches already marked complete in checkpoint.

.PARAMETER SecondaryYear
    Optional second year to interleave after each primary slice (e.g. 2021). Empty = primary only.

.PARAMETER MaxConsecutiveFailures
    Stop the overnight loop after this many consecutive slice failures that exhausted their
    one retry (default 3). A successful slice resets the counter.

.EXAMPLE
    .\scripts\start-wiki-ingest-overnight.ps1 -Year 2017 -FileLimit 100 -MaxSlices 200 -MaxHours 12

.NOTES
    Requires: V:\Cognee mounted, Ollama on :11434, PocketBase on :8090 (optional but logged).
    status=error in the checkpoint is NOT permanent - overnight resumes from next_index.

    Detached Cursor-safe launch (breakaway from parent; keep a visible/minimized console):

      scripts\launch-wiki-ingest-overnight.cmd
      scripts\launch-wiki-ingest-overnight.cmd 2017 200 300 23 50

    Or from cmd.exe (first quoted string is the WINDOW TITLE - not the program name):

      start "EMPIRE-wiki-2017" /MIN powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\EMPIRE\scripts\start-wiki-ingest-overnight.ps1 -Year 2017 -FileLimit 200 -MaxSlices 300 -MaxHours 23 -FlushEvery 50

    Do NOT use: cmd /c start "EMPIRE-wiki-2017" /MIN cmd /c "..."
    That makes Windows look for a file named EMPIRE-wiki-2017 ("The system cannot find the file ...").

    Use /MIN for a taskbar window with live [wiki] progress, or omit /MIN for a full console.
#>
param(
    [string]$Year = "2017",
    [int]$FileLimit = 200,
    [int]$MaxSlices = 300,
    [double]$MaxHours = 23.0,
    [int]$StartBatch = 0,
    [string]$SecondaryYear = "",
    [int]$FlushEvery = 50,
    [int]$MaxConsecutiveFailures = 3
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$LogDir = "I:\EMPIRE_DATA\logs"
$Python = Join-Path $Root "venv\Scripts\python.exe"
$WikiRoot = if ($env:WIKI_ROOT) { $env:WIKI_ROOT } else { "D:\wiki_md" }
$CheckpointPath = Join-Path $env:LOCALAPPDATA "EMPIRE\wiki-checkpoint.json"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-ddTHH:mm:ss"), $Message
    Write-Host $line
    Add-Content -Path $script:LogFile -Value $line
}

function Keep-OllamaModelsWarm {
    <#
    .SYNOPSIS
        Pin embed (and optionally LLM) models in VRAM for the overnight run.
        Fast Mode only needs nomic-embed-text; skipping llama frees ~5GB on 16GB cards.
        Set EMPIRE_OVERNIGHT_PIN_LLAMA=1 to also pin llama3.1 for full cognify nights.
    #>
    $models = [System.Collections.Generic.List[object]]::new()
    $models.Add(@{ Name = "nomic-embed-text:latest"; Kind = "embed" })
    if ($env:EMPIRE_OVERNIGHT_PIN_LLAMA -eq "1") {
        $models.Insert(0, @{ Name = "llama3.1:latest"; Kind = "generate" })
    }
    foreach ($m in $models) {
        try {
            if ($m.Kind -eq "embed") {
                $body = @{ model = $m.Name; input = "warmup"; keep_alive = -1 } | ConvertTo-Json -Compress
                Invoke-RestMethod -Uri "http://localhost:11434/api/embed" -Method Post -Body $body -ContentType "application/json" -TimeoutSec 120 | Out-Null
            }
            else {
                $body = @{
                    model      = $m.Name
                    prompt     = "ping"
                    stream     = $false
                    keep_alive = -1
                    options    = @{ num_predict = 1 }
                } | ConvertTo-Json -Compress -Depth 5
                Invoke-RestMethod -Uri "http://localhost:11434/api/generate" -Method Post -Body $body -ContentType "application/json" -TimeoutSec 180 | Out-Null
            }
            Write-Log "Ollama keep_alive=-1: $($m.Name)"
        }
        catch {
            Write-Log "WARN: could not pin $($m.Name) keep_alive: $($_.Exception.Message)"
        }
    }
}

function Test-Preflight {
    if (-not (Test-Path "V:\Cognee")) {
        throw "V:\Cognee not mounted. Run scripts\mount-cognee-vhdx.ps1 as admin (see docs\COGNEE_VHDX.md)."
    }
    # OLLAMA_NUM_PARALLEL only applies when ollama serve starts (ensure-ollama-parallel.ps1).
    if (-not $env:OLLAMA_NUM_PARALLEL) { $env:OLLAMA_NUM_PARALLEL = "8" }
    $ensureScript = Join-Path $Root "scripts\ensure-ollama-parallel.ps1"
    if (Test-Path $ensureScript) {
        Write-Log "Ensuring ollama serve OLLAMA_NUM_PARALLEL=$($env:OLLAMA_NUM_PARALLEL) (skip restart if already set)..."
        & powershell.exe -NoProfile -ExecutionPolicy Bypass -File $ensureScript -NumParallel ([int]$env:OLLAMA_NUM_PARALLEL)
        if ($LASTEXITCODE -ne 0) {
            throw "ensure-ollama-parallel.ps1 failed (exit $LASTEXITCODE)"
        }
    }
    Write-Log "OLLAMA_NUM_PARALLEL=$($env:OLLAMA_NUM_PARALLEL) (verified on ollama serve when possible)"
    try {
        Invoke-RestMethod -Uri "http://localhost:11434/api/tags" -TimeoutSec 10 | Out-Null
        Write-Log "Ollama: OK"
    }
    catch {
        throw "Ollama not reachable at http://localhost:11434 - run scripts\ensure-ollama-parallel.ps1 or: ollama serve"
    }
    # Skip MCP / file-lock conflict warnings when Just-Postgres + EMPIRE_COGNEE_SKIP_FILE_LOCK.
    if ($env:EMPIRE_COGNEE_SKIP_FILE_LOCK -eq "1") {
        Write-Log "EMPIRE_COGNEE_SKIP_FILE_LOCK=1 - MCP cognee tools OK alongside overnight (Postgres)"
    }
    Keep-OllamaModelsWarm
    try {
        Invoke-RestMethod -Uri "http://127.0.0.1:8090/api/health" -TimeoutSec 5 | Out-Null
        Write-Log "PocketBase: OK"
    }
    catch {
        Write-Log "WARN: PocketBase not reachable - ingest_jobs will not be logged to PB"
    }
}

function Get-BatchDirs {
    param([string]$Y)
    $dir = Join-Path $WikiRoot $Y
    if (-not (Test-Path $dir)) { return @() }
    return @(Get-ChildItem $dir -Directory -Filter "batch_*" | Sort-Object Name)
}

function Get-CheckpointBatch {
    param([string]$Key)
    if (-not (Test-Path $CheckpointPath)) { return $null }
    $cp = Get-Content $CheckpointPath -Raw | ConvertFrom-Json
    return $cp.batches.$Key
}

function Get-CheckpointNextIndex {
    param([string]$Key)
    $entry = Get-CheckpointBatch -Key $Key
    if (-not $entry) { return 0 }
    return [int]$entry.next_index
}

function Update-CheckpointBatchFields {
    param(
        [string]$Key,
        [hashtable]$Fields
    )
    if (-not (Test-Path $CheckpointPath)) { return $false }
    $tmpFields = Join-Path $env:TEMP "empire-wiki-cp-fields-$PID.json"
    # Windows PowerShell 5.1 Set-Content -Encoding utf8 writes a BOM that breaks json.loads.
    # Write via .NET UTF8Encoding(false) so both PS5 and PS7 produce BOM-free JSON.
    $json = ($Fields | ConvertTo-Json -Compress)
    [System.IO.File]::WriteAllText($tmpFields, $json, [System.Text.UTF8Encoding]::new($false))
    $code = @"
import json, pathlib, sys
p = pathlib.Path(r'$CheckpointPath')
k = r'$Key'
f = json.loads(pathlib.Path(r'$tmpFields').read_text(encoding='utf-8-sig'))
d = json.loads(p.read_text(encoding='utf-8-sig'))
e = d.setdefault('batches', {}).setdefault(k, {})
e.update(f)
p.write_text(json.dumps(d, indent=2), encoding='utf-8')
"@
    & $Python -c $code
    $ok = ($LASTEXITCODE -eq 0)
    Remove-Item $tmpFields -ErrorAction SilentlyContinue
    return $ok
}

function Set-CheckpointSkipForward {
    <#
    .SYNOPSIS
        After a slice exhausts retries, advance next_index by FileLimit so the overnight
        loop does not spin forever on the same window. Clears status=error -> in_progress.
    #>
    param(
        [string]$Key,
        [int]$FromIndex,
        [int]$AdvanceBy,
        [int]$Total = 0
    )
    if (-not (Test-Path $CheckpointPath)) {
        Write-Log "WARN: no checkpoint file; cannot skip-forward $Key"
        return $FromIndex
    }
    $entry = Get-CheckpointBatch -Key $Key
    if (-not $entry) {
        Write-Log "WARN: checkpoint missing key $Key; cannot skip-forward"
        return $FromIndex
    }
    $newIndex = $FromIndex + $AdvanceBy
    if ($Total -gt 0 -and $newIndex -gt $Total) { $newIndex = $Total }
    $updated = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    $ok = Update-CheckpointBatchFields -Key $Key -Fields @{
        next_index = $newIndex
        status     = "in_progress"
        updated    = $updated
    }
    if (-not $ok) {
        Write-Log "WARN: skip-forward write failed for $Key"
        return $FromIndex
    }
    Write-Log "SKIP-FORWARD ${Key}: next_index $FromIndex -> $newIndex (status=in_progress)"
    return $newIndex
}

function Clear-CheckpointErrorStatus {
    param([string]$Key)
    $entry = Get-CheckpointBatch -Key $Key
    if ($entry -and $entry.status -eq "error") {
        $updated = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
        $null = Update-CheckpointBatchFields -Key $Key -Fields @{
            status  = "in_progress"
            updated = $updated
        }
        Write-Log "Cleared status=error on $Key (resuming from next_index=$($entry.next_index))"
    }
}

function Test-HighSignalLine {
    param([string]$Line)
    if ([string]::IsNullOrWhiteSpace($Line)) { return $false }
    # Live console: wiki progress + harness errors; full stream still goes to the log.
    return ($Line -match '^\[wiki\]|__WIKI_RESULT__|^ERROR|^WARN|docs/s|Slice |Ollama |PocketBase |SKIP-FORWARD|===')
}

function Invoke-WikiSlice {
    param(
        [string]$Y,
        [string]$BatchName,
        [int]$Limit
    )
    $batchIdx = [int]($BatchName -replace '^batch_', '')
    $pyArgs = @(
        "-u",
        "-m", "pipeline.wiki_ingest",
        "--year", $Y,
        "--batch", "$batchIdx",
        "--mode", "fast",
        "--limit", "$Limit",
        "--flush-every", "$FlushEvery"
    )
    $env:PYTHONPATH = $Root
    $env:PYTHONUNBUFFERED = "1"
    # Fast Mode throughput knobs (5080 / 64GB class defaults).
    if (-not $env:EMPIRE_COGNIFY_SKIP_SUMMARIZE) { $env:EMPIRE_COGNIFY_SKIP_SUMMARIZE = "1" }
    if (-not $env:EMPIRE_OLLAMA_STRUCTURED_MAX_RETRIES) { $env:EMPIRE_OLLAMA_STRUCTURED_MAX_RETRIES = "2" }
    if (-not $env:EMPIRE_EMBED_DATA_PER_BATCH) { $env:EMPIRE_EMBED_DATA_PER_BATCH = "16" }
    if (-not $env:EMPIRE_REMEMBER_CONCURRENCY) { $env:EMPIRE_REMEMBER_CONCURRENCY = "20" }
    if (-not $env:EMPIRE_REMEMBER_DATA_PER_BATCH) { $env:EMPIRE_REMEMBER_DATA_PER_BATCH = "16" }
    if (-not $env:EMBEDDING_BATCH_SIZE) { $env:EMBEDDING_BATCH_SIZE = "512" }
    if (-not $env:EMPIRE_QUIET_COGNEE) { $env:EMPIRE_QUIET_COGNEE = "1" }
    if (-not $env:EMPIRE_COGNEE_SKIP_FILE_LOCK) { $env:EMPIRE_COGNEE_SKIP_FILE_LOCK = "1" }
    if (-not $env:OLLAMA_NUM_PARALLEL) { $env:OLLAMA_NUM_PARALLEL = "8" }
    Write-Log "Slice start $Y/$BatchName limit=$Limit flushEvery=$FlushEvery embedBatch=$($env:EMBEDDING_BATCH_SIZE) embedParallel=$($env:EMPIRE_EMBED_DATA_PER_BATCH) rememberConc=$($env:EMPIRE_REMEMBER_CONCURRENCY) rememberDpb=$($env:EMPIRE_REMEMBER_DATA_PER_BATCH)"
    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    $stdoutLines = New-Object System.Collections.Generic.List[string]
    $stderrLines = New-Object System.Collections.Generic.List[string]
    # Live tee: stream Python stdout/stderr to console + overnight log (not post-slice dump).
    # Avoid Start-Process -Redirect* which buffers until process exit on Windows.
    $prevEap = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    Push-Location $Root
    try {
        & $Python @pyArgs 2>&1 | ForEach-Object {
            $line = "$_"
            if ($line -match '^ERROR|Traceback|Exception|Could not set lock|database lock') {
                [void]$stderrLines.Add($line)
            }
            else {
                [void]$stdoutLines.Add($line)
            }
            Add-Content -Path $script:LogFile -Value $line
            if (Test-HighSignalLine -Line $line) {
                Write-Host $line
            }
        }
        $exitCode = $LASTEXITCODE
    }
    finally {
        Pop-Location
        $ErrorActionPreference = $prevEap
    }
    $sw.Stop()
    $stdout = ($stdoutLines -join "`n")
    $stderr = ($stderrLines -join "`n")
    Write-Log "Slice end $Y/$BatchName exit=$exitCode wall=$([math]::Round($sw.Elapsed.TotalSeconds, 1))s"
    return @{
        ExitCode = $exitCode
        Seconds  = [math]::Round($sw.Elapsed.TotalSeconds, 1)
        Stdout   = $stdout
        Stderr   = $stderr
    }
}

function Get-NextBatchForYear {
    param([string]$Y, [int]$FromIndex)
    $batches = Get-BatchDirs -Y $Y
    foreach ($b in $batches) {
        $idx = [int]($b.Name -replace '^batch_', '')
        if ($idx -lt $FromIndex) { continue }
        $key = "$Y/$($b.Name)"
        if (Test-Path $CheckpointPath) {
            $cp = Get-Content $CheckpointPath -Raw | ConvertFrom-Json
            $entry = $cp.batches.$key
            # Only skip fully complete batches. status=error / in_progress are resumable.
            if ($entry -and $entry.status -eq "complete") { continue }
        }
        return $b.Name
    }
    return $null
}

function Invoke-SliceWithRetry {
    <#
    .SYNOPSIS
        Run a wiki slice; on non-lock failure wait 60s and retry once.
        Lock conflicts get up to 3 attempts with 120s sleep (unchanged).
    #>
    param(
        [string]$Y,
        [string]$BatchName,
        [int]$Limit
    )
    $result = $null
    $lockAttempts = 0
    $didCognifyRetry = $false

    while ($true) {
        $result = Invoke-WikiSlice -Y $Y -BatchName $BatchName -Limit $Limit
        if ($result.ExitCode -eq 0) {
            return @{ Result = $result; Exhausted = $false }
        }

        if ($result.Stderr -match "lock conflict|database lock|Could not set lock") {
            $lockAttempts++
            if ($lockAttempts -lt 3) {
                Write-Log "Lock conflict (attempt $lockAttempts/3), sleeping 120s..."
                Start-Sleep -Seconds 120
                continue
            }
            Write-Log "ERROR exit $($result.ExitCode) after lock retries: $($result.Stderr)"
            return @{ Result = $result; Exhausted = $true }
        }

        Write-Log "ERROR exit $($result.ExitCode): $($result.Stderr)"
        if (-not $didCognifyRetry) {
            $didCognifyRetry = $true
            Write-Log "Retrying same slice once after 60s backoff ($Y/$BatchName)..."
            Start-Sleep -Seconds 60
            continue
        }

        Write-Log "Slice retry exhausted for $Y/$BatchName"
        return @{ Result = $result; Exhausted = $true }
    }
}

# --- main ---
# Postgres overnight: skip file-lock / MCP conflict noise (Just-Postgres shared writers OK).
if (-not $env:EMPIRE_COGNEE_SKIP_FILE_LOCK) { $env:EMPIRE_COGNEE_SKIP_FILE_LOCK = "1" }

New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$ts = Get-Date -Format "yyyyMMdd-HHmmss"
$script:LogFile = Join-Path $LogDir "wiki-ingest-overnight-$Year-$ts.log"
$PidFile = Join-Path $LogDir "wiki-ingest-overnight-$Year.pid"

# Refuse to start a duplicate harness for the same year
if (Test-Path $PidFile) {
    $existingPid = 0
    try { $existingPid = [int]((Get-Content $PidFile -Raw).Trim()) } catch { $existingPid = 0 }
    if ($existingPid -gt 0) {
        $alive = Get-Process -Id $existingPid -ErrorAction SilentlyContinue
        if ($alive) {
            throw "Overnight harness already running for year=$Year (PID $existingPid). Refusing duplicate."
        }
        Write-Host "Stale PID file for $existingPid - removing"
        Remove-Item $PidFile -ErrorAction SilentlyContinue
    }
}
$PID | Set-Content $PidFile

Write-Log "=== EMPIRE overnight wiki ingest (year=$Year limit=$FileLimit maxSlices=$MaxSlices maxHours=$MaxHours maxConsecutiveFailures=$MaxConsecutiveFailures) ==="
Write-Log "Log: $script:LogFile"
Write-Log "PID: $PID -> $PidFile"
Write-Log "Checkpoint: $CheckpointPath (status=error is resumable)"

Test-Preflight

# Drain resolved priority articles once at window start (before linear checkpoint).
Write-Log "Priority drain (once at window start)..."
$env:PYTHONPATH = $Root
& $Python -m pipeline.wiki_ingest --year $Year --drain-priorities --flush-every $FlushEvery
if ($LASTEXITCODE -ne 0) {
    Write-Log "WARN: priority drain exited $LASTEXITCODE - continuing to linear ingest"
}

$deadline = (Get-Date).AddHours($MaxHours)
$slicesDone = 0
$totalProcessed = 0
$failures = 0
$consecutiveFailures = 0
$currentBatchIdx = $StartBatch
$stopReason = "batches_complete"
$AbortFlag = Join-Path $env:LOCALAPPDATA "EMPIRE\wiki-abort.flag"

while ($slicesDone -lt $MaxSlices -and (Get-Date) -lt $deadline) {
    if (Test-Path $AbortFlag) {
        Write-Log "Operator abort flag present - finishing after current work, then stop."
        $stopReason = "operator_abort"
        Remove-Item $AbortFlag -ErrorAction SilentlyContinue
        break
    }

    $batchName = Get-NextBatchForYear -Y $Year -FromIndex $currentBatchIdx
    if (-not $batchName) {
        Write-Log "No more incomplete batches for year $Year (from index $currentBatchIdx)."
        $stopReason = "batches_complete"
        break
    }

    $key = "$Year/$batchName"
    Clear-CheckpointErrorStatus -Key $key
    $preIndex = Get-CheckpointNextIndex -Key $key
    $entry = Get-CheckpointBatch -Key $key
    $totalFiles = if ($entry -and $entry.total) { [int]$entry.total } else { 0 }

    Write-Log "Slice $($slicesDone + 1)/${MaxSlices}: $Year/$batchName from next_index=$preIndex (limit $FileLimit)..."
    $attempt = Invoke-SliceWithRetry -Y $Year -BatchName $batchName -Limit $FileLimit
    $result = $attempt.Result

    if ($result.ExitCode -ne 0) {
        $failures++
        $consecutiveFailures++
        Write-Log "Slice FAILED for $Year/$batchName (consecutiveFailures=$consecutiveFailures/$MaxConsecutiveFailures)"

        if ($consecutiveFailures -ge $MaxConsecutiveFailures) {
            Write-Log "MaxConsecutiveFailures ($MaxConsecutiveFailures) reached - stopping primary loop."
            $stopReason = "consecutive_failures"
            break
        }

        # Skip this window and continue; do not treat status=error as terminal.
        $null = Set-CheckpointSkipForward -Key $key -FromIndex $preIndex -AdvanceBy $FileLimit -Total $totalFiles
        Write-Log "Continuing overnight after skip (remaining consecutive budget: $($MaxConsecutiveFailures - $consecutiveFailures))"
        Start-Sleep -Seconds 5
        continue
    }

    $consecutiveFailures = 0
    $slicesDone++
    $docsThis = 0
    $rateThis = ""
    if ($result.Stdout -match '"processed":\s*(\d+)') {
        $docsThis = [int]$Matches[1]
        $totalProcessed += $docsThis
    }
    if ($result.Stdout -match '"docs_per_sec":\s*([0-9.]+)') {
        $rateThis = " $($Matches[1]) docs/s"
    }
    Write-Log "Slice OK in $($result.Seconds)s$rateThis (sliceDocs=$docsThis cumulative~=$totalProcessed next_index checkpoint may advance)"

    # Advance batch index if this batch is now complete
    if (Test-Path $CheckpointPath) {
        $cp = Get-Content $CheckpointPath -Raw | ConvertFrom-Json
        $entry = $cp.batches.$key
        if ($entry -and $entry.status -eq "complete") {
            $currentBatchIdx = [int]($batchName -replace '^batch_', '') + 1
            Write-Log "Batch $batchName complete - next batch index $currentBatchIdx"
        }
    }

    if ($SecondaryYear) {
        $secBatch = Get-NextBatchForYear -Y $SecondaryYear -FromIndex 0
        if ($secBatch) {
            Write-Log "Secondary slice: $SecondaryYear/$secBatch..."
            $sec = Invoke-WikiSlice -Y $SecondaryYear -BatchName $secBatch -Limit $FileLimit
            if ($sec.ExitCode -eq 0) {
                Write-Log "Secondary slice OK in $($sec.Seconds)s"
            }
            else {
                Write-Log "WARN: secondary slice failed (non-fatal)"
            }
        }
    }

    Start-Sleep -Seconds 5
}

if ((Get-Date) -ge $deadline -and $stopReason -eq "batches_complete" -and $slicesDone -gt 0) {
    # Prefer max_hours when deadline hit mid-loop exit
}
if ((Get-Date) -ge $deadline -and $stopReason -ne "operator_abort" -and $stopReason -ne "consecutive_failures") {
    $more = Get-NextBatchForYear -Y $Year -FromIndex $currentBatchIdx
    if ($more) { $stopReason = "max_hours" }
}

Write-Log "=== Overnight ingest finished: slices=$slicesDone processed~=$totalProcessed failures=$failures consecutiveAtEnd=$consecutiveFailures stop_reason=$stopReason ==="

# Stop snapshot (checkpoint-only; no titles rebuild during/after overnight stop)
try {
    $env:PYTHONPATH = $Root
    & $Python -c @"
from pipeline.wiki_report_export import write_wiki_status, build_progress_block
from pipeline.wiki_checkpoint import load_checkpoint
from datetime import datetime, timezone
year = '$Year'
cp = load_checkpoint()
progress = build_progress_block(cp, year)
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
write_wiki_status(
    year,
    phase='ingest_stopped',
    ingest={
        'max_hours': $MaxHours,
        'ended_at': now,
        'stop_reason': '$stopReason',
        'slices_done': $slicesDone,
        'docs_this_window': $totalProcessed,
        'pid_file': r'$PidFile',
        'log_glob': r'I:\\EMPIRE_DATA\\logs\\wiki-ingest-overnight-$Year-*.log',
    },
    skip_titles=True,
)
print('stop snapshot written')
"@
}
catch {
    Write-Log "WARN: stop snapshot failed: $($_.Exception.Message)"
}

Remove-Item $PidFile -ErrorAction SilentlyContinue
exit 0
