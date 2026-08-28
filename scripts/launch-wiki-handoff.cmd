@echo off
REM Detached handoff: wait overnight STOPPED -> wiki-maintenance -> overnight MaxHours 24
REM Use this launcher (not hand-rolled cmd start) to avoid the Windows start TITLE-as-exe bug.
REM Wrong:  cmd /c start "EMPIRE-wiki-handoff-2017" /MIN cmd /c "..."
REM         -> ERROR: The system cannot find the file EMPIRE-wiki-handoff-2017.
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
if "%MAXHOURS%"=="" set "MAXHOURS=24"
set "FLUSHEVERY=%~5"
if "%FLUSHEVERY%"=="" set "FLUSHEVERY=50"

cd /d "%ROOT%"
start "EMPIRE-wiki-handoff-%YEAR%" /MIN powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%ROOT%\scripts\wiki-handoff-after-overnight.ps1" -Year %YEAR% -FileLimit %FILELIMIT% -MaxSlices %MAXSLICES% -MaxHours %MAXHOURS% -FlushEvery %FLUSHEVERY% -PollSeconds 30
echo Launched handoff watcher year=%YEAR% FileLimit=%FILELIMIT% MaxSlices=%MAXSLICES% MaxHours=%MAXHOURS% FlushEvery=%FLUSHEVERY%
echo Handoff PID file: I:\EMPIRE_DATA\logs\wiki-handoff-after-overnight-%YEAR%.pid
echo Handoff logs: I:\EMPIRE_DATA\logs\wiki-handoff-after-overnight-%YEAR%-*.log
endlocal
