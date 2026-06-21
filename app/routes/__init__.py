"""
Routes Package - API Endpoint Handlers

This module contains all FastAPI route definitions for the document scanner API.

Routes:
    - scan: POST /api/v1/scan - Extract text from documents (OCR only)
    - analyze: POST /api/v1/analyze - Analyze documents with AI
    - embed: POST /api/v1/embed - Generate embeddings
    - status: GET /api/v1/status/{file_id} - Check file status

Usage:
    from app.routes.scan import router
"""

from app.routes.scan import router as scan_router

__all__ = ['scan_router']