from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os

from app.routes import scan

app = FastAPI(
    title="AI Document Scanner",
    description="OCR and AI-powered document scanning and analysis API",
    version="1.0.0"
)

# 🔹 CORS (allow all for now - change later for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Include API routes
app.include_router(scan.router)


# 🔹 Root endpoint
@app.get("/")
async def root():
    return {
        "message": "AI Document Scanner API",
        "status": "running"
    }


# 🔹 Health check (used by deployment platforms)
@app.get("/health")
async def health():
    return {"status": "healthy"}


# 🔹 Global error handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "error": str(exc)
        },
    )


# 🔹 Run locally
if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))  # Render uses PORT

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )