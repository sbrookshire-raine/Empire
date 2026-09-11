@echo off
setlocal
cd /d "%~dp0\.."
title EMPIRE Wiki Chat Smoke

echo.
echo Wiki chat smoke (injection + live Eve)
echo Requires: stack up + Weaviate on :8091
echo.

set "PYTHONPATH=%CD%"
".\venv\Scripts\python.exe" ".\scripts\test-wiki-chat-smoke.py"
set "RC=%ERRORLEVEL%"
echo.
if "%RC%"=="0" (
    echo PASS
) else (
    echo FAIL exit %RC%
)
pause
exit /b %RC%
