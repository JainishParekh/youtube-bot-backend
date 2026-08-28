from fastapi import APIRouter
import logging
from src.api.business_dto import ProcessRequest, ProcessResponse, QueryRequest, QueryResponse
from src.loader import get_youtube_transcript
from src.indexing import index_documents
from src.retrieval import retrieve_context
from src.generation import generate_answer
from src.api.exceptions import BadRequestError, VideoNotFoundError, RAGPipelineException, LLMGenerationException

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/process-video", response_model=ProcessResponse)
async def process_video(req: ProcessRequest):
    """Fetch transcript and index it into Chroma DB"""
    if not req.video_id:
        raise BadRequestError("video_id is required.")

    try:
        logger.info(f"Fetching transcript for video: {req.video_id}")
        docs = await get_youtube_transcript(req.video_id)
        
        if not docs:
            raise VideoNotFoundError(req.video_id)
            
        logger.info("Indexing documents to Chroma DB...")
        index_documents(req.video_id, docs)
        
        return ProcessResponse(message="Video indexed successfully", video_id=req.video_id)
    
    except VideoNotFoundError:
        raise # Re-raise to be caught by FastAPI exception handler
    except Exception as e:
        logger.error(f"RAG Pipeline failed during indexing: {str(e)}")
        raise RAGPipelineException(f"Failed to process and index video: {str(e)}")

@router.post("/ask", response_model=QueryResponse)
def ask_question(req: QueryRequest):
    """Retrieve context and generate answer"""
    if not req.query or not req.video_id:
        raise BadRequestError("Both video_id and query are required.")

    try:
        logger.info(f"Retrieving context for query: {req.query}")
        context = retrieve_context(req.video_id, req.query)
        
        logger.info("Generating answer via LLM...")
        answer = generate_answer(context, req.query)
        
        return QueryResponse(answer=answer, video_id=req.video_id)
    
    except Exception as e:
        logger.error(f"LLM Generation failed: {str(e)}")
        raise LLMGenerationException(f"Failed to generate answer: {str(e)}")