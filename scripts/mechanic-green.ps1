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

Invoke-Step "wiki extract battery (CLI)" {
    & $py (Join-Path $Root "scripts\wiki_extract_battery.py")
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
