from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title="YouTube RAG Bot")

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)