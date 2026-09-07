# EMPIRE start-voice helper
# Prefers Speaches / Voicebox if docker is available; otherwise prints manual steps.

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

Write-Host "Trying Speaches (STT+TTS, models on demand)…"
# Non-destructive: only start if not running
$existing = docker ps -a --filter "name=empire-speaches" --format "{{.Names}}" 2>$null
if ($existing -eq "empire-speaches") {
  docker start empire-speaches | Out-Host
} else {
  Write-Host "No empire-speaches container yet."
  Write-Host "Example (Architect-approved pull):"
  Write-Host '  docker run -d --name empire-speaches -p 8000:8000 ghcr.io/speaches-ai/speaches:latest'
  Write-Host "Or use Voicebox: https://github.com/agjs/voicebox"
}

Write-Host ""
Write-Host "Health check:"
& "$PSScriptRoot\..\venv\Scripts\python.exe" -c "import os; os.environ['PYTHONPATH']=r'C:\EMPIRE'; from pipeline import voice_presence; import json; print(json.dumps(voice_presence.health(), indent=2))"
