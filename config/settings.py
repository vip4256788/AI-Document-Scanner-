import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings loaded from environment variables."""
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    TESSERACT_PATH = os.getenv("TESSERACT_PATH", None)
    
    # Application settings
    APP_NAME = "AI Document Scanner"
    APP_VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # Upload settings
    UPLOAD_DIR = "uploads"
    MAX_UPLOAD_SIZE = 50 * 1024 * 1024  # 50 MB
    ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".pdf", ".bmp", ".tiff"}
    
    # OpenAI settings
    OPENAI_MODEL = "gpt-3.5-turbo"
    OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"
    OPENAI_TEMPERATURE = 0.7
    OPENAI_MAX_TOKENS = 1000

settings = Settings()
