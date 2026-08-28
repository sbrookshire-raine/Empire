<#
.SYNOPSIS
    Idempotently attach the Cognee NTFS VHDX and ensure it is mounted at drive V:.

.DESCRIPTION
    Attaches I:\EMPIRE_VHDX\empire_cognee.vhdx and guarantees it is reachable at V:\.
    Safe to run repeatedly:
      - If V:\ is already present and the VHDX is attached, does nothing.
      - Otherwise mounts the image and assigns drive letter V.

    On machines with Hyper-V enabled, Mount-DiskImage returns Access Denied.
    This script prefers Mount-VHD (Hyper-V) and falls back to Mount-DiskImage.

    Called from scripts\start-stack.ps1 and scripts\roll-in.ps1.
    Also intended to run at logon via Task Scheduler.

.NOTES
    REQUIRES ADMINISTRATOR ELEVATION.

    Auto-mount at logon with highest privileges (run ONCE as admin):

      schtasks /Create /TN "EMPIRE Mount Cognee VHDX" /RL HIGHEST /SC ONLOGON /F /TR 'powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\EMPIRE\scripts\mount-cognee-vhdx.ps1"'
#>

param(
    [switch]$Detach
)

$ErrorActionPreference = 'Stop'

$VhdxPath    = 'I:\EMPIRE_VHDX\empire_cognee.vhdx'
$DriveLetter = 'V'
$DriveRoot   = 'V:\'
$CogneeRoot  = 'V:\Cognee'

function Test-IsAdmin {
    $id = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($id)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Test-HyperVMountAvailable {
    if (-not (Get-Module -ListAvailable -Name Hyper-V)) {
        return $false
    }
    Import-Module Hyper-V -ErrorAction SilentlyContinue
    return [bool](Get-Command Mount-VHD -ErrorAction SilentlyContinue)
}

function Get-EmpireVhdDiskNumber {
    if (Test-HyperVMountAvailable) {
        $vhd = Get-VHD -Path $VhdxPath -ErrorAction SilentlyContinue
        if ($vhd -and $vhd.Attached -and $null -ne $vhd.DiskNumber) {
            return [int]$vhd.DiskNumber
        }
    }
    $img = Get-DiskImage -ImagePath $VhdxPath -ErrorAction SilentlyContinue
    if ($img -and $img.Attached) {
        $disk = $img | Get-Disk -ErrorAction SilentlyContinue
        if ($disk) { return [int]$disk.Number }
    }
    return $null
}

function Set-EmpireDriveLetter {
    param([int]$DiskNumber)
    if (Test-Path -LiteralPath $DriveRoot) { return }

    try {
        Set-Disk -Number $DiskNumber -IsOffline $false -ErrorAction SilentlyContinue
        Set-Disk -Number $DiskNumber -IsReadOnly $false -ErrorAction SilentlyContinue
    }
    catch { }

    $part = Get-Partition -DiskNumber $DiskNumber |
        Where-Object { $_.Type -ne 'Reserved' -and $_.Size -gt 0 } |
        Sort-Object -Property Size -Descending |
        Select-Object -First 1
    if (-not $part) {
        throw 'No usable partition found on the Cognee VHDX.'
    }
    if ($part.DriveLetter -eq $DriveLetter) { return }

    if (Test-Path -LiteralPath $DriveRoot) {
        Get-Partition -DriveLetter $DriveLetter -ErrorAction SilentlyContinue |
            Remove-PartitionAccessPath -AccessPath $DriveRoot -ErrorAction SilentlyContinue
    }
    Set-Partition -DiskNumber $part.DiskNumber -PartitionNumber $part.PartitionNumber -NewDriveLetter $DriveLetter
}

if (-not (Test-IsAdmin)) {
    Write-Warning 'mount-cognee-vhdx: elevation required. Run as admin, or use .\scripts\start-stack.ps1 (it will prompt UAC).'
    exit 2
}

if (-not (Test-Path -LiteralPath $VhdxPath)) {
    Write-Warning 'VHDX not found at I:\EMPIRE_VHDX\empire_cognee.vhdx. Plug in the T7 (I:) first.'
    exit 3
}

if ($Detach) {
    Write-Host ('Detaching {0} ...' -f $VhdxPath)
    if (Test-HyperVMountAvailable) {
        Dismount-VHD -Path $VhdxPath -ErrorAction SilentlyContinue
    }
    Dismount-DiskImage -ImagePath $VhdxPath -ErrorAction SilentlyContinue | Out-Null
    Write-Host 'Detached.'
    exit 0
}

if ((Test-Path -LiteralPath $DriveRoot) -and (Test-Path -LiteralPath $CogneeRoot)) {
    Write-Host 'Cognee VHDX already mounted at V: - nothing to do.'
    exit 0
}

$vds = Get-Service -Name vds -ErrorAction SilentlyContinue
if ($vds -and $vds.Status -ne 'Running') {
    Start-Service vds -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 1
}

$attachedViaHyperV = $false
if (Test-HyperVMountAvailable) {
    $vhd = Get-VHD -Path $VhdxPath -ErrorAction SilentlyContinue
    if (-not ($vhd -and $vhd.Attached)) {
        Write-Host ('Attaching {0} via Mount-VHD ...' -f $VhdxPath)
        Mount-VHD -Path $VhdxPath
        Start-Sleep -Milliseconds 800
    }
    $attachedViaHyperV = $true
}

if (-not $attachedViaHyperV) {
    $img = Get-DiskImage -ImagePath $VhdxPath -ErrorAction SilentlyContinue
    if (-not ($img -and $img.Attached)) {
        Write-Host ('Attaching {0} via Mount-DiskImage ...' -f $VhdxPath)
        Mount-DiskImage -ImagePath $VhdxPath | Out-Null
        Start-Sleep -Milliseconds 800
    }
}

$diskNumber = Get-EmpireVhdDiskNumber
if ($null -eq $diskNumber) {
    throw 'VHDX attached but disk number was not found.'
}
Set-EmpireDriveLetter -DiskNumber $diskNumber

if (Test-Path -LiteralPath $DriveRoot) {
    New-Item -ItemType Directory -Force -Path $CogneeRoot | Out-Null
    Write-Host ('Cognee VHDX mounted at V: (root: {0}).' -f $CogneeRoot)
}
else {
    throw 'Failed to expose the Cognee VHDX at V:.'
}
