# Start EMPIRE structured-extract llama-server on 127.0.0.1:8092
$ErrorActionPreference = "Stop"
$Port = 8092
$Listen = "127.0.0.1"
$GgufDir = Join-Path $env:LOCALAPPDATA "EMPIRE\models\gguf"
$Manifest = Join-Path $PSScriptRoot "..\config\empire-release-manifest.json"
$PathHint = Join-Path $env:LOCALAPPDATA "EMPIRE\llama-server-path.txt"

$GgufName = "Qwen3-14B-Q4_K_M.gguf"
if (Test-Path $Manifest) {
  try {
    $m = Get-Content $Manifest -Raw | ConvertFrom-Json
    if ($m.workers.structured_extract.gguf_filename) {
      $GgufName = [string]$m.workers.structured_extract.gguf_filename
    }
  } catch {}
}

$GgufPath = Join-Path $GgufDir $GgufName

$Llama = $env:EMPIRE_LLAMA_SERVER
if (-not $Llama -and (Test-Path $PathHint)) {
  $Llama = (Get-Content $PathHint -Raw).Trim()
}
if (-not $Llama) {
  $defaultExe = Join-Path $env:LOCALAPPDATA "EMPIRE\bin\llama.cpp\win-cuda-12.4\llama-server.exe"
  if (Test-Path $defaultExe) { $Llama = $defaultExe }
}
if (-not $Llama) {
  $Llama = (Get-Command llama-server -ErrorAction SilentlyContinue | Select-Object -First 1).Source
}
if (-not $Llama) {
  $Llama = (Get-Command llama-server.exe -ErrorAction SilentlyContinue | Select-Object -First 1).Source
}

Write-Host "Structured Extract starter"
Write-Host "  GGUF: $GgufPath"
Write-Host "  llama-server: $Llama"
Write-Host "  listen: http://${Listen}:${Port}"

if (-not (Test-Path $GgufPath)) {
  Write-Host "ERROR: GGUF not found. Download Qwen3-14B Q4_K_M into $GgufDir"
  Write-Host "See docs/workers/STRUCTURED_EXTRACT.md"
  exit 2
}
if (-not $Llama -or -not (Test-Path $Llama)) {
  Write-Host "ERROR: llama-server not found. Expected under LOCALAPPDATA\EMPIRE\bin\llama.cpp"
  exit 3
}

# Put llama dir on PATH so CUDA companion DLLs resolve
$llamaDir = Split-Path -Parent $Llama
$env:PATH = "$llamaDir;$env:PATH"

# Acquire GPU lease (non-fatal if denied)
$py = Join-Path $PSScriptRoot "..\venv\Scripts\python.exe"
if (Test-Path $py) {
  & $py -m pipeline.gpu_lease acquire extract --holder llama-server | Out-Host
}

$existing = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
if ($existing) {
  Write-Host "Already listening on $Port - leaving as-is."
  exit 0
}

$argList = @(
  "-m", $GgufPath,
  "--host", $Listen,
  "--port", "$Port",
  "-c", "8192"
)
Write-Host "Starting: $Llama $($argList -join ' ')"
Start-Process -FilePath $Llama -ArgumentList $argList -WorkingDirectory $llamaDir -WindowStyle Minimized
Start-Sleep -Seconds 3
Write-Host "Started. Stop with scripts\stop-structured-extract.ps1"
