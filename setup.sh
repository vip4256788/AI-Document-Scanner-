#!/bin/bash

# AI Document Scanner - Quick Start Script for macOS/Linux

echo ""
echo "============================================"
echo "AI Document Scanner - Quick Start"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    exit 1
fi

echo "[1/4] Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Created: venv/"
else
    echo "Virtual environment already exists"
fi

echo ""
echo "[2/4] Activating virtual environment..."
source venv/bin/activate

echo ""
echo "[3/4] Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "[4/4] Configuration..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "Created .env file from template"
    echo "Please edit .env and add your OPENAI_API_KEY"
else
    echo ".env file already exists"
fi

echo ""
echo "============================================"
echo "Setup Complete!"
echo "============================================"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your OpenAI API key"
echo "2. Run: uvicorn app.main:app --reload"
echo "3. Open: http://localhost:8000/docs"
echo ""
