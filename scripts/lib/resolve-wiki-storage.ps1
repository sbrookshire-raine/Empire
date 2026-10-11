#Requires -Version 5.1
<#
  Resolve Wikipedia storage paths when I: is not the T7 (e.g. Google Drive on I:).
  Sets EMPIRE_WIKI_REPORTS_ROOT and EMPIRE_WEAVIATE_ARCHIVE on the current process.
#>

function Resolve-WeaviateArchivePath {
    param(
        [string]$Preferred = ""
    )
    if ($Preferred -and (Test-Path -LiteralPath $Preferred)) {
        return $Preferred
    }
    $fromEnv = [string]$env:EMPIRE_WEAVIATE_ARCHIVE
    $fromEnv = $fromEnv.Trim()
    if ($fromEnv -and (Test-Path -LiteralPath $fromEnv)) {
        return $fromEnv
    }
    $candidates = @(
        "I:\weaviate_v2_archive\weaviate",
        "D:\weaviate_v2_archive\weaviate"
    )
    foreach ($path in $candidates) {
        if (Test-Path -LiteralPath $path) {
            return $path
        }
    }
    return $candidates[0]
}

function Test-EmpireWikiDataOnDriveI {
    if (Test-Path -LiteralPath "I:\EMPIRE_DATA") {
        return $true
    }
    if (Test-Path -LiteralPath "I:\weaviate_v2_archive") {
        return $true
    }
    $indexOnI = "I:\EMPIRE_DATA\wiki-reports\2026\title-index.sqlite"
    if (Test-Path -LiteralPath $indexOnI) {
        return $true
    }
    return $false
}

function Resolve-WikiReportsRoot {
    param(
        [string]$Year = "2026"
    )
    $fromEnv = [string]$env:EMPIRE_WIKI_REPORTS_ROOT
    $fromEnv = $fromEnv.Trim()
    if ($fromEnv) {
        return $fromEnv
    }
    $iRoot = "I:\EMPIRE_DATA\wiki-reports"
    $dRoot = "D:\EMPIRE_DATA\wiki-reports"
    $iIndex = Join-Path $iRoot "$Year\title-index.sqlite"
    $dIndex = Join-Path $dRoot "$Year\title-index.sqlite"
    if (Test-Path -LiteralPath $iIndex) {
        return $iRoot
    }
    if (Test-Path -LiteralPath $dIndex) {
        return $dRoot
    }
    if (Test-EmpireWikiDataOnDriveI) {
        return $iRoot
    }
    return $dRoot
}

function Initialize-EmpireWikiStorageEnv {
    param(
        [string]$Year = "2026"
    )
    $reports = Resolve-WikiReportsRoot -Year $Year
    $archive = Resolve-WeaviateArchivePath
    $env:EMPIRE_WIKI_REPORTS_ROOT = $reports
    $env:EMPIRE_WEAVIATE_ARCHIVE = $archive
    $yearDir = Join-Path $reports $Year
    if (-not (Test-Path -LiteralPath $yearDir)) {
        New-Item -ItemType Directory -Force -Path $yearDir | Out-Null
    }
    return @{
        reports_root = $reports
        weaviate_archive = $archive
        year_dir       = $yearDir
    }
}
