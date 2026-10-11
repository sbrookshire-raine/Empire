#Requires -Version 5.1
<#
.SYNOPSIS
  Read optional limb categories from the Workbench toolbelt (LocalAppData or repo fallback).
#>
function Get-EmpireToolbeltActive {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepoRoot
    )
    $candidates = @(
        (Join-Path $env:LOCALAPPDATA "EMPIRE\eve-toolbelt.json")
        (Join-Path $RepoRoot "config\eve-toolbelt.json")
    )
    foreach ($cfg in $candidates) {
        if (-not (Test-Path -LiteralPath $cfg)) {
            continue
        }
        try {
            $raw = Get-Content -LiteralPath $cfg -Raw -Encoding UTF8 | ConvertFrom-Json
            if ($null -eq $raw.active_tools) {
                return @()
            }
            $out = @()
            foreach ($item in @($raw.active_tools)) {
                $s = [string]$item
                if ($s.Trim()) {
                    $out += $s.Trim()
                }
            }
            return $out
        }
        catch {
            continue
        }
    }
    return @()
}
