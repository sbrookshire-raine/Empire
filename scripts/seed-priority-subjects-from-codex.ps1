<#
.SYNOPSIS
    Seed ranked priority subjects from Master Codex (planning only — no Wikipedia ingest).

.PARAMETER DryRun
    Print would-add count without writing.

.PARAMETER CodexPath
    Override Codex markdown path.

.PARAMETER SubjectsPath
    Override priority_subjects.json path.
#>
param(
    [switch]$DryRun,
    [string]$CodexPath = "",
    [string]$SubjectsPath = ""
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$py = Join-Path $Root "venv\Scripts\python.exe"
$env:PYTHONPATH = $Root

$argsList = @("-m", "pipeline.wiki_codex_seed")
if ($DryRun) { $argsList += "--dry-run" }
if ($CodexPath) { $argsList += @("--codex-path", $CodexPath) }
if ($SubjectsPath) { $argsList += @("--subjects-path", $SubjectsPath) }

& $py @argsList
exit $LASTEXITCODE
