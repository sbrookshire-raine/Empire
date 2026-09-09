# Inventory + Build1 3-Bin triage for SKILL.md trees (local Tool Forge).
param(
    [string[]]$Paths = @(),
    [switch]$NoDefaultSkills
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$py = Join-Path $root "venv\Scripts\python.exe"
$args = @("-m", "pipeline.skill_compiler")
if ($NoDefaultSkills) { $args += "--no-default-skills" }
if ($Paths.Count -gt 0) { $args += $Paths }
& $py @args
