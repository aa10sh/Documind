from pathlib import Path

from backend.config.settings import RAW_DOCS_DIR
from backend.config.logging import logger
from backend.utils.file_loader import load_document
from backend.rag.generator import generate_summary



# Summarize Uploaded Document
def summarize_document(filename: str):
    """
    Generates summary of a previously uploaded document.
    """

    file_path = Path(RAW_DOCS_DIR) / filename

    if not file_path.exists():
        raise ValueError("Document not found. Please upload the document first.")

    logger.info(f"Generating summary for: {filename}")

    # 1️ Load document text
    text = load_document(file_path)

    # 2️ Generate summary using LLM
    summary = generate_summary(text)

    logger.info("Summary generated successfully")

    return {
        "summary": summary
    }
