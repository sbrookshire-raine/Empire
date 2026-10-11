#Requires -Version 5.1
param(
    [switch]$SkipOllamaCheck,
    [switch]$Weaviate,
    [switch]$NoWiki,
    [switch]$NoVoice,
    [switch]$SkipStartupChecks
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot

function Test-Url {
    param([string]$Url)
    try {
        $response = Invoke-WebRequest -Uri $Url -UseBasicParsing -TimeoutSec 4
        return $response.StatusCode -ge 200 -and $response.StatusCode -lt 400
    }
    catch {
        return $false
    }
}

function Wait-Url {
    param([string]$Name, [string]$Url)
    for ($attempt = 1; $attempt -le 45; $attempt++) {
        if (Test-Url $Url) {
            Write-Host "  $Name healthy"
            return
        }
        Start-Sleep -Seconds 1
    }
    throw "$Name did not become healthy: $Url"
}

Write-Host "EMPIRE start"
Write-Host "============"

# Startup should cost the longest leg, not the sum of every leg - services that
# do not depend on each other are launched together and awaited in a second pass.
$StartupClock = [System.Diagnostics.Stopwatch]::StartNew()

. (Join-Path $PSScriptRoot "lib\cognee-storage.ps1")
. (Join-Path $PSScriptRoot "lib\git-path.ps1")
. (Join-Path $PSScriptRoot "lib\resolve-wiki-storage.ps1")
. (Join-Path $PSScriptRoot "lib\read-eve-toolbelt.ps1")
Ensure-GitOnPath -Quiet | Out-Null
$cogneeRoot = Ensure-EmpireCogneeRoot
$env:EMPIRE_COGNEE_ROOT = $cogneeRoot
$env:PYTHONPATH = $Root
Write-Host "  Cognee file root: $cogneeRoot"
$wikiStorage = Initialize-EmpireWikiStorageEnv
Write-Host "  Wiki reports root: $($wikiStorage.reports_root)"
Write-Host "  Weaviate archive:  $($wikiStorage.weaviate_archive)"
$wikiArchiveReady = Test-Path -LiteralPath $wikiStorage.weaviate_archive
$toolbeltOn = @(Get-EmpireToolbeltActive -RepoRoot $Root)
$wikiLimbOn = "wiki_local" -in $toolbeltOn
$voiceLimbOn = "voice_presence" -in $toolbeltOn
$startWikiLocal = (-not $NoWiki) -and ($wikiLimbOn -or $Weaviate) -and ($Weaviate -or $wikiArchiveReady)
if ($startWikiLocal -and -not $wikiArchiveReady) {
    Write-Warning "Wiki Local requested but archive path missing: $($wikiStorage.weaviate_archive)"
    $startWikiLocal = $false
}
if (-not $wikiLimbOn -and -not $Weaviate -and -not $NoWiki) {
    Write-Host "  Wiki Local stack skipped (wiki_local off in toolbelt; turn on in header or -Weaviate)"
}
if ($startWikiLocal) {
    & (Join-Path $PSScriptRoot "ensure-wiki-title-index.ps1") -StartBackgroundBuild
}

try {
    & (Join-Path $PSScriptRoot "ensure-cognee-postgres.ps1")
}
catch {
    Write-Warning "Cognee Postgres did not start: $($_.Exception.Message)"
    Write-Warning "Eve chat may still work; memory/graph features need Docker."
}

if (-not $SkipOllamaCheck -and -not (Test-Url "http://127.0.0.1:11434/api/tags")) {
    throw "Ollama is down. Start Ollama and run this command again."
}
Write-Host "  Ollama healthy"

# --- launch phase: independent services start together ---
if (-not (Test-Url "http://127.0.0.1:8090/api/health")) {
    Start-Process -FilePath (Join-Path $Root "backend\pocketbase\pocketbase.exe") `
        -ArgumentList "serve","--http=127.0.0.1:8090" `
        -WorkingDirectory (Join-Path $Root "backend\pocketbase")
}

$workbenchFresh = -not (Test-Url "http://127.0.0.1:8080/api/memory/status")
if ($workbenchFresh) {
    Write-Host "  Eve Workbench (venv + wiki paths)..."
}
else {
    Write-Host "  Refreshing Eve Workbench (pick up routing/latency fixes)..."
    foreach ($line in (netstat -ano | Select-String ":8080\s" | Select-String "LISTENING")) {
        $procId = ($line -split "\s+") | Where-Object { $_ -match "^\d+$" } | Select-Object -Last 1
        if ($procId -and $procId -ne "0") {
            Stop-Process -Id ([int]$procId) -Force -ErrorAction SilentlyContinue
        }
    }
    Start-Sleep -Seconds 1
}
$frontendScript = Join-Path $Root "scripts\start-frontend.ps1"
Start-Process -FilePath "powershell.exe" `
    -ArgumentList @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-WindowStyle", "Hidden",
        "-Command",
        "& { `$env:EMPIRE_TRACE='1'; `$env:PYTHONPATH='$Root'; Set-Location '$Root'; & '$Root\venv\Scripts\python.exe' -m frontend.serve }"
    ) `
    -WorkingDirectory $Root | Out-Null

# Eve's build check and the voice container depend on nothing the two above
# provide, so they start now and are awaited below.
$EveDown = -not (Test-Url "http://127.0.0.1:2000/eve/v1/info")
$EveBuild = $null
if ($EveDown) {
    $EveBuild = Start-Process -FilePath (Join-Path $Root "venv\Scripts\python.exe") `
        -ArgumentList (Join-Path $Root "scripts\ensure-eve-build.py") `
        -WorkingDirectory $Root -PassThru
}

$VoiceProc = $null
$startVoice = (-not $NoVoice) -and $voiceLimbOn
if (-not $startVoice -and -not $NoVoice) {
    Write-Host "  Voice (Speaches) skipped (voice_presence off in toolbelt; turn on in header strip)"
}
if ($startVoice) {
    $VoiceProc = Start-Process -FilePath "powershell.exe" `
        -ArgumentList "-NoProfile","-ExecutionPolicy","Bypass","-File",(Join-Path $PSScriptRoot "start-voice.ps1") `
        -WindowStyle Hidden -PassThru
}

# --- wait phase ---
Wait-Url "PocketBase" "http://127.0.0.1:8090/api/health"
Wait-Url "Eve Workbench" "http://127.0.0.1:8080/api/memory/status"

if ($EveDown) {
    if ($EveBuild) {
        $EveBuild.WaitForExit()
        if ($EveBuild.ExitCode -ne 0) {
            throw "Eve production build preparation failed."
        }
    }
    $env:EMPIRE_ROOT = $Root
    $env:POCKETBASE_URL = "http://127.0.0.1:8090"
    $env:OLLAMA_BASE_URL = "http://localhost:11434/v1"
    $env:OLLAMA_MODEL = "richardyoung/qwen2.5-14b-instruct-abliterated:latest"
    $npm = (Get-Command npm.cmd -ErrorAction Stop).Source

    # Sweep orphaned workflow runs so Eve boots with a clean queue instead of
    # re-enqueuing stale "running" runs left behind by a crash or forced stop.
    & (Join-Path $PSScriptRoot "cleanup-stale-runs.ps1")
    # One-per-chat Docker sandboxes (legacy backend) must not accumulate across restarts.
    & (Join-Path $PSScriptRoot "stop-eve-sandbox-containers.ps1") -Kill -Remove -Quiet

    Start-Process -FilePath $npm `
        -ArgumentList "exec","--","eve","start","--host","127.0.0.1","--port","2000" `
        -WorkingDirectory (Join-Path $Root "agents\empire-task-agent")
}
Wait-Url "Eve" "http://127.0.0.1:2000/eve/v1/info"

if ($VoiceProc) {
    Write-Host ""
    try {
        Wait-Url "Voice (Speaches)" "http://127.0.0.1:8000/health"
    }
    catch {
        Write-Warning "Voice (Speaches) not confirmed healthy on :8000. Eve text chat still works."
    }
    if ($VoiceProc.HasExited -and $VoiceProc.ExitCode -ne 0) {
        Write-Warning "Voice (Speaches) did not start cleanly. Eve text chat still works; push-to-talk needs port 8000."
    }
}

if ($startWikiLocal) {
    Write-Host ""
    try {
        & (Join-Path $PSScriptRoot "start-weaviate.ps1")
    }
    catch {
        Write-Warning "Wiki Local Weaviate did not start: $($_.Exception.Message)"
        Write-Warning "EMPIRE will run without wiki archive on :8091. Start Docker and retry, or use Start-EMPIRE.bat -NoWiki"
        $startWikiLocal = $false
    }
}

& (Join-Path $PSScriptRoot "refresh-dashboard.ps1")

if (-not $SkipStartupChecks) {
    $py = Join-Path $Root "venv\Scripts\python.exe"
    if ($startWikiLocal -and (Test-Path -LiteralPath $py)) {
        Write-Host ""
        Write-Host "Wiki Local preflight"
        & (Join-Path $PSScriptRoot "verify-wiki-local.ps1") -SkipSearch
        if ($LASTEXITCODE -eq 1) {
            Write-Warning "Wiki preflight failed - archive or Weaviate. Wiki asks may fail until fixed."
        }
    }
    if (Test-Path -LiteralPath $py) {
        Write-Host ""
        Write-Host "Baseline audit (host + Docker + services + pulse)"
        & (Join-Path $PSScriptRoot "baseline-audit.ps1") -Json
        if ($LASTEXITCODE -ne 0) {
            Write-Warning "Baseline audit reported blockers. Try: .\scripts\baseline-audit.ps1 -FixOrphans"
        }
        Write-Host ""
        Write-Host "Query battery (fast: routing + wiki green + session inject)"
        & $py (Join-Path $Root "scripts\run-query-battery.py") --tier fast
        if ($LASTEXITCODE -ne 0) {
            Write-Warning "Query battery failed. Stop-EMPIRE.bat then Start-EMPIRE.bat after code updates."
        }
    }
}
else {
    Write-Host "  Startup checks skipped (-SkipStartupChecks)"
}

$StartupClock.Stop()
Write-Host ("  Startup: {0:N1}s" -f $StartupClock.Elapsed.TotalSeconds)

Write-Host ""
Write-Host "Ready: http://127.0.0.1:8080/eve.html"
if ($startVoice) {
    Write-Host "Voice (Speaches):  http://127.0.0.1:8000  (Eve push-to-talk / auto-speak)"
}
if ($startWikiLocal) {
    Write-Host "Wiki Local Weaviate: http://127.0.0.1:8091"
}
