# Install JDK + Ghidra for REA native binary analysis (Windows).
# Usage: .\scripts\ensure-ghidra-rea.ps1
# Idempotent: skips download if zip and extract dir already exist.

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$GhidraRoot = Join-Path $Root "tools\ghidra"
$GhidraVersion = "12.1.4"
$ZipName = "ghidra_${GhidraVersion}_PUBLIC_20260921.zip"
$ZipPath = Join-Path $GhidraRoot $ZipName
$ReleaseTag = "Ghidra_${GhidraVersion}_build"
$DownloadUrl =
  "https://github.com/NationalSecurityAgency/ghidra/releases/download/$ReleaseTag/$ZipName"

function Resolve-JdkHome {
    $fromEnv = $env:JAVA_HOME
    if ($fromEnv -and (Test-Path (Join-Path $fromEnv "bin\java.exe"))) {
        return $fromEnv
    }
    $glob = Get-ChildItem "C:\Program Files\Microsoft" -Directory -Filter "jdk-21*" -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if ($glob -and (Test-Path (Join-Path $glob.FullName "bin\java.exe"))) {
        return $glob.FullName
    }
    $adopt = Get-ChildItem "C:\Program Files\Eclipse Adoptium" -Directory -Filter "jdk-21*" -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if ($adopt -and (Test-Path (Join-Path $adopt.FullName "bin\java.exe"))) {
        return $adopt.FullName
    }
    return $null
}

$jdk = Resolve-JdkHome
if (-not $jdk) {
    Write-Host "Installing Microsoft OpenJDK 21 (Ghidra headless requires Java)..."
    winget install Microsoft.OpenJDK.21 --accept-package-agreements --accept-source-agreements
    $jdk = Resolve-JdkHome
    if (-not $jdk) {
        throw "JDK 21 not found after winget install. Set JAVA_HOME and re-run."
    }
}
Write-Host "JAVA_HOME: $jdk"

New-Item -ItemType Directory -Path $GhidraRoot -Force | Out-Null

if (-not (Test-Path $ZipPath)) {
    Write-Host "Downloading Ghidra $GhidraVersion (~540 MB)..."
    Invoke-WebRequest -Uri $DownloadUrl -OutFile $ZipPath -Headers @{ "User-Agent" = "EMPIRE-setup" }
}

$installDir = Get-ChildItem $GhidraRoot -Directory -Filter "ghidra_*PUBLIC*" -ErrorAction SilentlyContinue |
    Select-Object -First 1
if (-not $installDir) {
    Write-Host "Expanding Ghidra archive..."
    Expand-Archive -Path $ZipPath -DestinationPath $GhidraRoot -Force
    $installDir = Get-ChildItem $GhidraRoot -Directory -Filter "ghidra_*PUBLIC*" |
        Select-Object -First 1
}
if (-not $installDir) {
    throw "Ghidra extract folder missing under $GhidraRoot"
}

$ghidraDir = $installDir.FullName
Write-Host "GHIDRA_INSTALL_DIR: $ghidraDir"

$env:JAVA_HOME = $jdk
$env:GHIDRA_INSTALL_DIR = $ghidraDir
$env:Path = "$jdk\bin;$env:Path"

$reaScript = Join-Path $Root "tools\rea\node_modules\rea-agents\scripts\rea.mjs"
if (-not (Test-Path $reaScript)) {
    Write-Host "REA npm package missing — running ensure-rea.ps1 first..."
    & (Join-Path $Root "scripts\ensure-rea.ps1")
}

$env:REA_EVIDENCE_ROOT = "C:/Empire_Workbench/04_Thought_Experiments/rea_cache"
$ghidraCheck = & node $reaScript doctor --filter-output scope_checks 2>&1 | Out-String
if ($ghidraCheck -notmatch '(?s)- name: ghidra\r?\n\s+ok: true') {
    Write-Host $ghidraCheck
    throw "rea doctor did not report healthy Ghidra"
}

$workbenchDirs = @(
    "C:\Empire_Workbench\rea_inbox",
    "C:\Empire_Workbench\04_Thought_Experiments\rea_cache"
)
foreach ($d in $workbenchDirs) {
    New-Item -ItemType Directory -Path $d -Force | Out-Null
}

Write-Host "Ghidra + REA native path OK."
exit 0
