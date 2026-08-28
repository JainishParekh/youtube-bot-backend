from langchain_community.document_loaders import YoutubeLoader
from src.api.exceptions import VideoNotFoundError, RAGPipelineException
import logging

logger = logging.getLogger(__name__)

async def get_youtube_transcript(video_id: str):
    try:
        logger.info(f"Fetching transcript for video: {video_id}")
        # Use from_video_id and set add_video_info=False to bypass pytube 400 errors
        url = f"https://www.youtube.com/watch?v={video_id}"
        loader = YoutubeLoader.from_youtube_url(
            url, 
            add_video_info=False, # <--- THIS FIXES THE 400 ERROR
            language=["en", "hi"]
        )
        
        # Use asynchronous load
        documents = await loader.aload()
        
        if not documents:
            raise VideoNotFoundError(video_id)
            
        return documents
        
    except Exception as e:
        # If it's already our custom exception, just raise it
        if isinstance(e, RAGPipelineException):
            raise
        logger.error(f"Failed to load YouTube transcript: {str(e)}")
        raise RAGPipelineException(f"Failed to fetch transcript for {video_id}: {str(e)}")