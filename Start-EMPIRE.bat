@echo off
setlocal
cd /d "%~dp0"

title EMPIRE Launcher

set "LAUNCH_FLAGS=-SkipStartupChecks"
if /I "%~1"=="-Verify" (
    set "LAUNCH_FLAGS="
    shift
)
if /I "%~1"=="/Verify" (
    set "LAUNCH_FLAGS="
    shift
)

echo.
echo Starting EMPIRE (Ollama 24k, PocketBase, Workbench, Eve; Voice/Wiki only if toolbelt ON)...
echo Default: quick start. Full wiki query battery: Start-EMPIRE.bat -Verify
echo Optional: -NoVoice  -NoWiki  -Weaviate (force wiki stack)
echo.

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\launch-empire.ps1" %LAUNCH_FLAGS% %*
if errorlevel 1 (
    echo.
    echo EMPIRE failed to start. See the message above.
    echo Common fixes: open Docker Desktop, then retry; or Start-EMPIRE.bat -NoWiki
    echo.
    pause
    exit /b 1
)

echo Press any key to close this window. EMPIRE keeps running in the background.
pause >nul
exit /b 0
