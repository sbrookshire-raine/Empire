#Requires -Version 5.1
param(
    [switch]$NoBrowser,
    [switch]$SkipOllamaCheck
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$WorkbenchUrl = "http://127.0.0.1:8080/eve.html"

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

function Get-OllamaExecutable {
    $cmd = Get-Command ollama -ErrorAction SilentlyContinue
    if ($cmd -and $cmd.Source) {
        return $cmd.Source
    }
    $candidates = @(
        (Join-Path $env:LOCALAPPDATA "Programs\Ollama\ollama.exe"),
        (Join-Path ${env:ProgramFiles} "Ollama\ollama.exe"),
        (Join-Path ${env:ProgramFiles(x86)} "Ollama\ollama.exe")
    )
    foreach ($path in $candidates) {
        if ($path -and (Test-Path $path)) {
            return $path
        }
    }
    return $null
}

function Ensure-OllamaRunning {
    if (Test-Url "http://127.0.0.1:11434/api/tags") {
        Write-Host "  Ollama already running"
        return
    }

    $ollamaExe = Get-OllamaExecutable
    if (-not $ollamaExe) {
        throw "Ollama is not running and ollama.exe was not found. Install from https://ollama.com/ or start manually."
    }

    Write-Host "  Starting Ollama..."
    Start-Process -FilePath $ollamaExe -ArgumentList "serve"

    for ($attempt = 1; $attempt -le 30; $attempt++) {
        if (Test-Url "http://127.0.0.1:11434/api/tags") {
            Write-Host "  Ollama healthy"
            return
        }
        Start-Sleep -Seconds 1
    }

    throw "Ollama did not become healthy within 30 seconds."
}

Write-Host ""
Write-Host "EMPIRE Launcher"
Write-Host "==============="
Write-Host ""

if (-not $SkipOllamaCheck) {
    Write-Host "Ollama"
    Ensure-OllamaRunning
    Write-Host ""
}

Write-Host "Stack"
$stackArgs = @{}
if ($SkipOllamaCheck) {
    $stackArgs.SkipOllamaCheck = $true
}
& (Join-Path $PSScriptRoot "start-stack.ps1") @stackArgs

if (-not $NoBrowser) {
    Write-Host ""
    Write-Host "Opening $WorkbenchUrl"
    Start-Process $WorkbenchUrl | Out-Null
}

Write-Host ""
Write-Host "EMPIRE is ready. Services keep running in the background."
Write-Host "Workbench: $WorkbenchUrl"
Write-Host ""
