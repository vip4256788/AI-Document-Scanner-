import pytesseract
from PIL import Image
import os
import logging
from pdf2image import convert_from_path

logger = logging.getLogger(__name__)

# Optional: Set path if Tesseract not in PATH (Windows)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_image(file_path: str) -> str:
    try:
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == '.pdf':
            pages = convert_from_path(file_path)
            texts = []

            for page in pages:
                texts.append(pytesseract.image_to_string(page))

            return "\n".join(texts).strip()

        else:
            image = Image.open(file_path).convert("RGB")
            text = pytesseract.image_to_string(image)
            return text.strip()

    except Exception as e:
        logger.error(f"OCR Error: {str(e)}")
        raise


def extract_text_with_config(file_path: str, config: str = "") -> str:
    try:
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == '.pdf':
            pages = convert_from_path(file_path)
            texts = []

            for page in pages:
                texts.append(pytesseract.image_to_string(page, config=config))

            return "\n".join(texts).strip()

        else:
            image = Image.open(file_path).convert("RGB")
            text = pytesseract.image_to_string(image, config=config)
            return text.strip()

    except Exception as e:
        logger.error(f"OCR Config Error: {str(e)}")
        raise


def get_image_data(file_path: str) -> dict:
    try:
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == '.pdf':
            pages = convert_from_path(file_path)

            data = {
                "num_pages": len(pages),
                "text": "",
                "pages": []
            }

            for i, page in enumerate(pages):
                page_text = pytesseract.image_to_string(page)

                data["text"] += page_text + "\n"

                data["pages"].append({
                    "page_num": i + 1,
                    "text": page_text.strip()
                })

            return data

        else:
            image = Image.open(file_path).convert("RGB")
            text = pytesseract.image_to_string(image)

            return {
                "width": image.width,
                "height": image.height,
                "format": image.format,
                "text": text.strip()
            }

    except Exception as e:
        logger.error(f"Image Data Error: {str(e)}")
        raise
