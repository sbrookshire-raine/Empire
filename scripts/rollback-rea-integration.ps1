# Roll back the REA Bin-1 integration (one command, no state left behind).
#
# Removes everything the 2026-10-21 integration added:
#   - the two Eve tools (rea_skills, claim_ledger) and the MCP adapter
#   - the two Eve skill files (skill-rea-skills, skill-claim-ledger)
#   - the vendored upstream skill tree (vendor/rea-skills)
#   - the vendored claim-ledger MCP server and its .cursor/mcp.json entry
#   - the two capabilities from the manifest and the capability seed
#   - the playbook area entries, the tool docs, and the routing synonyms
#
# Then it re-seeds the capability registry and regenerates the operating
# context, so the governance layer is self-consistent again.
#
# Tracked files are restored with `git checkout`; untracked additions are
# deleted. The script is idempotent: running it twice is harmless.
#
# Usage:  .\scripts\rollback-rea-integration.ps1 [-WhatIf]

param(
    [switch]$WhatIf
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not $Root) { $Root = "C:\EMPIRE" }
Set-Location $Root

$py = Join-Path $Root "venv\Scripts\python.exe"

function Remove-ItemSafe {
    param([string]$Path)
    if (-not (Test-Path $Path)) {
        Write-Host "  skip (absent): $Path"
        return
    }
    if ($WhatIf) {
        Write-Host "  would remove: $Path"
        return
    }
    Remove-Item -Path $Path -Recurse -Force
    Write-Host "  removed: $Path"
}

function Restore-File {
    param([string]$Path)
    if (-not (Test-Path $Path)) {
        Write-Host "  skip (absent): $Path"
        return
    }
    if ($WhatIf) {
        Write-Host "  would restore: $Path"
        return
    }
    git checkout -- $Path
    Write-Host "  restored: $Path"
}

Write-Host "Rollback: REA Bin-1 integration" -ForegroundColor Cyan
Write-Host "================================="
if ($WhatIf) { Write-Host "DRY RUN — nothing will be deleted." -ForegroundColor Yellow }

Write-Host "`n1. Untracked additions" -ForegroundColor Cyan
Remove-ItemSafe (Join-Path $Root "agents\empire-task-agent\agent\tools\rea_skills.ts")
Remove-ItemSafe (Join-Path $Root "agents\empire-task-agent\agent\tools\claim_ledger.ts")
Remove-ItemSafe (Join-Path $Root "agents\empire-task-agent\agent\lib\claim-ledger-mcp.ts")
Remove-ItemSafe (Join-Path $Root "agents\empire-task-agent\agent\skills\skill-rea-skills.md")
Remove-ItemSafe (Join-Path $Root "agents\empire-task-agent\agent\skills\skill-claim-ledger.md")
Remove-ItemSafe (Join-Path $Root "mcp\claim_ledger_mcp.py")
Remove-ItemSafe (Join-Path $Root "vendor\rea-skills")
Remove-ItemSafe (Join-Path $Root "config\eve-capabilities\tool-docs\rea_skills.md")
Remove-ItemSafe (Join-Path $Root "config\eve-capabilities\tool-docs\claim_ledger.md")
Remove-ItemSafe (Join-Path $Root "tests\pipeline\test_rea_skills.py")
Remove-ItemSafe (Join-Path $Root "tests\pipeline\test_claim_ledger.py")
Remove-ItemSafe (Join-Path $Root "docs\rea-integration")

Write-Host "`n2. Tracked files (restored from git)" -ForegroundColor Cyan
Restore-File "agents\empire-task-agent\agent\lib\toolbelt.ts"
Restore-File "config\capability-manifest.json"
Restore-File "config\eve-capabilities\capability-registry.json"
Restore-File "config\eve-capabilities\tool-schema-snapshot.json"
Restore-File "config\eve-capabilities\playbook\reverse-engineering.md"
Restore-File "config\eve-capabilities\route-synonyms.json"
Restore-File "frontend\eve_toolbelt.py"
Restore-File "pipeline\capability_seed.py"
Restore-File ".cursor\mcp.json"
Restore-File "tests\pipeline\test_capability_seed.py"

# NOTE: two files are deliberately NOT restored.
#
# pipeline/eve_operating_context.py — the de-duplication of the proven-tool list
# is an independent prompt-budget fix, not part of this integration, and
# reverting it would push the always-on prompt back over its ceiling.
#
# pipeline/capability_index.py — the UTF-8 stdout guard is an independent
# Windows console fix. Without it `python -m pipeline.capability_index` dies
# with UnicodeEncodeError on a cp1252 console, which blocks the route query
# the new tools depend on. Neither revert is part of this integration.

Write-Host "`n3. Scratch state" -ForegroundColor Cyan
Remove-ItemSafe (Join-Path $Root "eve-output\rea-skills")
Remove-ItemSafe (Join-Path $Root "eve-output\claim-ledger")

if (-not $WhatIf -and (Test-Path $py)) {
    Write-Host "`n4. Re-seed the capability registry" -ForegroundColor Cyan
    $env:PYTHONPATH = $Root
    & $py -m pipeline.capability_seed | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Capability seed failed (exit $LASTEXITCODE)"
        exit 1
    }
    Write-Host "  registry re-seeded"

    Write-Host "`n5. Regenerate the operating context" -ForegroundColor Cyan
    & $py -m pipeline.eve_operating_context | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Operating context regeneration failed (exit $LASTEXITCODE)"
        exit 1
    }
    Write-Host "  operating context regenerated"
}

Write-Host ""
if ($WhatIf) {
    Write-Host "DRY RUN complete. Re-run without -WhatIf to apply." -ForegroundColor Yellow
} else {
    Write-Host "Rollback complete. The REA Bin-1 integration is removed." -ForegroundColor Green
}
exit 0
