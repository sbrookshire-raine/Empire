#Requires -Version 5.1
<#
.SYNOPSIS
  Stop and remove the on-demand EMPIRE Wikipedia Weaviate container.
#>
param(
    [string]$ContainerName = "empire-weaviate-heist-2017"
)

$ErrorActionPreference = "Continue"

Write-Host "Stopping Weaviate ($ContainerName)…"
docker stop $ContainerName 2>$null | Out-Null
docker rm $ContainerName 2>$null | Out-Null
Write-Host "  Done. Wiki Local will fail until you start it again (Start-EMPIRE.bat -Weaviate)."
