from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.api.routes import router
from src.api.exceptions import AppException
from src.api.business_dto import ErrorResponse
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO)

app = FastAPI(title="YouTube RAG Bot")

# Register Custom Exception Handler
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    # Whenever an AppException is raised, FastAPI will format it using our ErrorResponse schema
    error_response = ErrorResponse(
        error_code=exc.error_code,
        message=exc.message,
        details=str(request.url.path) # Optional: adds the endpoint path where error occurred
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.dict()
    )

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)