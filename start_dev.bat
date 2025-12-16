@echo off
echo Starting Script2Image-Video Development Environment...

:: Start Backend
echo Starting Backend Server...
start "Backend Server" cmd /k "cd backend && python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000"

:: Start Frontend
echo Starting Frontend Server...
start "Frontend Server" cmd /k "cd frontend && npm run dev"

echo ===================================================
echo Services are starting in separate windows.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo ===================================================
pause
