<#
.SYNOPSIS
    Ensure ollama serve is running with OLLAMA_NUM_PARALLEL (default 8) for nomic-embed concurrency.

.DESCRIPTION
    OLLAMA_NUM_PARALLEL is read only at ollama serve start. Setting it on the ingest
    process alone has no effect. This script verifies the live serve process env; if it
    already matches NumParallel, it skips restart (keeps pinned nomic). Otherwise it
    stops local ollama processes, starts serve with the env var, waits for readiness,
    and warms nomic-embed-text.
#>
param(
    [int]$NumParallel = 8
)

$ErrorActionPreference = "Stop"
if ($NumParallel -lt 1) { throw "NumParallel must be >= 1" }

$env:OLLAMA_NUM_PARALLEL = "$NumParallel"
Write-Host "Desired OLLAMA_NUM_PARALLEL=$($env:OLLAMA_NUM_PARALLEL)"

function Get-OllamaServePid {
    $procs = Get-CimInstance Win32_Process -Filter "Name='ollama.exe'" -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        if ($p.CommandLine -match '\bserve\b') { return [int]$p.ProcessId }
    }
    # Fallback: any ollama.exe (App often hosts serve in the main process)
    $any = Get-Process -Name "ollama" -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($any) { return [int]$any.Id }
    return 0
}

function Get-ProcessEnvVar {
    param([int]$ProcessId, [string]$Name)
    if ($ProcessId -le 0) { return $null }
    $code = @"
using System;
using System.Runtime.InteropServices;
using System.Text;
public static class EmpireOllamaEnv {
  [DllImport("kernel32.dll")] static extern IntPtr OpenProcess(uint a, bool b, int pid);
  [DllImport("kernel32.dll")] static extern bool CloseHandle(IntPtr h);
  [DllImport("ntdll.dll")] static extern int NtQueryInformationProcess(IntPtr p, int c, ref PBI pbi, int s, out int r);
  [DllImport("kernel32.dll")] static extern bool ReadProcessMemory(IntPtr h, IntPtr a, byte[] b, int n, out IntPtr r);
  [StructLayout(LayoutKind.Sequential)] public struct PBI { public IntPtr a,b,c,d,e,f; }
  public static string Get(int pid, string name) {
    IntPtr h = OpenProcess(0x0410, false, pid);
    if (h == IntPtr.Zero) return null;
    try {
      PBI pbi = new PBI(); int ret;
      if (NtQueryInformationProcess(h, 0, ref pbi, Marshal.SizeOf(pbi), out ret) != 0) return null;
      byte[] buf = new byte[8]; IntPtr r;
      if (!ReadProcessMemory(h, IntPtr.Add(pbi.b, 0x20), buf, 8, out r)) return null;
      IntPtr pp = (IntPtr)BitConverter.ToInt64(buf, 0);
      if (!ReadProcessMemory(h, IntPtr.Add(pp, 0x80), buf, 8, out r)) return null;
      IntPtr env = (IntPtr)BitConverter.ToInt64(buf, 0);
      byte[] e = new byte[65536];
      if (!ReadProcessMemory(h, env, e, e.Length, out r)) return null;
      foreach (var part in Encoding.Unicode.GetString(e).Split(new char[]{'\0'}, StringSplitOptions.RemoveEmptyEntries)) {
        if (part.StartsWith(name + "=", StringComparison.OrdinalIgnoreCase))
          return part.Substring(name.Length + 1);
      }
      return "";
    } finally { CloseHandle(h); }
  }
}
"@
    if (-not ("EmpireOllamaEnv" -as [type])) {
        Add-Type -TypeDefinition $code -ErrorAction Stop
    }
    try {
        return [EmpireOllamaEnv]::Get($ProcessId, $Name)
    }
    catch {
        return $null
    }
}

function Test-OllamaReady {
    try {
        Invoke-RestMethod -Uri "http://localhost:11434/api/tags" -TimeoutSec 2 | Out-Null
        return $true
    }
    catch {
        return $false
    }
}

function Keep-NomicWarm {
    try {
        $body = @{ model = "nomic-embed-text:latest"; input = "warmup"; keep_alive = -1 } | ConvertTo-Json -Compress
        Invoke-RestMethod -Uri "http://localhost:11434/api/embed" -Method Post -Body $body `
            -ContentType "application/json" -TimeoutSec 120 | Out-Null
        Write-Host "Pinned nomic-embed-text:latest (keep_alive=-1)"
    }
    catch {
        Write-Host "WARN: nomic warmup failed: $($_.Exception.Message)"
    }
}

$servePid = Get-OllamaServePid
if ($servePid -gt 0 -and (Test-OllamaReady)) {
    $live = Get-ProcessEnvVar -ProcessId $servePid -Name "OLLAMA_NUM_PARALLEL"
    if ($live -eq "$NumParallel") {
        Write-Host ("ollama serve PID {0} already has OLLAMA_NUM_PARALLEL={1} - skip restart" -f $servePid, $live)
        Keep-NomicWarm
        Write-Host ("Ollama ready on :11434 (OLLAMA_NUM_PARALLEL={0}; unchanged)" -f $NumParallel)
        exit 0
    }
    if ($null -eq $live) {
        Write-Host ("WARN: could not read env for PID {0}; will restart to set OLLAMA_NUM_PARALLEL={1}" -f $servePid, $NumParallel)
    }
    else {
        Write-Host ("Live OLLAMA_NUM_PARALLEL='{0}' (want {1}) - restarting serve" -f $live, $NumParallel)
    }
}
else {
    Write-Host ("Ollama not ready on :11434 - starting serve with OLLAMA_NUM_PARALLEL={0}" -f $NumParallel)
}

Get-Process -Name "ollama*" -ErrorAction SilentlyContinue | ForEach-Object {
    Write-Host "Stopping $($_.Name) PID $($_.Id)..."
    Stop-Process -Id $_.Id -Force -ErrorAction SilentlyContinue
}
Start-Sleep -Seconds 2

if (-not (Get-Command ollama -ErrorAction SilentlyContinue)) {
    throw "ollama not on PATH"
}

# cmd.exe so Windows PowerShell 5.1 and PS7 both pass the env into the serve process.
$cmdLine = "set OLLAMA_NUM_PARALLEL=$NumParallel&& ollama serve"
Write-Host ("Starting ollama serve with OLLAMA_NUM_PARALLEL={0}..." -f $NumParallel)
Start-Process -FilePath "cmd.exe" -ArgumentList @("/c", $cmdLine) -WindowStyle Hidden | Out-Null

$ready = $false
for ($i = 0; $i -lt 40; $i++) {
    if (Test-OllamaReady) {
        $ready = $true
        break
    }
    Start-Sleep -Seconds 1
}
if (-not $ready) {
    throw "Ollama did not become ready on :11434 after restart"
}

$newPid = Get-OllamaServePid
$verify = Get-ProcessEnvVar -ProcessId $newPid -Name "OLLAMA_NUM_PARALLEL"
if ($verify -ne "$NumParallel") {
    Write-Host ("WARN: post-start OLLAMA_NUM_PARALLEL='{0}' (expected {1}) on PID {2}" -f $verify, $NumParallel, $newPid)
}
else {
    Write-Host ("Confirmed OLLAMA_NUM_PARALLEL={0} on serve PID {1}" -f $verify, $newPid)
}

Write-Host ("Ollama ready on :11434 (OLLAMA_NUM_PARALLEL={0})" -f $NumParallel)
Keep-NomicWarm
