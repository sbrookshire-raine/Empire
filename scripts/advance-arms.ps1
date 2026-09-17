# Eve governed-arms phase runner (auto-advance gate).
#
# Runs each phase gate in order. Stops at the first red gate by default.
# With -Continue it auto-proceeds past green gates so no user input is needed
# to reach the first failing phase. `mechanic-green.ps1` remains the final
# pre-Architect gate.
#
# Phase gates:
#   P0  governance  : capability registry seeded + fail-closed verify
#   P1  evidence    : workspace_search / query_data / read_document
#   P2  artifact    : create_spreadsheet / author_code / python_verify
#   P3  switchboard : service plan + headroom + tenant serialization
#   P4  isolation   : url_broker SSRF + trust_gate prompt-injection
#
# Usage:
#   .\scripts\advance-arms.ps1           # run all gates, stop at first red
#   .\scripts\advance-arms.ps1 -Continue # auto-proceed past green gates

param(
    [switch]$Continue
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not $Root) { $Root = "C:\EMPIRE" }
Set-Location $Root

$py = Join-Path $Root "venv\Scripts\python.exe"
if (-not (Test-Path $py)) {
    Write-Error "Missing venv python at $py"
    exit 1
}
$env:PYTHONPATH = $Root
$env:PYTHONIOENCODING = "utf-8"

# Ordered gate table. Each gate is `id|label|script block label` keyed below.
$gates = @(
    @{ Id = "P0"; Label = "governance: capability registry seeded + fail-closed" },
    @{ Id = "P1"; Label = "evidence arms: search / query / read" },
    @{ Id = "P2"; Label = "artifact arms: spreadsheet / author / verify" },
    @{ Id = "P3"; Label = "switchboard: plan + headroom + tenant serialization" },
    @{ Id = "P4"; Label = "isolation: url_broker SSRF + trust_gate" }
)

function Invoke-Gate([string]$GateId) {
    switch ($GateId) {
        "P0" {
            # Seed must be runnable and every canonical capability must verify.
            & $py -m unittest tests.pipeline.test_capability_seed tests.pipeline.test_capability_registry 2>&1 | Out-Null
            return $LASTEXITCODE
        }
        "P1" {
            & $py -m unittest tests.pipeline.test_evidence_arms 2>&1 | Out-Null
            return $LASTEXITCODE
        }
        "P2" {
            & $py -m unittest tests.pipeline.test_artifact_arms 2>&1 | Out-Null
            return $LASTEXITCODE
        }
        "P3" {
            & $py -m unittest tests.pipeline.test_switchboard 2>&1 | Out-Null
            return $LASTEXITCODE
        }
        "P4" {
            & $py -m unittest tests.pipeline.test_url_broker tests.pipeline.test_trust_gate 2>&1 | Out-Null
            return $LASTEXITCODE
        }
        default {
            Write-Host "Unknown gate: $GateId" -ForegroundColor Red
            return 1
        }
    }
}

Write-Host "EMPIRE governed-arms phase runner" -ForegroundColor Cyan
Write-Host "================================="
if ($Continue) {
    Write-Host "Auto-advance mode: proceeding past green gates."
}

$firstRed = $false
$passed = 0
$failed = 0

foreach ($gate in $gates) {
    Write-Host ""
    Write-Host "--- $($gate.Id): $($gate.Label) ---" -ForegroundColor Cyan
    $code = Invoke-Gate $gate.Id
    if ($code -eq 0) {
        Write-Host "[PASS] $($gate.Id) $($gate.Label)" -ForegroundColor Green
        $passed++
    } else {
        Write-Host "[FAIL] $($gate.Id) $($gate.Label) (exit $code)" -ForegroundColor Red
        $failed++
        $firstRed = $true
        break
    }
}

Write-Host ""
if ($failed -gt 0) {
    Write-Host "advance-arms: stopped at first red gate ($($gate.Id)). Fix and re-run." -ForegroundColor Red
    exit 1
}
Write-Host "advance-arms: all $passed phase gates passed. Run mechanic-green for the pre-Architect gate." -ForegroundColor Green
exit 0
