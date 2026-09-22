@echo off
REM ====================================================================
REM  LAMMPS Workbench launcher (Windows cmd / PowerShell)
REM  Usage: double-click, or run .\start.bat from the repo root.
REM  URL  : http://127.0.0.1:8000
REM
REM  Behavior:
REM    1. checks uv
REM    2. checks frontend dist (warn + confirm if missing)
REM    3. starts uvicorn in the FOREGROUND (so Ctrl+C cleanly stops it)
REM    4. a tiny background watcher polls port 8000 and opens the
REM       default browser once it answers. The watcher does NOT block
REM       the foreground uvicorn -- when you Ctrl+C, the whole window
REM       closes and the watcher dies with the console.
REM
REM  ASCII-only on purpose so it works under any system codepage.
REM ====================================================================

cd /d "%~dp0"

set "LOG=%~dp0start.log"
> "%LOG%" echo === LAMMPS Workbench launcher ===
>>"%LOG%" echo CWD: %cd%
>>"%LOG%" echo When: %date% %time%
>>"%LOG%" echo.

echo === LAMMPS Workbench - launching ===
echo CWD: %cd%
echo Log: %LOG%
echo.

echo --- step 1/4: check uv ---
where uv >nul 2>nul
if errorlevel 1 goto :err_uv
echo [OK] uv found
>>"%LOG%" echo [OK] uv found

echo.
echo --- step 2/4: check frontend dist ---
if exist "workbench\frontend\dist\index.html" goto :frontend_ok
echo [WARN] workbench\frontend\dist\index.html not found.
echo        Frontend not built. Visit "/" in browser will 404.
echo        Build:  cd workbench\frontend ^&^& npm install ^&^& npm run build
echo.
set /p CONTINUE=Start backend anyway (API only)? [y/N]:
if /i "%CONTINUE%"=="y" goto :frontend_ok
echo Cancelled.
>>"%LOG%" echo [CANCEL] user declined to continue without frontend
goto :err_cancel

:frontend_ok
echo [OK] frontend dist found (or user chose to continue)
>>"%LOG%" echo [OK] frontend step passed

echo.
echo --- step 3/4: launch uv run workbench (foreground) ---
echo Server will be at: http://127.0.0.1:8000
echo Press Ctrl+C in THIS window to stop the server.
echo.

REM Start uvicorn truly in foreground so Ctrl+C in this window stops it.
REM We launch it with `start /WAIT /B` so this batch pauses but stays
REM attached.  The `start /WAIT` makes the parent block until the child
REM exits; `/B` keeps the child in the same console (so Ctrl+C reaches
REM uvicorn).  Once the user Ctrl+Cs, the batch resumes, reaches :end,
REM and the whole window closes -- the browser watcher started below
REM is bound to this console, so it dies too. Clean shutdown.

REM First, kick off the browser watcher in a fully detached process so
REM it can't block uvicorn. `start /B` in a new cmd title is enough.
start "browser-watcher" /B cmd /c ""%~dp0start_browser.bat""

echo --- step 4/4: browser auto-open (watcher started) ---
echo.
start "uvicorn" /WAIT /B cmd /c "uv run workbench"
set "RC=%errorlevel%"

>>"%LOG%" echo uvicorn exit=%RC%
if not "%RC%"=="0" goto :err_uvrun
>>"%LOG%" echo clean exit
echo Done.
goto :end

:err_uv
echo [ERROR] uv not found in PATH. Install: https://docs.astral.sh/uv/
>>"%LOG%" echo [FATAL] uv missing
goto :end

:err_cancel
>>"%LOG%" echo [CANCEL] user cancelled
goto :end

:err_uvrun
echo [ERROR] uv run workbench exited with code %RC%.
>>"%LOG%" echo [FATAL] uvicorn exit %RC%

:end
echo.
echo === See %LOG% for full log ===
pause
exit /b 0
