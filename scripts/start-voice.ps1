#Requires -Version 5.1
<#
.SYNOPSIS
  Start Speaches (CPU) on http://127.0.0.1:8000 for Eve push-to-talk STT/TTS.

.NOTES
  Called automatically from scripts/start-stack.ps1 and Start-EMPIRE.bat.
  Docs: docs/VOICE_PRESENCE.md
#>
param(
    [switch]$SkipModelEnsure
)

$ErrorActionPreference = "Continue"
$Root = Split-Path -Parent $PSScriptRoot

Write-Host "EMPIRE Voice Presence"
Write-Host "====================="
Write-Host "Target API: http://127.0.0.1:8000 (OpenAI-compatible /v1/audio/*)"
Write-Host ""

$docker = Get-Command docker -ErrorAction SilentlyContinue
if (-not $docker) {
    Write-Warning "Docker not found. Voice in Eve will fail until Speaches is running."
    Write-Host "  Set EMPIRE_VOICE_BASE_URL if you run Voicebox elsewhere."
    Write-Host "  Docs: docs/VOICE_PRESENCE.md"
    exit 0
}

$image = if ($env:EMPIRE_SPEACHES_IMAGE) { $env:EMPIRE_SPEACHES_IMAGE } else { "ghcr.io/speaches-ai/speaches:latest-cpu" }
$name = "empire-speaches"

Write-Host "Speaches image: $image"
$existing = docker ps -a --filter "name=^/${name}$" --format "{{.Names}}" 2>$null
if (-not $existing) {
    $existing = docker ps -a --filter "name=$name" --format "{{.Names}}" 2>$null
}

if ($existing -match $name) {
    Write-Host "  Starting existing container $name..."
    docker start $name | Out-Null
}
else {
    Write-Host "  Creating $name (CPU - keeps GPU free for Ollama)..."
    docker run -d --name $name `
        -p 127.0.0.1:8000:8000 `
        --volume empire-speaches-hf:/home/ubuntu/.cache/huggingface/hub `
        $image | Out-Null
}

Write-Host "  Waiting for /health..."
$ready = $false
for ($i = 1; $i -le 45; $i++) {
    try {
        $r = Invoke-WebRequest -Uri "http://127.0.0.1:8000/health" -UseBasicParsing -TimeoutSec 3
        if ($r.StatusCode -lt 500) { $ready = $true; break }
    }
    catch {
        if (($i % 10) -eq 0) {
            Write-Host "  Still warming up... ($i s)"
        }
        Start-Sleep -Seconds 2
    }
}
if (-not $ready) {
    Write-Error "Speaches not healthy. Check: docker logs $name"
    exit 1
}

if (-not $SkipModelEnsure) {
    $models = @(
        "Systran/faster-whisper-base",
        "speaches-ai/Kokoro-82M-v1.0-ONNX"
    )
    foreach ($m in $models) {
        try {
            $null = Invoke-WebRequest -Uri "http://127.0.0.1:8000/v1/models/$m" -Method POST -UseBasicParsing -TimeoutSec 600
            Write-Host "  Model ready: $m"
        }
        catch {
            Write-Warning "Model ensure warning for ${m}: $($_.Exception.Message)"
        }
    }
}

Write-Host "  Ready: http://127.0.0.1:8000"
$env:PYTHONPATH = $Root
& (Join-Path $Root "venv\Scripts\python.exe") -m pipeline.voice_presence health
exit $LASTEXITCODE
