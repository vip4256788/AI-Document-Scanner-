# AI Document Scanner - Setup & Deployment Guide

## Overview

The AI Document Scanner is a production-ready FastAPI application that:
1. **Scans** images/PDFs and extracts text using OCR (pytesseract)
2. **Analyzes** extracted text using OpenAI GPT LLM
3. **Generates** semantic embeddings for document content
4. **Stores** uploaded documents with unique IDs
5. **Provides** RESTful API with comprehensive error handling

---

## Part 1: Local Development Setup

### Step 1: Install System Dependencies

#### Windows
1. Download Tesseract installer: https://github.com/UB-Mannheim/tesseract/wiki
2. Run installer (default path: `C:\Program Files\Tesseract-OCR`)
3. Note the installation path for configuration

#### macOS
```bash
brew install tesseract
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get install tesseract-ocr
sudo apt-get install poppler-utils  # For PDF support
```

### Step 2: Set Up Python Environment

```bash
# Navigate to project directory
cd c:\Users\Adm\Downloads\ai_document_scanner

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

1. Copy `.env.example` to `.env`
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` file with your credentials:
   ```
   OPENAI_API_KEY=sk-your-openai-api-key-here
   ```

3. For Windows, if Tesseract is not in PATH, add:
   ```
   TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
   ```

### Step 5: Run the Application

```bash
# Development mode with auto-reload
uvicorn app.main:app --reload

# Or production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

**Access the API:**
- API: http://localhost:8000
- Interactive Docs (Swagger UI): http://localhost:8000/docs
- Alternative Docs (ReDoc): http://localhost:8000/redoc
- Health Check: http://localhost:8000/health

---

## Part 2: API Testing

### Test Using cURL

#### 1. Health Check
```bash
curl http://localhost:8000/health
```

#### 2. Scan Document (OCR only)
```bash
curl -X POST http://localhost:8000/api/v1/scan \
  -F "file=@path/to/your/document.jpg"
```

#### 3. Analyze Document (OCR + LLM Analysis)
```bash
curl -X POST http://localhost:8000/api/v1/analyze \
  -F "file=@path/to/your/document.jpg" \
  -G --data-urlencode "prompt=Summarize this document"
```

#### 4. Generate Embeddings
```bash
curl -X POST http://localhost:8000/api/v1/embed \
  -F "file=@path/to/your/document.jpg"
```

### Test Using Python

```python
import requests
import json

# Scan a document
with open('document.jpg', 'rb') as f:
    response = requests.post(
        'http://localhost:8000/api/v1/scan',
        files={'file': f}
    )
    result = response.json()
    print(json.dumps(result, indent=2))

# Analyze a document
with open('document.jpg', 'rb') as f:
    response = requests.post(
        'http://localhost:8000/api/v1/analyze',
        files={'file': f},
        params={'prompt': 'Extract all product names and prices'}
    )
    result = response.json()
    print(json.dumps(result, indent=2))
```

---

## Part 3: Project Structure Explained

```
ai_document_scanner/
├── app/                          # Main application package
│   ├── main.py                  # FastAPI app initialization
│   ├── routes/
│   │   └── scan.py              # API endpoints (/scan, /analyze, /embed, /status)
│   ├── services/
│   │   ├── ocr.py               # Pytesseract OCR functions
│   │   └── llm.py               # OpenAI API integration
│   └── models/
│       └── document.py          # Pydantic data models (request/response validation)
├── uploads/                      # Stores uploaded documents with UUID filenames
├── config/
│   └── settings.py              # Configuration and environment variables
├── tests/
│   └── test_api.py              # Basic API endpoint tests
├── docs/
│   └── ARCHITECTURE.md          # Architecture documentation
├── requirements.txt             # Python dependencies
├── render.yaml                  # Render.com deployment config
├── README.md                    # User documentation
└── .env.example                 # Environment variables template
```

---

## Part 4: Running Tests

```bash
# Install pytest
pip install pytest pytest-cov

# Run tests
pytest tests/

# Run tests with coverage
pytest tests/ --cov=app
```

---

## Part 5: Deployment to Render.com

### Prerequisites
1. GitHub account with your repository
2. Render.com account (free tier available)
3. OpenAI API key

### Deployment Steps

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: AI Document Scanner"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/ai-document-scanner.git
   git push -u origin main
   ```

2. **Connect to Render**
   - Go to https://render.com
   - Click "New +"
   - Select "Web Service"
   - Connect your GitHub repository
   - Render will automatically detect `render.yaml`

3. **Configure Environment**
   - In Render dashboard, go to Environment
   - Add environment variable: `OPENAI_API_KEY=sk-your-key`
   - Deploy!

4. **Monitor Deployment**
   - View logs in real-time
   - API will be available at `https://your-app-name.onrender.com`

---

## Part 6: Production Deployment Checklist

- [ ] OPENAI_API_KEY is set and valid
- [ ] Tesseract OCR is installed on deployment server
- [ ] All dependencies in requirements.txt are correct
- [ ] `.env` file is NOT committed to git
- [ ] Tests pass successfully
- [ ] API health check passes
- [ ] File upload permissions configured
- [ ] Error logging enabled
- [ ] Rate limiting considered (for production)
- [ ] Database backup strategy (if using DB)

---

## Part 7: API Endpoints Reference

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| POST | `/api/v1/scan` | OCR text extraction |
| POST | `/api/v1/analyze` | OCR + LLM analysis |
| POST | `/api/v1/embed` | OCR + embeddings |
| GET | `/api/v1/status/{file_id}` | File status check |

---

## Part 8: Troubleshooting

### Issue: "tesseract is not installed or it's not in your PATH"

**Solution:**
1. Install Tesseract (see system dependencies)
2. Add to PATH or set `TESSERACT_PATH` in `.env`
3. Restart the application

### Issue: "Invalid OPENAI_API_KEY"

**Solution:**
1. Verify API key format (starts with `sk-`)
2. Check API key has not expired at https://platform.openai.com/account/api-keys
3. Ensure no extra whitespace in `.env` file

### Issue: "File upload fails with 413 error"

**Solution:**
1. Reduce file size (max recommended: 50MB)
2. Or increase `MAX_UPLOAD_SIZE` in `config/settings.py`

### Issue: "PDF processing hangs"

**Solution:**
1. Ensure `poppler-utils` is installed (Linux)
2. Try with a smaller PDF first
3. Check system memory availability

---

## Part 9: Performance Optimization

### For Large Documents
- Implement image preprocessing to improve OCR accuracy
- Use batching for multiple documents
- Consider implementing caching for frequently analyzed documents

### For High Traffic
- Set up API rate limiting
- Use a production ASGI server (Gunicorn with Uvicorn workers)
- Implement database for document history
- Use Redis for caching

---

## Part 10: Security Best Practices

1. **Never commit `.env` file** to git
2. **Rotate API keys** regularly
3. **Validate file uploads** (size, format, content)
4. **Use HTTPS** in production
5. **Implement authentication** for API endpoints
6. **Monitor logs** for suspicious activity
7. **Keep dependencies updated** regularly

---

## Support & Next Steps

- Check logs: `logs/` directory (implement logging as needed)
- Review API documentation: Interactive docs at `/docs`
- Test endpoints: Use Swagger UI at `/docs`
- Read code: Start with `app/main.py`

Happy document scanning! 📄✨
