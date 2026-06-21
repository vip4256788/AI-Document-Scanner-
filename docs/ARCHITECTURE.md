# AI Document Scanner Documentation

## Quick Start

1. Install dependencies: `pip install -r requirements.txt`
2. Set up environment variables (see `.env.example`)
3. Run the app: `uvicorn app.main:app --reload`
4. Access API docs: `http://localhost:8000/docs`

## API Documentation

See README.md for comprehensive API endpoint documentation.

## Architecture

### Components

1. **FastAPI Application** (`app/main.py`)
   - Initializes FastAPI app
   - Configures middleware (CORS)
   - Registers routes

2. **Routes** (`app/routes/scan.py`)
   - `/scan`: OCR scanning endpoint
   - `/analyze`: LLM analysis endpoint
   - `/embed`: Embedding generation endpoint
   - `/status/{file_id}`: Status check endpoint

3. **Services**
   - **OCR Service** (`app/services/ocr.py`): Pytesseract integration
   - **LLM Service** (`app/services/llm.py`): OpenAI API integration

4. **Models** (`app/models/document.py`)
   - Pydantic models for request/response validation

## Environment Setup

1. Create `.env` file with your OpenAI API key
2. Install Tesseract OCR on your system
3. Update `TESSERACT_PATH` if needed (Windows)

## Deployment

Use `render.yaml` for automatic deployment to Render platform.
