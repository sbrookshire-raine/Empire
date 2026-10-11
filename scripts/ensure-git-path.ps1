#Requires -Version 5.1
<#
.SYNOPSIS
  Ensure git.exe is on PATH for this session (and optionally persist for the user).
#>
param([switch]$PersistUser)

$ErrorActionPreference = "Stop"
. (Join-Path $PSScriptRoot "lib\git-path.ps1")

if (-not (Ensure-GitOnPath)) {
    exit 1
}

if ($PersistUser) {
    $gitCmd = (Get-Command git).Source
    $gitDir = Split-Path -Parent $gitCmd
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($userPath -notlike "*$([regex]::Escape($gitDir))*") {
        [Environment]::SetEnvironmentVariable("Path", "$gitDir;$userPath", "User")
        Write-Host "Persisted Git cmd to user PATH: $gitDir"
        Write-Host "Open a new terminal for other apps to see it."
    }
    else {
        Write-Host "User PATH already contains Git cmd."
    }
}

Write-Host "OK: $(git --version)"
