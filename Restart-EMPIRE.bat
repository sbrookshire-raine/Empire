@echo off
setlocal EnableExtensions
cd /d "%~dp0"

title EMPIRE Restart (stop, npm build, start)

echo.
echo EMPIRE restart
echo ==============
echo Stop Eve/Workbench/PocketBase, rebuild Eve, then start the stack.
echo Ollama and Docker stay up unless you pass /full
echo.

set "KEEP_OLLAMA=1"
set "KEEP_DOCKER=1"
if /I "%~1"=="/full" (
    set "KEEP_OLLAMA=0"
    set "KEEP_DOCKER=0"
)

echo [1/3] Shutdown...
set "STOP_EMPIRE_NO_PAUSE=1"
if "%KEEP_OLLAMA%"=="1" (
    call "%~dp0Stop-EMPIRE.bat" /keep-ollama /keep-docker
) else (
    call "%~dp0Stop-EMPIRE.bat"
)
if errorlevel 1 (
    echo Shutdown reported an error. Continuing to rebuild.
)

echo.
echo [2/3] npm run build (agents\empire-task-agent)...
cd /d "%~dp0agents\empire-task-agent"
call npm.cmd run build
if errorlevel 1 (
    echo.
    echo Eve npm build failed. Fix the error above, then run Start-EMPIRE.bat.
    echo.
    pause
    exit /b 1
)
cd /d "%~dp0"

echo.
echo [3/3] Startup...
call "%~dp0Start-EMPIRE.bat"
exit /b %ERRORLEVEL%
