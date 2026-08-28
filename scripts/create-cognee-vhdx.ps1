<#
.SYNOPSIS
    One-time creation of the NTFS VHDX that hosts Cognee's heavy graph/vector DB.

.DESCRIPTION
    EMPIRE hard rule: keep heavy storage off the C: Core Runtime drive.
    The 4TB I: drive is exFAT; Cognee DBs (lancedb/kuzu/sqlite) need NTFS.
    This script creates a dynamically expanding NTFS VHDX on I: and mounts it at V:.

    VHDX file : I:\EMPIRE_VHDX\empire_cognee.vhdx
    Type      : dynamically expanding
    Max size  : 2 TB (2097152 MB)
    Filesystem: NTFS, label EMPIRE_COGNEE
    Mount     : drive letter V:
    Cognee root: V:\Cognee

    Weaviate export path I:\EMPIRE_DATA\weaviate_dump is never touched.

.NOTES
    REQUIRES ADMINISTRATOR ELEVATION.
    Run once. Afterwards use scripts\mount-cognee-vhdx.ps1 to re-attach.

    Elevated command:
      powershell -NoProfile -ExecutionPolicy Bypass -File "C:\EMPIRE\scripts\create-cognee-vhdx.ps1"
#>

$ErrorActionPreference = 'Stop'

$VhdxDir     = 'I:\EMPIRE_VHDX'
$VhdxPath    = 'I:\EMPIRE_VHDX\empire_cognee.vhdx'
$DriveLetter = 'V'
$MaxSizeMB   = 2097152
$Label       = 'EMPIRE_COGNEE'
$CogneeRoot  = 'V:\Cognee'
$DriveRoot   = 'V:\'

function Test-IsAdmin {
    $id = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($id)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

if (-not (Test-IsAdmin)) {
    Write-Error @'
This script must be run as Administrator (diskpart create/attach/format require elevation).
Right-click PowerShell -> Run as administrator, then run:
  powershell -NoProfile -ExecutionPolicy Bypass -File "C:\EMPIRE\scripts\create-cognee-vhdx.ps1"
'@
    exit 1
}

New-Item -ItemType Directory -Force -Path $VhdxDir | Out-Null

if (Test-Path -LiteralPath $VhdxPath) {
    Write-Host ('VHDX already exists at {0} - skipping create. Use mount-cognee-vhdx.ps1 to attach.' -f $VhdxPath)
}
else {
    Write-Host ('Creating NTFS VHDX (dynamically expanding, max {0} MB) at {1} ...' -f $MaxSizeMB, $VhdxPath)

    # Single-quoted here-string: literal content only. Fill placeholders after.
    $diskpartTemplate = @'
create vdisk file="__VHDX_PATH__" maximum=__MAX_MB__ type=expandable
select vdisk file="__VHDX_PATH__"
attach vdisk
create partition primary
format fs=ntfs quick label=__LABEL__
assign letter=__LETTER__
'@

    $diskpartScript = $diskpartTemplate.Replace('__VHDX_PATH__', $VhdxPath)
    $diskpartScript = $diskpartScript.Replace('__MAX_MB__', [string]$MaxSizeMB)
    $diskpartScript = $diskpartScript.Replace('__LABEL__', $Label)
    $diskpartScript = $diskpartScript.Replace('__LETTER__', $DriveLetter)

    $tmp = Join-Path $env:TEMP 'empire-create-cognee-vhdx.txt'
    Set-Content -Path $tmp -Value $diskpartScript -Encoding Ascii
    try {
        & diskpart.exe /s $tmp
        if ($LASTEXITCODE -ne 0) {
            throw ('diskpart exited with code {0}' -f $LASTEXITCODE)
        }
    }
    finally {
        Remove-Item -LiteralPath $tmp -Force -ErrorAction SilentlyContinue
    }
}

if (-not (Test-Path -LiteralPath $DriveRoot)) {
    Write-Error 'Drive V: is not available after attach. Check diskpart output above.'
    exit 1
}

New-Item -ItemType Directory -Force -Path $CogneeRoot | Out-Null

Write-Host ''
Write-Host ('Done. VHDX mounted at V: and {0} is ready.' -f $CogneeRoot)
Write-Host 'Next:'
Write-Host ('  1. Cognee is already configured to use {0} (see config/cognee.env and mcp.json).' -f $CogneeRoot)
Write-Host '  2. Register auto-mount at logon (elevated PowerShell, copy-paste-safe):'
Write-Host '     schtasks /Create /TN "EMPIRE Mount Cognee VHDX" /RL HIGHEST /SC ONLOGON /F /TR ''powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\EMPIRE\scripts\mount-cognee-vhdx.ps1"'''
