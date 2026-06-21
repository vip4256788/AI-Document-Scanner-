from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from datetime import datetime
import os
import uuid

from app.services.ocr import extract_text_from_image
from app.services.llm import process_with_llm

router = APIRouter(prefix="/api/v1", tags=["scan"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# 🔹 Helper function to validate, save, extract and cleanup
async def save_and_extract(file: UploadFile):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required")

    file_extension = os.path.splitext(file.filename)[1].lower()

    if file_extension not in ['.jpg', '.jpeg', '.png', '.pdf', '.bmp', '.tiff']:
        raise HTTPException(
            status_code=400,
            detail="Invalid file format. Supported: JPG, JPEG, PNG, PDF, BMP, TIFF"
        )

    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}{file_extension}")

    try:
        contents = await file.read()

        with open(file_path, "wb") as f:
            f.write(contents)

        extracted_text = extract_text_from_image(file_path)

        if not extracted_text.strip():
            raise HTTPException(
                status_code=400,
                detail="No text could be extracted from the file"
            )

        return file_id, file_path, extracted_text

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File processing error: {str(e)}")


# 🔹 1. OCR ONLY
@router.post("/scan")
async def scan_document(file: UploadFile = File(...)):
    """
    Upload document → Extract text using OCR
    """
    file_id, file_path, extracted_text = await save_and_extract(file)

    # Clean up file after processing
    if os.path.exists(file_path):
        os.remove(file_path)

    return {
        "file_id": file_id,
        "filename": file.filename,
        "extracted_text": extracted_text,
        "timestamp": datetime.utcnow()
    }


# 🔹 2. OCR + LLM ANALYSIS
@router.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    prompt: str = Query(None, description="Custom prompt for analysis")
):
    """
    Upload document → OCR → LLM (Gemini) analysis
    """
    file_id, file_path, extracted_text = await save_and_extract(file)

    try:
        default_prompt = """
        Analyze this document and provide:
        1. Document type
        2. Summary
        3. Key points
        4. Hindi translation
        """

        analysis_prompt = prompt or default_prompt

        analysis_result = process_with_llm(extracted_text, analysis_prompt)

        return {
            "file_id": file_id,
            "filename": file.filename,
            "extracted_text": extracted_text,
            "analysis": analysis_result,
            "timestamp": datetime.utcnow()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis error: {str(e)}")

    finally:
        # Always delete file (even if error happens)
        if os.path.exists(file_path):
            os.remove(file_path)


# 🔹 3. STATUS CHECK (Optional)
@router.get("/status/{file_id}")
async def get_status(file_id: str):
    """
    Check if a file exists (basic status)
    """
    for file in os.listdir(UPLOAD_DIR):
        if file.startswith(file_id):
            return {
                "file_id": file_id,
                "status": "processed",
                "filename": file
            }

    raise HTTPException(status_code=404, detail="File not found")