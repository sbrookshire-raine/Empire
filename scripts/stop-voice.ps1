#Requires -Version 5.1
<#
.SYNOPSIS
  Stop the EMPIRE Speaches voice container (port 8000).
#>
param(
    [string]$ContainerName = "empire-speaches"
)

$ErrorActionPreference = "Continue"

Write-Host "Stopping Voice / Speaches ($ContainerName)..."
docker stop $ContainerName 2>$null | Out-Null
Write-Host "  Done. Eve push-to-talk will fail until the stack restarts or you run .\scripts\start-voice.ps1"
