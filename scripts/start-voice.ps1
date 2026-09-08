# EMPIRE start-voice helper
# Starts Speaches (CPU by default) on 127.0.0.1:8000 when Docker is available.

$ErrorActionPreference = "Continue"
Write-Host "EMPIRE Voice Presence"
Write-Host "Target API: http://127.0.0.1:8000 (OpenAI-compatible /v1/audio/*)"
Write-Host ""

$docker = Get-Command docker -ErrorAction SilentlyContinue
if (-not $docker) {
  Write-Host "Docker not found. Install Speaches or Voicebox manually, then set EMPIRE_VOICE_BASE_URL."
  Write-Host "Docs: docs/VOICE_PRESENCE.md"
  exit 0
}

$image = if ($env:EMPIRE_SPEACHES_IMAGE) { $env:EMPIRE_SPEACHES_IMAGE } else { "ghcr.io/speaches-ai/speaches:latest-cpu" }
$name = "empire-speaches"

Write-Host "Speaches image: $image"
$existing = docker ps -a --filter "name=^/${name}$" --format "{{.Names}}" 2>$null
if (-not $existing) {
  # Older docker format may omit leading slash in filter; fallback
  $existing = docker ps -a --filter "name=$name" --format "{{.Names}}" 2>$null
}

if ($existing -match $name) {
  Write-Host "Starting existing container $name…"
  docker start $name | Out-Host
} else {
  Write-Host "Creating $name (CPU preferred so Ollama keeps GPU)…"
  docker run -d --name $name `
    -p 127.0.0.1:8000:8000 `
    --volume empire-speaches-hf:/home/ubuntu/.cache/huggingface/hub `
    $image | Out-Host
}

Write-Host ""
Write-Host "Waiting for /health…"
$ready = $false
for ($i = 1; $i -le 30; $i++) {
  try {
    $r = Invoke-WebRequest -Uri "http://127.0.0.1:8000/health" -UseBasicParsing -TimeoutSec 3
    if ($r.StatusCode -lt 500) { $ready = $true; break }
  } catch {
    Start-Sleep -Seconds 2
  }
}
if (-not $ready) {
  Write-Host "Speaches not healthy yet. Check: docker logs $name"
  exit 1
}

# Ensure default EMPIRE models exist (idempotent)
$models = @(
  "Systran/faster-whisper-base",
  "speaches-ai/Kokoro-82M-v1.0-ONNX"
)
foreach ($m in $models) {
  try {
    $null = Invoke-WebRequest -Uri "http://127.0.0.1:8000/v1/models/$m" -Method POST -UseBasicParsing -TimeoutSec 600
    Write-Host "Model ready: $m"
  } catch {
    Write-Host "Model ensure warning for $m : $($_.Exception.Message)"
  }
}

Write-Host ""
Write-Host "Health check:"
$env:PYTHONPATH = "C:\EMPIRE"
& "$PSScriptRoot\..\venv\Scripts\python.exe" -m pipeline.voice_presence health
