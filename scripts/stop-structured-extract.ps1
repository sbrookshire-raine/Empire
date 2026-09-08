# Stop EMPIRE structured-extract (llama-server on :8092)
$ErrorActionPreference = "Continue"
$port = 8092
Write-Host "Stopping structured-extract listeners on port $port..."

try {
  $conns = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
  foreach ($c in $conns) {
    if ($c.OwningProcess) {
      Stop-Process -Id $c.OwningProcess -Force -ErrorAction SilentlyContinue
      Write-Host "  Stopped PID $($c.OwningProcess)"
    }
  }
} catch {
  Write-Host "  Get-NetTCPConnection unavailable; trying netstat fallback"
}

# Release extract lease if held
$py = Join-Path $PSScriptRoot "..\venv\Scripts\python.exe"
if (Test-Path $py) {
  & $py -m pipeline.gpu_lease release 2>$null | Out-Null
}

Write-Host "Done. Toolbelt Structured Extract can stay OFF until next use."
