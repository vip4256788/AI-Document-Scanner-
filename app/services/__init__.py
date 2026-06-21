"""
Services Package - Business Logic Layer

This module contains reusable business logic for:
    - OCR: Text extraction from images and PDFs using pytesseract
    - LLM: AI-powered document analysis using OpenAI
    - Embeddings: Semantic vector generation for documents

Services:
    - ocr.py: Pytesseract OCR functions
    - llm.py: OpenAI LLM and embeddings integration

Usage:
    from app.services.ocr import extract_text_from_image
    from app.services.llm import analyze_text, generate_embeddings
"""

from app.services import ocr, llm

__all__ = ['ocr', 'llm']