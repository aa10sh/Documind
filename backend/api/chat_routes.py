from fastapi import APIRouter, HTTPException
from backend.models.schemas import ChatRequest, ChatResponse
from backend.services.chat_service import chat_with_document
from backend.config.logging import logger

router = APIRouter(tags=["Chat"])


# Ask Question Endpoint (RAG)
@router.post("/ask", response_model=ChatResponse)
def ask_question(request: ChatRequest):
    """
    Ask questions about uploaded documents.
    """

    try:
        logger.info(f"Question received: {request.question}")

        result = chat_with_document(request.question)

        return ChatResponse(
            answer=result["answer"],
            source_chunks=result["source_chunks"]
        )

    except Exception as e:
        logger.error(f"Chat failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
