#!/bin/bash

# Script2Image-Video Startup Script for macOS/Linux

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Starting Script2Image-Video Development Environment...${NC}"

# Function to kill processes on exit
cleanup() {
    echo -e "\n${RED}🛑 Stopping services...${NC}"
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

# Trap SIGINT (Ctrl+C)
trap cleanup SIGINT

# 1. Start Backend
echo -e "${GREEN}📦 Starting Backend Server...${NC}"
cd backend

# Check for virtual environment
if [ -d ".venv" ]; then
    echo "   Activating virtual environment (.venv)..."
    source .venv/bin/activate
elif [ -d "venv" ]; then
    echo "   Activating virtual environment (venv)..."
    source venv/bin/activate
fi

# Install dependencies if needed (optional check)
# pip install -r requirements.txt

# Run Uvicorn in background
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd ..

# 2. Start Frontend
echo -e "${GREEN}🎨 Starting Frontend Server...${NC}"
cd frontend

# Run Vite in background
npm run dev &
FRONTEND_PID=$!
cd ..

echo -e "${BLUE}===================================================${NC}"
echo -e "${GREEN}✅ Services are running!${NC}"
echo -e "   Backend:  http://localhost:8000"
echo -e "   Frontend: http://localhost:5173"
echo -e "${BLUE}===================================================${NC}"
echo -e "Press Ctrl+C to stop all services."

# Wait for processes
wait
