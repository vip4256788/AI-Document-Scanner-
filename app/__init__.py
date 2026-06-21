"""
AI Document Scanner - Main Application Package

This package contains the FastAPI application for document scanning,
OCR processing, and AI-powered document analysis.

Modules:
    - routes: API endpoint handlers
    - services: Business logic (OCR, LLM)
    - models: Data validation models (Pydantic)

Usage:
    from app.main import app
"""

__version__ = "1.0.0"
__author__ = "AI Document Scanner Team"
__description__ = "Production-ready AI-powered document scanner with OCR and LLM analysis"

# Package metadata
__all__ = ['main', 'routes', 'services', 'models']