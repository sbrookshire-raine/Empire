#Requires -Version 5.1
<#
.SYNOPSIS
  Build EMPIRE offline survival kit manifest and optionally pull models/wheels.

.DESCRIPTION
  Time-sensitive: run while online. Writes D:\empire\MANIFEST.md (configurable).
  Does not auto-download Hugging Face weights unless -PullHuggingFace is set.

.EXAMPLE
  .\scripts\build-offline-mirror.ps1
  .\scripts\build-offline-mirror.ps1 -PullOllama -Wheelhouse
#>
param(
    [string]$MirrorRoot = "D:\empire",
    [switch]$PullOllama,
    [switch]$Wheelhouse,
    [switch]$PullHuggingFace,
    [switch]$DockerSave
)

$ErrorActionPreference = "Continue"
$Root = Split-Path -Parent $PSScriptRoot
$ConfigPath = Join-Path $Root "config\offline-mirror.json"

if (-not (Test-Path $ConfigPath)) {
    Write-Error "Missing $ConfigPath"
    exit 1
}

$config = Get-Content $ConfigPath -Raw | ConvertFrom-Json
if ($config.mirror_root_default -and -not $PSBoundParameters.ContainsKey("MirrorRoot")) {
    $MirrorRoot = $config.mirror_root_default
}

New-Item -ItemType Directory -Force -Path $MirrorRoot | Out-Null
$stamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
$manifestPath = Join-Path $MirrorRoot "MANIFEST.md"

Write-Host "EMPIRE Offline Mirror"
Write-Host "====================="
Write-Host "Root: $MirrorRoot"
Write-Host ""

$lines = @(
    "# EMPIRE Offline Mirror Manifest",
    "",
    "Generated: $stamp",
    "Repo: C:\EMPIRE",
    "",
    "## Ollama models",
    ""
)

$ollama = Get-Command ollama -ErrorAction SilentlyContinue
$localModels = @()
if ($ollama) {
    try {
        $localModels = (& ollama list 2>$null) -split "`n" | Where-Object { $_ -match "\S" }
    }
    catch { }
}

foreach ($entry in $config.ollama_models) {
    $name = $entry.name
    $present = $false
    if ($localModels) {
        $present = ($localModels | Where-Object { $_ -match [regex]::Escape($name.Split(":")[0]) }).Count -gt 0
    }
    $status = if ($present) { "present" } else { "missing" }
    $req = if ($entry.required) { "required" } else { "optional" }
    $lines += "- ``$name`` — $($entry.role) — **$status** ($req)"
    if ($PullOllama -and $ollama -and -not $present) {
        Write-Host "Pulling ollama model $name ..."
        & ollama pull $name
    }
}

$lines += @("", "## Python wheelhouse", "")
if ($Wheelhouse) {
    $reqFile = Join-Path $Root $config.pip_wheelhouse.requirements
    $wheelDir = $config.pip_wheelhouse.output_dir
    New-Item -ItemType Directory -Force -Path $wheelDir | Out-Null
    $pip = Join-Path $Root "venv\Scripts\pip.exe"
    if (Test-Path $pip) {
        Write-Host "Downloading wheels to $wheelDir ..."
        & $pip download -r $reqFile -d $wheelDir
        $lines += "- Wheelhouse: ``$wheelDir`` — downloaded $stamp"
    }
    else {
        $lines += "- Wheelhouse: **skipped** (venv pip not found)"
    }
}
else {
    $lines += "- Run ``.\scripts\build-offline-mirror.ps1 -Wheelhouse`` to populate ``$($config.pip_wheelhouse.output_dir)``"
}

$lines += @("", "## Hugging Face (optional)", "")
foreach ($hf in $config.huggingface_optional) {
    $lines += "- ``$($hf.repo)`` — $($hf.role)"
    if ($PullHuggingFace) {
        $hfCli = Get-Command huggingface-cli -ErrorAction SilentlyContinue
        if ($hfCli) {
            Write-Host "Downloading HF $($hf.repo) ..."
            & huggingface-cli download $hf.repo
        }
    }
}

$lines += @("", "## Docker images (optional)", "")
foreach ($img in $config.docker_images_optional) {
    $lines += "- ``$img``"
    if ($DockerSave) {
        $safe = ($img -replace "[/:]", "_")
        $tar = Join-Path $MirrorRoot "$safe.tar"
        Write-Host "Saving docker image $img -> $tar"
        docker pull $img 2>$null
        docker save -o $tar $img 2>$null
    }
}

$lines += @(
    "",
    "## Offline env flags",
    ""
)
foreach ($flag in $config.offline_env_flags) {
    $lines += "- ``$flag``"
}

$lines += @(
    "",
    "## Kiwix ZIM (manual)",
    "",
    "Browse https://library.kiwix.org/ and copy ZIM files to offline storage.",
    ""
)

foreach ($zim in $config.kiwix_zim_suggestions) {
    $lines += "- $($zim.name) — $($zim.url)"
}

$lines += ""
$lines += "## Verification"
$lines += ""
$lines += '```powershell'
$lines += ".\scripts\audit-embedding-stack.ps1"
$lines += "ollama list"
$lines += '```'
$lines += ""
$lines += "See docs/RESEARCH_CLOSURE.md - discovery phase closed 2026-09-10."

$content = ($lines -join "`n") + "`n"
Set-Content -Path $manifestPath -Value $content -Encoding UTF8
Write-Host ""
Write-Host "Wrote $manifestPath"
Write-Host "Next: review missing Ollama models; run with -PullOllama while online."
