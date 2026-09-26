#Requires -Version 5.1
<#
.SYNOPSIS
  Lens A infrastructure checks — dev-time only. Eve can never reach these tools.
.DESCRIPTION
  Three defect classes we have already been bitten by (docs/LENS_A_LANDSCAPE.md):

    deptry   undeclared/unused dependencies   <- docling was installed but absent from requirements.txt
    ruff     lint baseline                    <- the Python surface had no baseline at all
    gitleaks secret scan                      <- the secrets policy existed; the mechanism did not

  Advisory by default: findings are reported and written to eve-audit\ for review, and a missing tool is a
  SKIP, never a failure (same pattern as the node harness step). -Strict makes deptry and gitleaks fail.
  None of these tools add runtime cost: no prompt tokens, no VRAM, no limb.
.EXAMPLE
  .\scripts\infra-checks.ps1
.EXAMPLE
  .\scripts\infra-checks.ps1 -Strict
#>
param([switch]$Strict)

$ErrorActionPreference = 'Continue'
$Root = Split-Path -Parent $PSScriptRoot
$Py = Join-Path $Root 'venv\Scripts\python.exe'
$Out = Join-Path $Root 'eve-audit'
New-Item -ItemType Directory -Force -Path $Out | Out-Null
$failed = @()

function Resolve-EmpireTool([string]$Name) {
    # PATH first, then the winget package tree (winget installs do not refresh this shell's PATH).
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    $base = Join-Path $env:LOCALAPPDATA 'Microsoft\WinGet\Packages'
    if (Test-Path $base) {
        $hit = Get-ChildItem $base -Recurse -Filter "$Name*.exe" -ErrorAction SilentlyContinue |
            Select-Object -First 1
        if ($hit) { return $hit.FullName }
    }
    return $null
}

Write-Host ''
Write-Host '=== infra: dependency hygiene (deptry) ===' -ForegroundColor Cyan
if (Test-Path $Py) {
    $log = Join-Path $Out 'deptry.txt'
    & $Py -m deptry $Root --requirements-files (Join-Path $Root 'requirements.txt') *> $log
    if ($LASTEXITCODE -eq 0) {
        Write-Host '  clean' -ForegroundColor Green
    } else {
        $issues = (Select-String -Path $log -Pattern 'DEP\d{3}' | Measure-Object).Count
        Write-Host "  $issues issue(s) -> eve-audit\deptry.txt" -ForegroundColor Yellow
        if ($Strict) { $failed += 'deptry' }
    }
} else {
    Write-Host 'SKIP deptry (no venv python)' -ForegroundColor Yellow
}

Write-Host ''
Write-Host '=== infra: lint baseline (ruff) ===' -ForegroundColor Cyan
if (Test-Path $Py) {
    $log = Join-Path $Out 'ruff.txt'
    & $Py -m ruff check $Root --exit-zero --statistics *> $log
    # Parse the --statistics table ('162<TAB>FURB167<TAB>[*] regex-flag-alias'): the first column summed
    # is the finding total. First version matched '^\d+\s+\S' and reported "1 rule" against a real
    # ~30-rule table - the counter was wrong, not the tool (fixed 2026-09-26).
    $stat = @(Get-Content $log -ErrorAction SilentlyContinue | Where-Object { $_ -match '^\d+' })
    $total = ($stat | ForEach-Object { [int](($_ -split '\s+')[0]) } | Measure-Object -Sum).Sum
    if ($stat.Count -eq 0) {
        Write-Host '  clean' -ForegroundColor Green
    } else {
        Write-Host "  $total finding(s) across $($stat.Count) rule(s) -> eve-audit\ruff.txt" -ForegroundColor Yellow
    }
} else {
    Write-Host 'SKIP ruff (no venv python)' -ForegroundColor Yellow
}

Write-Host ''
Write-Host '=== infra: secret scan (gitleaks) ===' -ForegroundColor Cyan
$gl = Resolve-EmpireTool 'gitleaks'
if ($gl) {
    $report = Join-Path $Out 'gitleaks.json'
    & $gl detect --source $Root --redact --no-banner --report-format json --report-path $report *> (Join-Path $Out 'gitleaks.txt')
    if ($LASTEXITCODE -eq 0) {
        Write-Host '  no leaks' -ForegroundColor Green
    } else {
        $leaks = @()
        if (Test-Path $report) { $leaks = @(Get-Content $report -Raw | ConvertFrom-Json) }
        $byRule = ($leaks | Group-Object RuleID | Sort-Object Count -Descending |
            Select-Object -First 3 | ForEach-Object { "$($_.Name)=$($_.Count)" }) -join ' '
        Write-Host "  $(@($leaks).Count) finding(s): $byRule -> eve-audit\gitleaks.json" -ForegroundColor Yellow
        if ($Strict) { $failed += 'gitleaks' }
    }
} else {
    Write-Host 'SKIP gitleaks (winget install Gitleaks.Gitleaks)' -ForegroundColor Yellow
}

Write-Host ''
if ($failed.Count) {
    Write-Host "infra-checks STRICT: $($failed -join ', ') failed" -ForegroundColor Red
    exit 1
}
Write-Host 'infra-checks: advisory pass (findings recorded in eve-audit\, nothing blocked)' -ForegroundColor Green
exit 0
