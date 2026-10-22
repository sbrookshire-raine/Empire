# Mechanic green gate - run before handing UX smoke to the Architect.
# Default: unit tests + wiki extract CLI battery + verify-stack.
# -Live: also run the live capability tier (real Eve tool calls on the wire).
#        The live tier is ENFORCED: if it was requested and did not run, the
#        gate fails. A silent "live verification never ran" is how a green
#        gate came to mean "nothing was actually proven".
# -Full: also verify-eve-workbench (live Cognee + Eve chat).
param(
    [switch]$Full,
    [switch]$Live,
    [switch]$SkipStack
)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not $Root) { $Root = "C:\EMPIRE" }
Set-Location $Root
$py = Join-Path $Root "venv\Scripts\python.exe"
if (-not (Test-Path $py)) {
    Write-Error "Missing venv python at $py"
}
$env:PYTHONPATH = $Root
$env:PYTHONIOENCODING = "utf-8"

$failed = 0

function Invoke-Step {
    param([string]$Name, [scriptblock]$Block)
    Write-Host ""
    Write-Host "=== $Name ===" -ForegroundColor Cyan
    & $Block
    if ($LASTEXITCODE -ne 0) {
        Write-Host "FAIL $Name (exit $LASTEXITCODE)" -ForegroundColor Red
        $script:failed += 1
    } else {
        Write-Host "PASS $Name" -ForegroundColor Green
    }
}

Invoke-Step "baseline audit (L1-L4)" {
    & (Join-Path $Root "scripts\baseline-audit.ps1") -Json
}

Invoke-Step "unit tests" {
    & $py -c @"
import unittest, io, sys
sys.path.insert(0, r'$Root')
loader = unittest.TestLoader()
suite = loader.discover('tests', pattern='test_*.py', top_level_dir='.')
result = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
print(f'{suite.countTestCases()} tests fail={len(result.failures)} err={len(result.errors)}')
for t, tb in result.failures + result.errors:
    print('X', t.id())
raise SystemExit(0 if result.wasSuccessful() else 1)
"@
}

Invoke-Step "verify-capabilities (offline)" {
    & (Join-Path $Root "scripts\verify-capabilities.ps1")
}

# The live tier proves real Eve tool calls on the wire. It is separate from the
# offline tier because it needs the stack up (Ollama + Eve + frontend), and it
# is ENFORCED when requested: the report must say the live tier actually ran.
# Without that check, "-Live" could quietly do nothing and still report green.
$liveReport = Join-Path $Root "tmp\capability_verification_report.json"
if ($Live) {
    # Delete the report first: a stale one from an earlier run would carry
    # live_ran=true and make this check pass without the live tier ever
    # having run in *this* gate.
    if (Test-Path $liveReport) {
        Remove-Item $liveReport -Force
    }
    Invoke-Step "verify-capabilities (live)" {
        & (Join-Path $Root "scripts\verify-capabilities.ps1") -Live
    }
    $liveRan = $false
    if (Test-Path $liveReport) {
        try {
            $parsed = Get-Content $liveReport -Raw -Encoding UTF8 | ConvertFrom-Json
            $liveRan = [bool]$parsed.live_ran
        }
        catch {
            $liveRan = $false
        }
    }
    if (-not $liveRan) {
        Write-Host ""
        Write-Host "FAIL live verification tier did not run (report has live_ran=false)." -ForegroundColor Red
        Write-Host "     The live tier needs the stack up: .\scripts\start-stack.ps1" -ForegroundColor Yellow
        $failed += 1
    }
    else {
        Write-Host "PASS live verification tier ran" -ForegroundColor Green
    }
}

Invoke-Step "capability governance (fail-closed)" {
    & $py -c @"
import json, sys
from pipeline import capability_registry as cr
from pipeline import capability_seed as cs
# Verify every canonical capability against the on-disk snapshot. A missing
# snapshot or drifted schema reports fail-closed (exit 1).
missing = []
for cap in cs.canonical_capabilities():
    res = cr.verify_capability(cap['capability_id'])
    if not res.get('ok'):
        missing.append((cap['capability_id'], res.get('reason'), res.get('mismatches')))
print(f'capabilities verified={len(cs.canonical_capabilities())} fail={len(missing)}')
for cid, reason, mm in missing:
    print('X', cid, reason, mm)
raise SystemExit(0 if not missing else 1)
"@
}

# LEGO contract conformance: bricks, adapters, library paths, prompt budget.
Invoke-Step "LEGO contract (check-legos)" {
    & $py (Join-Path $Root "scripts\check-legos.py")
}

# Foundation registry: measures how far dataset eve_core (the set chat recall prefers) is from the
# deliberate allowlist. ADVISORY until the curated rebuild lands - see docs/MEMORY_GOVERNANCE.md
# section 7 step 5. Drop --advisory after the rebuild to make violations fatal.
Invoke-Step "foundation registry (check-foundation, advisory)" {
    & $py (Join-Path $Root "scripts\check-foundation.py") --advisory
}

# Lens A infrastructure checks: dependency hygiene, lint baseline, secret scan. Dev-time only - none of
# these tools are reachable by Eve and none cost prompt tokens. Advisory until the findings are triaged
# (docs/audits/2026-09-26-infra-adoption.md); pass -Strict to make deptry/gitleaks block.
Invoke-Step "infra checks (deptry/ruff/gitleaks, advisory)" {
    & (Join-Path $Root "scripts\infra-checks.ps1")
}

# The wiki extract battery needs the Title DNS corpus. Ask the RUNTIME where
# that corpus is (scripts/wiki-index-path.py -> pipeline.wiki_ops_paths) instead
# of hardcoding a drive letter: the old hardcoded I: check made the gate skip
# the battery whenever the T7 was not mounted, even though the runtime was
# serving wiki lookups from the same corpus on D:. A green gate that skipped a
# real check proved nothing about the wiki limb.
$wikiTitleIndex = ""
try {
    $resolved = & $py (Join-Path $Root "scripts\wiki-index-path.py") 2>$null
    if ($resolved) { $wikiTitleIndex = ($resolved | Select-Object -First 1).Trim() }
} catch {
    $wikiTitleIndex = ""
}
if ($wikiTitleIndex -and (Test-Path $wikiTitleIndex)) {
    Write-Host ""
    Write-Host "wiki corpus: $wikiTitleIndex" -ForegroundColor DarkGray
    Invoke-Step "wiki extract battery (CLI)" {
        & $py (Join-Path $Root "scripts\wiki_extract_battery.py")
    }
} else {
    Write-Host ""
    Write-Host "SKIP wiki extract battery (no Title DNS corpus found — plug T7 or run build-wiki-title-index.ps1)" -ForegroundColor Yellow
}

# The browser-logic harness stubs the workbench JS in node. It is the only gate on
# eve-workbench.js behaviour (transcript, stream events, mode switch, chat history), and it had
# rotted unnoticed while nothing ran it — found 2026-09-24 (missing browser stubs, a stale
# fetch-count assertion, and a model-picker test left behind by the mode-picker rewrite).
$nodeExe = (Get-Command node -ErrorAction SilentlyContinue).Source
if ($nodeExe) {
    Invoke-Step "workbench UI harness (node)" {
        & $nodeExe (Join-Path $Root "tests\frontend\eve_workbench_harness.js")
    }
} else {
    Write-Host ""
    Write-Host "SKIP workbench UI harness (node not on PATH)" -ForegroundColor Yellow
}

if (-not $SkipStack) {
    Invoke-Step "verify-stack" {
        & $py (Join-Path $Root "scripts\verify-stack.py")
    }
    # The operating contract's own measurement: services, model window, prompt layer.
    # Fails when the running stack drifts from docs/OPERATING_CONTRACT.md.
    Invoke-Step "operating contract (audit-empire)" {
        & $py (Join-Path $Root "scripts\audit-empire.py")
    }
}

if ($Full) {
    Invoke-Step "verify-eve-workbench" {
        & $py (Join-Path $Root "scripts\verify-eve-workbench.py")
    }
}

Write-Host ""
if ($failed -gt 0) {
    Write-Host "mechanic-green: $failed step(s) failed - do not hand to Architect yet." -ForegroundColor Red
    exit 1
}
Write-Host "mechanic-green: all steps passed. Architect UX smoke is optional." -ForegroundColor Green
exit 0
