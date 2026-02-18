from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.document_service import process_document
from backend.services.summarizer_service import summarize_document
from backend.models.schemas import UploadResponse, SummaryResponse
from backend.config.logging import logger

router = APIRouter(tags=["Document"])


# Upload Document Endpoint
@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    """
    Upload PDF/DOCX/TXT and ingest into vector DB.
    """

    try:
        logger.info(f"Uploading file: {file.filename}")

        filename = process_document(file)

        return UploadResponse(
            filename=filename,
            message="File uploaded and processed successfully"
        )

    except Exception as e:
        logger.error(f"Upload failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))



# Summarize Document Endpoint
@router.post("/summarize/{filename}", response_model=SummaryResponse)
def summarize_uploaded_document(filename: str):
    """
    Generate summary of uploaded document.
    """

    try:
        result = summarize_document(filename)
        return SummaryResponse(summary=result["summary"])

    except Exception as e:
        logger.error(f"Summarization failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
