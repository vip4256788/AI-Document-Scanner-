from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class ScanResult(BaseModel):
    file_id: str
    filename: str
    extracted_text: str
    timestamp: datetime
    file_path: Optional[str] = None

class AnalysisResult(BaseModel):
    file_id: str
    filename: str
    extracted_text: str
    analysis: dict
    timestamp: datetime

class EmbeddingResult(BaseModel):
    file_id: str
    filename: str
    extracted_text: str
    embedding: List[float]
    embedding_dimension: int
    timestamp: datetime

class DocumentMetadata(BaseModel):
    file_id: str
    filename: str
    file_size: int
    file_type: str
    upload_timestamp: datetime
    processing_status: str

class KeyPoints(BaseModel):
    key_points: List[str]
    count: int

class Summary(BaseModel):
    summary: str
    original_length: int
    summary_length: int
