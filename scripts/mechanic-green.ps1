# Mechanic green gate - run before handing UX smoke to the Architect.
# Default: unit tests + wiki extract CLI battery + verify-stack.
# -Full: also verify-eve-workbench (live Cognee + Eve chat).
param(
    [switch]$Full,
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

Invoke-Step "wiki extract battery (CLI)" {
    & $py (Join-Path $Root "scripts\wiki_extract_battery.py")
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
