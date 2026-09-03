#Requires -Version 5.1
<#
.SYNOPSIS
  Build the verifiable projects catalog from workbench harvest artifacts.
#>
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root "venv\Scripts\python.exe"
$env:PYTHONPATH = $Root
& $Python -c "from frontend.project_catalog import save_project_catalog; c=save_project_catalog(); print('Projects:', c.get('project_count'), '| eve_core:', c.get('in_eve_core_count'), '| flattened:', c.get('flattened_count'))"
