@echo off
REM AI Document Scanner - Quick Start Script for Windows

echo.
echo ============================================
echo AI Document Scanner - Quick Start
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    pause
    exit /b 1
)

echo [1/4] Creating virtual environment...
if not exist venv (
    python -m venv venv
    echo Created: venv/
) else (
    echo Virtual environment already exists
)

echo.
echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/4] Installing dependencies...
pip install -r requirements.txt

echo.
echo [4/4] Configuration...
if not exist .env (
    copy .env.example .env
    echo Created .env file from template
    echo Please edit .env and add your OPENAI_API_KEY
) else (
    echo .env file already exists
)

echo.
echo ============================================
echo Setup Complete!
echo ============================================
echo.
echo Next steps:
echo 1. Edit .env file with your OpenAI API key
echo 2. Run: uvicorn app.main:app --reload
echo 3. Open: http://localhost:8000/docs
echo.
pause
