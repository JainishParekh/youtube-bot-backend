from langchain_chroma import Chroma
from src.indexing import embeddings
from src.constants import Constants

def retrieve_context(video_id: str, query: str, k: int = 4):
    
    vector_store = Chroma(
        persist_directory=Constants.PERSIST_DIR, 
        embedding_function=embeddings,
        collection_name=Constants.YOUTUBE_COLLECTION
    )
    
    # This ensures the bot only answers based on THIS video's transcript
    results = vector_store.similarity_search(
        query=query, 
        k=k, 
        filter={"video_id": video_id}
    )
    return results