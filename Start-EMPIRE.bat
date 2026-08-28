@echo off
setlocal
cd /d "%~dp0"

title EMPIRE Launcher

echo.
echo Starting EMPIRE (Ollama, PocketBase, Workbench, Eve)...
echo.

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\launch-empire.ps1"
if errorlevel 1 (
    echo.
    echo EMPIRE failed to start. See the message above.
    echo.
    pause
    exit /b 1
)

echo Press any key to close this window. EMPIRE keeps running in the background.
pause >nul
exit /b 0
