#Requires -Version 5.1
param([switch]$SkipOllamaCheck)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot

function Test-Url {
    param([string]$Url)
    try {
        $response = Invoke-WebRequest -Uri $Url -UseBasicParsing -TimeoutSec 4
        return $response.StatusCode -ge 200 -and $response.StatusCode -lt 400
    }
    catch {
        return $false
    }
}

function Wait-Url {
    param([string]$Name, [string]$Url)
    for ($attempt = 1; $attempt -le 45; $attempt++) {
        if (Test-Url $Url) {
            Write-Host "  $Name healthy"
            return
        }
        Start-Sleep -Seconds 1
    }
    throw "$Name did not become healthy: $Url"
}

Write-Host "EMPIRE start"
Write-Host "============"

if (-not (Test-Path "V:\Cognee")) {
    Write-Host "Requesting the scheduled V: mount..."
    schtasks /Run /TN "EMPIRE Mount Cognee VHDX" | Out-Null
    for ($attempt = 1; $attempt -le 15 -and -not (Test-Path "V:\Cognee"); $attempt++) {
        Start-Sleep -Seconds 1
    }
    if (-not (Test-Path "V:\Cognee")) {
        throw "V:\Cognee is unavailable. Plug in the T7, then run scripts\mount-cognee-vhdx.ps1 as Administrator."
    }
}
Write-Host "  V:\Cognee ready"

& (Join-Path $PSScriptRoot "ensure-cognee-postgres.ps1")

if (-not $SkipOllamaCheck -and -not (Test-Url "http://127.0.0.1:11434/api/tags")) {
    throw "Ollama is down. Start Ollama and run this command again."
}
Write-Host "  Ollama healthy"

if (-not (Test-Url "http://127.0.0.1:8090/api/health")) {
    Start-Process -FilePath (Join-Path $Root "backend\pocketbase\pocketbase.exe") `
        -ArgumentList "serve","--http=127.0.0.1:8090" `
        -WorkingDirectory (Join-Path $Root "backend\pocketbase")
}
Wait-Url "PocketBase" "http://127.0.0.1:8090/api/health"

if (-not (Test-Url "http://127.0.0.1:8080/api/memory/status")) {
    Start-Process -FilePath (Join-Path $Root "venv\Scripts\python.exe") `
        -ArgumentList "-m","frontend.serve" `
        -WorkingDirectory $Root
}
Wait-Url "Eve Workbench" "http://127.0.0.1:8080/api/memory/status"

if (-not (Test-Url "http://127.0.0.1:2000/eve/v1/info")) {
    & (Join-Path $Root "venv\Scripts\python.exe") (Join-Path $Root "scripts\ensure-eve-build.py")
    if ($LASTEXITCODE -ne 0) {
        throw "Eve production build preparation failed."
    }
    $env:EMPIRE_ROOT = $Root
    $env:POCKETBASE_URL = "http://127.0.0.1:8090"
    $env:OLLAMA_BASE_URL = "http://localhost:11434/v1"
    $env:OLLAMA_MODEL = "richardyoung/qwen2.5-14b-instruct-abliterated:latest"
    $npm = (Get-Command npm.cmd -ErrorAction Stop).Source
    Start-Process -FilePath $npm `
        -ArgumentList "exec","--","eve","start","--host","127.0.0.1","--port","2000" `
        -WorkingDirectory (Join-Path $Root "agents\empire-task-agent")
}
Wait-Url "Eve" "http://127.0.0.1:2000/eve/v1/info"

& (Join-Path $PSScriptRoot "refresh-dashboard.ps1")

Write-Host ""
Write-Host "Ready: http://127.0.0.1:8080/eve.html"
