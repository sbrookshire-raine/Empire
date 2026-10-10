<#
.SYNOPSIS
    Restore the Cognee NTFS VHDX to a live path (default E:\EMPIRE_VHDX) from hub backup.

.DESCRIPTION
    After T7 reformat or I: becoming Google Drive, I:\EMPIRE_VHDX is gone and V: will not mount.
    This copies the 2026-09-27 hub snapshot to E:\EMPIRE_VHDX\empire_cognee.vhdx (or -Destination),
    then you run mount-cognee-vhdx.ps1 as Administrator.

    Does NOT require admin. Mounting V: does.

.EXAMPLE
    .\scripts\restore-cognee-vhdx.ps1
    powershell -ExecutionPolicy Bypass -File C:\EMPIRE\scripts\mount-cognee-vhdx.ps1
#>

param(
    [string]$Source,
    [string]$Destination,
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'lib\cognee-vhdx-config.ps1')

if (-not $Source) {
    $Source = Get-EmpireCogneeVhdxHubSnapshot
}
if (-not $Destination) {
    $Destination = 'E:\EMPIRE_VHDX\empire_cognee.vhdx'
}

if (-not (Test-Path -LiteralPath $Source)) {
    throw "Hub snapshot missing: $Source. See docs/COGNEE_VHDX.md and E:\EMPIRE_HUB\00_CORE\state\cognee_vhdx\"
}

$destDir = Split-Path -Parent $Destination
New-Item -ItemType Directory -Force -Path $destDir | Out-Null

if ((Test-Path -LiteralPath $Destination) -and -not $Force) {
    $srcLen = (Get-Item -LiteralPath $Source).Length
    $dstLen = (Get-Item -LiteralPath $Destination).Length
    if ($srcLen -eq $dstLen) {
        Write-Host "Live VHDX already present ($Destination, $([math]::Round($dstLen/1GB,2)) GB). Use -Force to recopy."
        Write-Host "Next (elevated): .\scripts\mount-cognee-vhdx.ps1"
        exit 0
    }
    Write-Warning "Destination exists but size differs (src=$srcLen dst=$dstLen). Use -Force to overwrite."
    exit 1
}

Write-Host "Copying Cognee VHDX snapshot..."
Write-Host "  From: $Source"
Write-Host "  To:   $Destination"
Copy-Item -LiteralPath $Source -Destination $Destination -Force
Write-Host "Done. Next step (Run as Administrator):"
Write-Host '  powershell -NoProfile -ExecutionPolicy Bypass -File "C:\EMPIRE\scripts\mount-cognee-vhdx.ps1"'
