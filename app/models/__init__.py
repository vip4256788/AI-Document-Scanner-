"""
Models Package - Data Validation & Schemas

This module contains Pydantic models for request/response validation
and data integrity across the API.

Models:
    - Document: Core document data model
    - ScanRequest: Request model for document scanning
    - ScanResponse: Response model for scan operations
    - AnalysisResponse: Response model for analysis operations
    - EmbeddingResponse: Response model for embedding generation
    - StatusResponse: Response model for status checks

Usage:
    from app.models.document import ScanResponse, AnalysisResponse
"""

from app.models.document import (
    ScanResponse,
    AnalysisResponse,
    EmbeddingResponse,
    StatusResponse,
    FileMetadata
)

__all__ = [
    'ScanResponse',
    'AnalysisResponse',
    'EmbeddingResponse',
    'StatusResponse',
    'FileMetadata'
]