# AI Document Scanner

A production-ready AI-powered document scanning and analysis API built with FastAPI, OCR, and OpenAI LLM integration.

## Features

- **OCR Document Scanning**: Extract text from images (JPG, PNG, BMP, TIFF) and PDFs using pytesseract
- **LLM-based Analysis**: Analyze extracted text using OpenAI GPT models
- **Text Embeddings**: Generate semantic embeddings for document content
- **RESTful API**: FastAPI-powered endpoints for all operations
- **Error Handling**: Comprehensive error handling and validation
- **CORS Support**: Cross-origin resource sharing enabled
- **Health Checks**: API health monitoring endpoints

## Project Structure

```
ai_document_scanner/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── routes/
│   │   ├── __init__.py
│   │   └── scan.py            # Document scanning routes
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ocr.py             # OCR functionality
│   │   └── llm.py             # LLM and embedding services
│   └── models/
│       ├── __init__.py
│       └── document.py        # Pydantic data models
├── uploads/                    # Directory for storing uploaded documents
├── config/                     # Configuration files
├── tests/                      # Test suite
├── docs/                       # Documentation
├── requirements.txt            # Python dependencies
├── render.yaml                 # Render deployment configuration
└── README.md                   # This file
```

## Prerequisites

- Python 3.8+
- Tesseract OCR engine installed on your system
- OpenAI API key
- pip (Python package manager)

## Installation

### 1. Clone or Setup the Repository

```bash
cd ai_document_scanner
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Tesseract OCR

**Windows:**
1. Download the installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Run the installer and note the installation path (default: `C:\Program Files\Tesseract-OCR`)
3. Add Tesseract to PATH or configure it in your code

**macOS:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tesseract-ocr
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key_here
TESSERACT_PATH=/path/to/tesseract  # Windows only if not in PATH
```

## Running the Application

### Local Development

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Production

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

### 1. Health Check

**GET** `/health`

Returns API health status.

**Response:**
```json
{
  "status": "healthy"
}
```

### 2. Root Endpoint

**GET** `/`

Returns API information.

**Response:**
```json
{
  "message": "AI Document Scanner API",
  "status": "running"
}
```

### 3. Scan Document

**POST** `/api/v1/scan`

Uploads a document and extracts text using OCR.

**Request:**
- Content-Type: multipart/form-data
- Parameter: `file` (image or PDF file)

**Response:**
```json
{
  "file_id": "550e8400-e29b-41d4-a716-446655440000",
  "filename": "document.jpg",
  "extracted_text": "Extracted text from the document...",
  "timestamp": "2024-01-01T12:00:00",
  "file_path": "uploads/550e8400-e29b-41d4-a716-446655440000.jpg"
}
```

### 4. Analyze Document

**POST** `/api/v1/analyze`

Uploads a document, extracts text, and analyzes it using OpenAI LLM.

**Request:**
- Content-Type: multipart/form-data
- Parameter: `file` (image or PDF file)
- Query Parameter: `prompt` (optional, custom analysis prompt)

**Response:**
```json
{
  "file_id": "550e8400-e29b-41d4-a716-446655440000",
  "filename": "document.jpg",
  "extracted_text": "Extracted text...",
  "analysis": {
    "response": "AI-generated analysis...",
    "tokens_used": 150,
    "model": "gpt-3.5-turbo"
  },
  "timestamp": "2024-01-01T12:00:00"
}
```

### 5. Generate Embeddings

**POST** `/api/v1/embed`

Uploads a document and generates embeddings for its content.

**Request:**
- Content-Type: multipart/form-data
- Parameter: `file` (image or PDF file)

**Response:**
```json
{
  "file_id": "550e8400-e29b-41d4-a716-446655440000",
  "filename": "document.jpg",
  "extracted_text": "Extracted text...",
  "embedding": [0.1234, -0.5678, ...],
  "embedding_dimension": 1536,
  "timestamp": "2024-01-01T12:00:00"
}
```

### 6. Get File Status

**GET** `/api/v1/status/{file_id}`

Retrieves the status of a previously processed document.

**Response:**
```json
{
  "file_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "processed",
  "filename": "document.jpg"
}
```

## Supported File Formats

- JPG/JPEG
- PNG
- BMP
- TIFF
- PDF

## Technology Stack

- **Framework**: FastAPI
- **Server**: Uvicorn
- **OCR**: pytesseract + Tesseract
- **LLM**: OpenAI GPT-3.5-turbo
- **Embeddings**: OpenAI text-embedding-3-small
- **Data Validation**: Pydantic
- **PDF Processing**: pdf2image + poppler

## Deployment

### Render Deployment

The project includes a `render.yaml` configuration for easy deployment to Render.

1. Push your code to GitHub
2. Connect your GitHub account to Render
3. Create a new Web Service and select your repository
4. Render will automatically detect and use the `render.yaml` configuration
5. Set the `OPENAI_API_KEY` environment variable in Render dashboard
6. Deploy!

**Note**: Render's free tier has limitations. For production use, consider upgrading the plan.

## Error Handling

The API provides detailed error responses:

```json
{
  "detail": "Invalid file format. Supported: JPG, JPEG, PNG, PDF, BMP, TIFF"
}
```

Common HTTP Status Codes:
- `200`: Success
- `400`: Bad Request (invalid file format, missing parameters)
- `404`: Not Found (file not found)
- `500`: Internal Server Error

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for LLM and embeddings | Yes |
| `TESSERACT_PATH` | Path to Tesseract executable (Windows only if not in PATH) | No |

## Example Usage

### Using cURL

```bash
# Scan a document
curl -X POST "http://localhost:8000/api/v1/scan" \
  -F "file=@document.jpg"

# Analyze a document
curl -X POST "http://localhost:8000/api/v1/analyze" \
  -F "file=@document.jpg" \
  -G --data-urlencode "prompt=Identify all names and locations"

# Generate embeddings
curl -X POST "http://localhost:8000/api/v1/embed" \
  -F "file=@document.jpg"
```

### Using Python

```python
import requests

# Scan a document
with open('document.jpg', 'rb') as f:
    response = requests.post(
        'http://localhost:8000/api/v1/scan',
        files={'file': f}
    )
    print(response.json())
```

## Contributing

Contributions are welcome! Please ensure:
- Code follows PEP 8 style guidelines
- Tests are included for new features
- Documentation is updated accordingly

## License

MIT License

## Support

For issues or questions, please open an issue on GitHub.

## Future Enhancements

- Database integration for document storage and history
- User authentication and authorization
- Batch document processing
- Advanced image preprocessing for better OCR accuracy
- Multi-language support
- Document classification
- Table extraction from documents
- API rate limiting
- Caching for frequently analyzed documents
