#Requires -Version 5.1
<#
  Prepend Git for Windows to the current process PATH (clone in intake_to_lego study depth).
#>
function Add-GitToProcessPath {
    if (Get-Command git -ErrorAction SilentlyContinue) {
        return (Get-Command git).Source
    }
    $candidates = @(
        (Join-Path ${env:ProgramFiles} "Git\cmd")
        (Join-Path ${env:ProgramFiles(x86)} "Git\cmd")
        (Join-Path $env:LOCALAPPDATA "Programs\Git\cmd")
    )
    foreach ($dir in $candidates) {
        if (-not $dir -or -not (Test-Path $dir)) { continue }
        if ($env:PATH -notlike "*$([regex]::Escape($dir))*") {
            $env:PATH = "$dir;$env:PATH"
        }
        $git = Join-Path $dir "git.exe"
        if (Test-Path $git) {
            return $git
        }
    }
    return $null
}

function Ensure-GitOnPath {
    param([switch]$Quiet)
    $resolved = Add-GitToProcessPath
    if ($resolved) {
        if (-not $Quiet) {
            Write-Host "  Git on PATH: $resolved"
        }
        return $true
    }
    if (-not $Quiet) {
        Write-Warning "Git not found. Install Git for Windows or add Git\cmd to PATH (needed for study-depth repo clone)."
    }
    return $false
}
