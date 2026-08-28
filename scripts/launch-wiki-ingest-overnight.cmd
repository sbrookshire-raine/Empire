@echo off
REM Detached Cursor-safe overnight wiki ingest launcher.
REM Windows "start" treats the FIRST quoted arg as the WINDOW TITLE, not a program.
REM Wrong:  cmd /c start "EMPIRE-wiki-2017" /MIN cmd /c "..."
REM         -> ERROR: The system cannot find the file EMPIRE-wiki-2017.
REM Right:  start "title" /MIN powershell.exe -File ...

setlocal
for %%I in ("%~dp0..") do set "ROOT=%%~fI"
set "YEAR=%~1"
if "%YEAR%"=="" set "YEAR=2017"
set "FILELIMIT=%~2"
if "%FILELIMIT%"=="" set "FILELIMIT=200"
set "MAXSLICES=%~3"
if "%MAXSLICES%"=="" set "MAXSLICES=300"
set "MAXHOURS=%~4"
if "%MAXHOURS%"=="" set "MAXHOURS=23"
set "FLUSHEVERY=%~5"
if "%FLUSHEVERY%"=="" set "FLUSHEVERY=50"

REM Must be set on ollama serve (not only ingest). Default 8 for nomic-only Fast Mode.
if "%OLLAMA_NUM_PARALLEL%"=="" set "OLLAMA_NUM_PARALLEL=8"
echo Ensuring Ollama with OLLAMA_NUM_PARALLEL=%OLLAMA_NUM_PARALLEL%...
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%ROOT%\scripts\ensure-ollama-parallel.ps1" -NumParallel %OLLAMA_NUM_PARALLEL%
if errorlevel 1 (
  echo ERROR: ensure-ollama-parallel.ps1 failed - overnight not launched.
  exit /b 1
)

start "EMPIRE-wiki-%YEAR%" /MIN powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%ROOT%\scripts\start-wiki-ingest-overnight.ps1" -Year %YEAR% -FileLimit %FILELIMIT% -MaxSlices %MAXSLICES% -MaxHours %MAXHOURS% -FlushEvery %FLUSHEVERY%
echo Launched minimized overnight wiki ingest year=%YEAR% FileLimit=%FILELIMIT% MaxSlices=%MAXSLICES% MaxHours=%MAXHOURS% FlushEvery=%FLUSHEVERY% OLLAMA_NUM_PARALLEL=%OLLAMA_NUM_PARALLEL%
echo PID file: I:\EMPIRE_DATA\logs\wiki-ingest-overnight-%YEAR%.pid
endlocal
