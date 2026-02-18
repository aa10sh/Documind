from pydantic import BaseModel, Field
from typing import Optional, List

# Upload Response Schema
class UploadResponse(BaseModel):
    filename: str
    message: str

# Ask Question Request
class ChatRequest(BaseModel):
    question: str = Field(..., example="Explain neural networks in simple terms")

# Chat Response Schema
class ChatResponse(BaseModel):
    answer: str
    source_chunks: Optional[List[str]] = None
    
# Summary Response Schema
class SummaryResponse(BaseModel):
    summary: str