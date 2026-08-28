#Requires -Version 5.1
<#
.SYNOPSIS
  Start Docker Desktop if needed and bring up empire-cognee-postgres.
#>
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Compose = Join-Path $Root "docker-compose.yml"
$DockerDesktop = Join-Path $env:ProgramFiles "Docker\Docker\Docker Desktop.exe"

function Test-DockerEngine {
    docker info --format "{{.ServerVersion}}" 2>$null | Out-Null
    return ($LASTEXITCODE -eq 0)
}

if (-not (Test-Path $Compose)) {
    throw "docker-compose.yml not found at $Compose"
}

if (-not (Test-DockerEngine)) {
    if (-not (Test-Path $DockerDesktop)) {
        throw "Docker engine is down and Docker Desktop.exe was not found."
    }
    Write-Host "Starting Docker Desktop..."
    Start-Process $DockerDesktop | Out-Null
    $deadline = (Get-Date).AddMinutes(3)
    do {
        Start-Sleep -Seconds 4
        if (Test-DockerEngine) { break }
        Write-Host "  waiting for Docker engine..."
    } while ((Get-Date) -lt $deadline)
    if (-not (Test-DockerEngine)) {
        throw "Docker engine did not become ready. Open Docker Desktop and retry."
    }
}

Write-Host "Starting empire-cognee-postgres..."
Push-Location $Root
try {
    docker compose up -d
} finally {
    Pop-Location
}

$deadline = (Get-Date).AddMinutes(2)
do {
    Start-Sleep -Seconds 3
    $health = docker inspect -f "{{.State.Health.Status}}" empire-cognee-postgres 2>$null
    if ($health -eq "healthy") {
        Write-Host "Postgres healthy on localhost:5432"
        exit 0
    }
    Write-Host ("  postgres health=" + $health)
} while ((Get-Date) -lt $deadline)

throw "empire-cognee-postgres did not become healthy."
