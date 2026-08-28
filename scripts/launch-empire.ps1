#Requires -Version 5.1
<#
.SYNOPSIS
    Start all EMPIRE services and open the Eve Workbench in the default browser.

.DESCRIPTION
    1. Ensures Ollama is running (starts ollama serve if needed)
    2. Runs scripts/start-stack.ps1 (V:, Postgres, PocketBase, frontend, Eve)
    3. Opens http://127.0.0.1:8080/eve.html

.PARAMETER NoBrowser
    Start services only; do not open a browser tab.

.PARAMETER SkipOllamaCheck
    Do not verify or start Ollama (passed through to start-stack.ps1).
#>
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
        throw @"
Ollama is not running and ollama.exe was not found.
Install Ollama from https://ollama.com/ or start it manually, then run this launcher again.
"@
    }

    Write-Host "  Starting Ollama ($ollamaExe serve)..."
    Start-Process -FilePath $ollamaExe -ArgumentList @("serve") -WindowStyle Hidden | Out-Null

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
