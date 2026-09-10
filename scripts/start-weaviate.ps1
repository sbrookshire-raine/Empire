#Requires -Version 5.1
<#
.SYNOPSIS
  Boot on-demand Wikipedia Weaviate on http://127.0.0.1:8091 (not part of default Start-EMPIRE).

.NOTES
  Archive: D:\weaviate_v2_archive\weaviate
  Container: empire-weaviate-heist-2017
  Tear down: .\scripts\stop-weaviate.ps1
#>
param(
    [string]$ArchivePath = "D:\weaviate_v2_archive\weaviate",
    [string]$ContainerName = "empire-weaviate-heist-2017",
    [string]$ApiKey = "WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih",
    [int]$ReadyTimeoutSec = 180
)

$ErrorActionPreference = "Stop"

function Test-WeaviateReady {
    param([string]$Key)
    try {
        $headers = @{ Authorization = "Bearer $Key" }
        $response = Invoke-WebRequest -Uri "http://127.0.0.1:8091/v1/.well-known/ready" `
            -Headers $headers -UseBasicParsing -TimeoutSec 5
        return $response.StatusCode -ge 200 -and $response.StatusCode -lt 400
    }
    catch {
        return $false
    }
}

Write-Host "Weaviate (Wiki Local)"
Write-Host "===================="

$docker = Get-Command docker -ErrorAction SilentlyContinue
if (-not $docker) {
    throw "Docker is not on PATH. Install Docker Desktop, then retry."
}

if (-not (Test-Path -LiteralPath $ArchivePath)) {
    throw "Weaviate archive not found: $ArchivePath - plug in / mount the drive that holds weaviate_v2_archive."
}

if (Test-WeaviateReady -Key $ApiKey) {
    Write-Host "  Already ready on http://127.0.0.1:8091"
    return
}

$existing = docker ps -a --filter "name=^/${ContainerName}$" --format "{{.Names}}" 2>$null
if ($existing -eq $ContainerName) {
    $running = docker ps --filter "name=^/${ContainerName}$" --format "{{.Names}}" 2>$null
    if ($running -eq $ContainerName) {
        Write-Host "  Container running - waiting for ready..."
    }
    else {
        Write-Host "  Starting existing container $ContainerName..."
        docker start $ContainerName | Out-Null
    }
}
else {
    Write-Host "  Creating container $ContainerName (port 8091)..."
    # Mount must be RW (Weaviate opens Bolt); scout/export use GET only.
    $archiveDocker = ($ArchivePath -replace "\\", "/")
    docker run -d --name $ContainerName `
        -p 8091:8080 -p 50052:50051 `
        -e AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED=false `
        -e AUTHENTICATION_APIKEY_ENABLED=true `
        -e AUTHENTICATION_APIKEY_ALLOWED_KEYS=$ApiKey `
        -e AUTHENTICATION_APIKEY_USERS=hello@dify.ai `
        -e AUTHORIZATION_ADMINLIST_ENABLED=true `
        -e AUTHORIZATION_ADMINLIST_USERS=hello@dify.ai `
        -e PERSISTENCE_DATA_PATH=/var/lib/weaviate `
        -e DISABLE_TELEMETRY=true `
        -e QUERY_DEFAULTS_LIMIT=25 `
        -e DEFAULT_VECTORIZER_MODULE=none `
        -e CLUSTER_HOSTNAME=node1 `
        -v "${archiveDocker}:/var/lib/weaviate" `
        semitechnologies/weaviate:1.27.0 `
        --host 0.0.0.0 --port 8080 --scheme http | Out-Null
}

for ($attempt = 1; $attempt -le $ReadyTimeoutSec; $attempt++) {
    if (Test-WeaviateReady -Key $ApiKey) {
        Write-Host "  Ready: http://127.0.0.1:8091"
        Write-Host "  Enable Toolbelt Wiki Local, then ask Eve."
        Write-Host "  Stop later: .\scripts\stop-weaviate.ps1"
        return
    }
    if (($attempt % 15) -eq 0) {
        Write-Host "  Still warming up... ($attempt s) - large archive can take a while"
    }
    Start-Sleep -Seconds 1
}

throw "Weaviate did not become ready within ${ReadyTimeoutSec}s. Check: docker logs $ContainerName"
