# Architect smoke scorecard - CLI checks for Phases 1-8 (ASCII only for PS 5.1)
# Usage:
#   .\scripts\architect-smoke-helper.ps1
#   .\scripts\architect-smoke-helper.ps1 -StartWorker
#   .\scripts\architect-smoke-helper.ps1 -Scorecard
# Does NOT mark Smoke PASS for you - reply in Cursor after Eve UI checks.
param(
  [switch]$StartWorker,
  [switch]$Scorecard
)

$ErrorActionPreference = "Continue"
$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $Root
$py = Join-Path $Root "venv\Scripts\python.exe"
if (-not (Test-Path $py)) {
  Write-Host "ERROR: venv python missing"
  exit 1
}

function Test-HttpUp([int]$Port) {
  try {
    Invoke-WebRequest -Uri "http://127.0.0.1:$Port/" -UseBasicParsing -TimeoutSec 2 | Out-Null
    return $true
  } catch {
    $m = $_.Exception.Message
    if ($m -match '400|401|403|404|405|500') { return $true }
    return $false
  }
}

Write-Host ""
Write-Host "=== EMPIRE Architect smoke helper ==="
Write-Host "Repo: $Root"
Write-Host ""

# --- Smoke A ---
Write-Host "--- Smoke A: GPU lease / fixtures ---"
& $py -m pipeline.gpu_lease release | Out-Null
$chat = & $py -m pipeline.gpu_lease acquire chat --holder smoke-a | ConvertFrom-Json
$deny = & $py -m pipeline.gpu_lease acquire extract --holder should-fail | ConvertFrom-Json
& $py -m pipeline.gpu_lease release | Out-Null
$fixtures = @(Get-ChildItem (Join-Path $Root "data\eval\structured_extract\fixtures\*.txt") -ErrorAction SilentlyContinue)
$audit = Join-Path $env:LOCALAPPDATA "EMPIRE\admission-audit.jsonl"
$manifest = Test-Path (Join-Path $Root "config\empire-release-manifest.json")
$denyOk = -not [bool]$deny.ok
$aPass = ([bool]$chat.ok) -and $denyOk -and ($fixtures.Count -ge 5) -and $manifest
Write-Host ("  acquire chat:     {0}" -f [bool]$chat.ok)
Write-Host ("  deny extract:     {0} (want True)" -f $denyOk)
Write-Host ("  fixtures:         {0}" -f $fixtures.Count)
Write-Host ("  release manifest: {0}" -f $manifest)
Write-Host ("  audit log exists: {0}" -f (Test-Path $audit))
if ($aPass) {
  Write-Host "SMOKE_A_RESULT=PASS"
  Write-Host "  -> In Cursor reply: Smoke PASS Phase 1"
} else {
  Write-Host "SMOKE_A_RESULT=FAIL - paste this output in Cursor"
}

$gguf = Join-Path $env:LOCALAPPDATA "EMPIRE\models\gguf\Qwen3-14B-Q4_K_M.gguf"
$llama = Join-Path $env:LOCALAPPDATA "EMPIRE\bin\llama.cpp\win-cuda-12.4\llama-server.exe"

if ($Scorecard) {
  Write-Host ""
  Write-Host "--- Scorecard (CLI; Eve UI still required for Phase 2 Toolbelt) ---"
  $results = @{}

  # Phase 1
  $results["phase1"] = @{ status = $(if ($aPass) { "PASS" } else { "FAIL" }); note = "gpu lease + fixtures" }

  # Phase 2 assets + optional extract via Ollama fallback if worker down
  $p2Assets = (Test-Path $gguf) -and (Test-Path $llama)
  $p2Worker = $false
  try {
    $h = Invoke-WebRequest -Uri "http://127.0.0.1:8092/health" -UseBasicParsing -TimeoutSec 2
    if ($h.StatusCode -eq 200) { $p2Worker = $true }
  } catch {
    try {
      $h2 = Invoke-WebRequest -Uri "http://127.0.0.1:8092/v1/models" -UseBasicParsing -TimeoutSec 2
      if ($h2.StatusCode -eq 200) { $p2Worker = $true }
    } catch {}
  }
  $p2Extract = $false
  $p2Note = "assets=$p2Assets worker=$p2Worker"
  if ($p2Assets) {
    if ($p2Worker) {
      $ex = & $py -m pipeline.structured_extract file "data\eval\structured_extract\fixtures\01_research_note.txt" --prefer llama 2>&1 | Out-String
      $p2Extract = ($ex -match '"ok"\s*:\s*true') -or ($LASTEXITCODE -eq 0 -and $ex -match 'title')
      $p2Note = "llama extract CLI"
    } else {
      $ex = & $py -m pipeline.structured_extract file "data\eval\structured_extract\fixtures\01_research_note.txt" --prefer ollama 2>&1 | Out-String
      $p2Extract = ($ex -match '"ok"\s*:\s*true') -or ($LASTEXITCODE -eq 0 -and $ex -match 'title')
      $p2Note = "ollama fallback CLI (start worker for full Soft Smoke B)"
    }
  }
  $p2Status = if ($p2Assets -and $p2Extract) { "CLI_PASS" } elseif ($p2Assets) { "ASSETS_OK" } else { "FAIL" }
  $results["phase2"] = @{ status = $p2Status; note = $p2Note; eve_ui_still_required = $true }

  # Phase 3
  $rerankRaw = & $py -m pipeline.retrieval_rerank eval 2>&1 | Out-String
  $rerankOk = $false
  try {
    $rj = $rerankRaw | ConvertFrom-Json -ErrorAction Stop
    $rerankOk = ([int]$rj.hits -ge 3) -and ([int]$rj.cases -ge 3)
  } catch {
    $rerankOk = ($rerankRaw -match 'hits.:.?3') -or ($rerankRaw -match '"hits":\s*3')
  }
  $results["phase3"] = @{ status = $(if ($rerankOk) { "PASS" } else { "FAIL" }); note = "retrieval_rerank eval" }

  # Phase 4 allowlist
  $allowOut = & $py -c "from pipeline.browser_local import is_allowed; a,b=is_allowed('http://127.0.0.1:8080/eve.html'); c,d=is_allowed('https://example.com/'); print(a, (not c))" 2>&1 | Out-String
  $allowOk = $allowOut -match 'True True'
  $feUp = Test-HttpUp 8080
  $results["phase4"] = @{ status = $(if ($allowOk) { if ($feUp) { "PASS_ALLOWLIST" } else { "CLI_PASS_NEED_FRONTEND" } } else { "FAIL" }); note = "allowlist; frontend_up=$feUp" }

  # Phase 5 - module present
  $vad = Test-Path (Join-Path $Root "pipeline\voice_vad.py")
  $voice = Test-Path (Join-Path $Root "pipeline\voice_presence.py")
  $results["phase5"] = @{ status = $(if ($vad -and $voice) { "WIRED" } else { "FAIL" }); note = "VAD+voice files; mic UI smoke still Architect" }

  # Phase 6
  $visPy = Test-Path (Join-Path $Root "pipeline\vision_ui_observe.py")
  $results["phase6"] = @{ status = $(if ($visPy) { "WIRED" } else { "FAIL" }); note = "observe-only module; Toolbelt Vision Local still Architect" }

  # Phase 7
  $results["phase7"] = @{ status = "PARKED"; note = "PaddleOCR - skip until Docling fails" }

  # Phase 8
  $sbomDir = Join-Path $Root "data\eval\sbom"
  $sbomFiles = @(Get-ChildItem $sbomDir -ErrorAction SilentlyContinue)
  if ($sbomFiles.Count -lt 1) {
    & (Join-Path $Root "scripts\empire-sbom.ps1") | Out-Null
    $sbomFiles = @(Get-ChildItem $sbomDir -ErrorAction SilentlyContinue)
  }
  $results["phase8"] = @{ status = $(if ($sbomFiles.Count -ge 1) { "PASS" } else { "FAIL" }); note = "reports=$($sbomFiles.Count)" }

  Write-Host ""
  Write-Host "PHASE SCORECARD"
  foreach ($k in @("phase1","phase2","phase3","phase4","phase5","phase6","phase7","phase8")) {
    $r = $results[$k]
    Write-Host ("  {0}: {1}  ({2})" -f $k, $r.status, $r.note)
  }

  $outDir = Join-Path $Root "data\eval"
  New-Item -ItemType Directory -Force -Path $outDir | Out-Null
  $stamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
  $jsonPath = Join-Path $outDir "architect_smoke_scorecard.json"
  $payload = @{
    stamped_at = $stamp
    stack = @{
      ollama = (Test-HttpUp 11434)
      frontend = (Test-HttpUp 8080)
      eve = (Test-HttpUp 2000)
      pocketbase = (Test-HttpUp 8090)
      extract_worker = $p2Worker
    }
    results = $results
    architect_replies_needed = @(
      "Smoke PASS Phase 1",
      "Smoke PASS Phase 2",
      "Smoke PASS Phase 3",
      "Smoke PASS Phase 4",
      "Smoke PASS Phase 5",
      "Smoke PASS Phase 6",
      "Smoke PASS Phase 8"
    )
    note = "CLI scorecard is evidence for Architect. Goal completes only after Architect replies Smoke PASS in Cursor."
  }
  ($payload | ConvertTo-Json -Depth 6) | Set-Content -Path $jsonPath -Encoding Ascii
  Write-Host ""
  Write-Host "Wrote $jsonPath"
  Write-Host "Next: Start-EMPIRE.bat, then Soft Smoke B in Eve, then reply Smoke PASS Phase N in Cursor."
  exit 0
}

# --- Phase 2 prep (default mode) ---
Write-Host ""
Write-Host "--- Smoke B prep: Structured Extract ---"
Write-Host ("  GGUF present:  {0}" -f (Test-Path $gguf))
Write-Host ("  llama-server:  {0}" -f (Test-Path $llama))

if ($StartWorker -and (Test-Path $gguf) -and (Test-Path $llama)) {
  Write-Host "  Starting structured-extract worker..."
  & (Join-Path $Root "scripts\start-structured-extract.ps1")
  Write-Host "  Wait about 20s for model load, then open Eve."
} else {
  Write-Host "  Worker not auto-started. When ready:"
  Write-Host "    1. Start-EMPIRE.bat"
  Write-Host "    2. .\scripts\start-structured-extract.ps1"
  Write-Host "    3. http://127.0.0.1:8080/eve.html  Toolbelt -> Structured Extract ON"
}

Write-Host ""
Write-Host "Paste this into Eve chat:"
Write-Host "----"
Write-Host "Extract document metadata from: Title: Architect smoke. Author: Architect. Date: 2026-09-07. Tags: smoke, extract. Summary: verifying structured extract limb."
Write-Host "----"
Write-Host "Then: .\scripts\stop-structured-extract.ps1"
Write-Host "Then in Cursor: Smoke PASS Phase 2"
Write-Host ""
Write-Host "Full checklist: docs\ARCHITECT_TEST_CHECKLIST.md"
Write-Host "Tip: .\scripts\architect-smoke-helper.ps1 -Scorecard"
