# Quick relief for slow Chrome Remote Desktop + Cursor days.
# Stops heavy optional services and zombie MCP processes. Restart Cursor after.

$ErrorActionPreference = "Continue"
$root = Split-Path -Parent $PSScriptRoot

Write-Host "Remote build lighten"
Write-Host "===================="

Write-Host "[1/4] Superwhisper + audio engine..."
Stop-Process -Name Superwhisper -Force -ErrorAction SilentlyContinue
Stop-Process -Name audiodg -Force -ErrorAction SilentlyContinue

Write-Host "[2/4] Weaviate (Wiki Local)..."
& (Join-Path $root "scripts\stop-weaviate.ps1")

Write-Host "[3/6] Remote Cursor MCP profile (no graft npx)..."
& (Join-Path $root "scripts\switch-cursor-mcp.ps1") -Profile Remote

Write-Host "[4/6] Stopping stray empire MCP python processes..."
Get-CimInstance Win32_Process -Filter "Name='python.exe'" -ErrorAction SilentlyContinue |
    Where-Object { $_.CommandLine -match 'mcp\\' } |
    ForEach-Object {
        Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue
    }

Write-Host "[5/6] Disable Graft Cursor hooks (saves ~140ms per Read/Grep)..."
$hooksOff = Join-Path $root ".cursor\hooks.json"
$hooksLean = @'
{
  "version": 1,
  "hooks": {}
}
'@
Set-Content -LiteralPath $hooksOff -Value $hooksLean -Encoding utf8NoBOM

Write-Host "[6/6] Stop Eve sandbox Docker containers..."
docker ps -q --filter "name=eve-sbx" 2>$null | ForEach-Object {
    docker stop $_ 2>$null | Out-Null
}
Write-Host "  Tip: quit Docker Desktop from the tray if you are not using containers today (~3 GB WSL RAM)."

Write-Host ""
Write-Host "Done. Fully quit and restart Cursor, then reconnect Chrome Remote Desktop."
Write-Host "Re-enable Graft hooks later: Copy-Item .cursor\hooks.with-graft.json .cursor\hooks.json -Force"
