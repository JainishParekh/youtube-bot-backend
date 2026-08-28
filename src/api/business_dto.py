from pydantic import BaseModel
from typing import Optional

# --- Request Models ---
class ProcessRequest(BaseModel):
    video_id: str

class QueryRequest(BaseModel):
    video_id: str
    query: str

# --- Response Models ---
class ProcessResponse(BaseModel):
    message: str
    video_id: str

class QueryResponse(BaseModel):
    answer: str
    video_id: str

class ErrorResponse(BaseModel):
    error_code: str
    message: str
    details: Optional[str] = None