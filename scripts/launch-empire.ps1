#Requires -Version 5.1
param(
    [switch]$NoBrowser,
    [switch]$SkipOllamaCheck,
    [switch]$Weaviate,
    [switch]$NoWiki,
    [switch]$NoVoice,
    [switch]$SkipStartupChecks
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
    Write-Host "  Tuning context for Eve (24k, parallel=1)..."
    & (Join-Path $PSScriptRoot "ensure-ollama-parallel.ps1") `
        -NumParallel 1 -ContextLength 24576 -KvCacheType q8_0 -FlashAttention
    if ($LASTEXITCODE -ne 0) {
        Write-Warning ('Ollama tune exited ' + $LASTEXITCODE + '; Eve may truncate instructions.')
    }
    Write-Host ""
}

Write-Host "Stack"
$stackArgs = @{}
if ($SkipOllamaCheck) {
    $stackArgs.SkipOllamaCheck = $true
}
if ($Weaviate) {
    $stackArgs.Weaviate = $true
}
if ($NoWiki) {
    $stackArgs.NoWiki = $true
}
if ($NoVoice) {
    $stackArgs.NoVoice = $true
}
if ($SkipStartupChecks) {
    $stackArgs.SkipStartupChecks = $true
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
Write-Host "Voice/Wiki: start only when voice_presence / wiki_local are ON in the header toolbelt (-NoVoice / -NoWiki override)."
Write-Host ""
