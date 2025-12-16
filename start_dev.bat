@echo off
chcp 65001 >nul
setlocal

echo ===================================================
echo Starting Script2Image-Video Development Environment
echo ===================================================

:: Backend
echo.
echo [Backend] Checking configuration...
cd backend
if exist ".venv\Scripts\activate.bat" (
    echo    Found .venv, activating...
    set "PYTHON_CMD=call .venv\Scripts\activate.bat && python"
) else if exist "venv\Scripts\activate.bat" (
    echo    Found venv, activating...
    set "PYTHON_CMD=call venv\Scripts\activate.bat && python"
) else (
    echo    No virtual environment found, using system python...
    set "PYTHON_CMD=python"
)

echo Starting Backend Server...
start "Backend Server (Script2Image)" cmd /k "%PYTHON_CMD% -m uvicorn main:app --reload --host 0.0.0.0 --port 8000"
cd ..

:: Frontend
echo.
echo [Frontend] Starting...
cd frontend
echo Starting Frontend Server...
start "Frontend Server (Script2Image)" cmd /k "npm run dev"
cd ..

echo.
echo ===================================================
echo Services are launching in separate windows.
echo.
echo    Backend:  http://localhost:8000
echo    Frontend: http://localhost:5173
echo.
echo    Close this window to exit the launcher 
echo    (Services will keep running in their own windows)
echo ===================================================
pause
