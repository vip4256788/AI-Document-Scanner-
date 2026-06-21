import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"

def test_health():
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_scan_missing_file():
    """Test scan endpoint without file."""
    response = client.post("/api/v1/scan")
    assert response.status_code == 422

def test_invalid_file_format():
    """Test scan endpoint with invalid file format."""
    response = client.post(
        "/api/v1/scan",
        files={"file": ("test.txt", b"test content")}
    )
    assert response.status_code == 400
