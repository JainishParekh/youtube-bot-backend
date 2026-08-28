class AppException(Exception):
    """Base exception for the application"""
    def __init__(self, status_code: int, error_code: str, message: str):
        self.status_code = status_code
        self.error_code = error_code
        self.message = message
        super().__init__(message)

# --- API / Client Errors (4xx) ---
class BadRequestError(AppException):
    def __init__(self, message: str = "Incorrect request payload."):
        super().__init__(status_code=400, error_code="API_400_001", message=message)

class VideoNotFoundError(AppException):
    def __init__(self, video_id: str):
        super().__init__(status_code=404, error_code="API_404_001", message=f"Transcript not found or video does not exist: {video_id}")

# --- RAG Pipeline Errors (5xx) ---
class RAGPipelineException(AppException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, error_code="RAG_500_001", message=f"RAG Pipeline Error: {detail}")

class LLMGenerationException(AppException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, error_code="RAG_500_002", message=f"LLM Generation Error: {detail}")