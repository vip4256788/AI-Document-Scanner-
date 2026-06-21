import os
import logging
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

# Get Gemini API Key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Use latest stable Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")


def process_with_llm(text: str, prompt: str) -> dict:
    """
    Send OCR text to Gemini and get analysis.
    """

    try:
        full_prompt = f"""
        {prompt}

        Document Text:
        ------------------
        {text}
        ------------------

        Return clear and structured output.
        """

        response = model.generate_content(full_prompt)

        return {
            "response": response.text,
            "model": "gemini-1.5-flash"
        }

    except Exception as e:
        logger.error(f"Gemini Error: {str(e)}")
        raise Exception(f"Gemini API Error: {str(e)}")


def summarize_text(text: str, max_length: int = 300) -> str:
    """
    Generate summary from OCR text.
    """

    try:
        prompt = f"""
        Summarize this document in less than {max_length} characters.
        """

        result = process_with_llm(text, prompt)

        return result["response"]

    except Exception as e:
        logger.error(f"Summary Error: {str(e)}")
        raise


def extract_key_points(text: str) -> list:
    """
    Extract important key points.
    """

    try:
        prompt = """
        Extract important key points from the document.
        Return only bullet points.
        """

        result = process_with_llm(text, prompt)

        lines = result["response"].split("\n")

        points = [
            line.replace("•", "")
                .replace("-", "")
                .strip()
            for line in lines
            if line.strip()
        ]

        return points

    except Exception as e:
        logger.error(f"Key Points Error: {str(e)}")
        raise