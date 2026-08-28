from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_chroma import Chroma
from src.constants import Constants


embeddings = FastEmbedEmbeddings(model_name=Constants.EMBEDDINGS_MODEL)


def index_documents(video_id: str, documents):
    # 1. Chunking
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    
    # Add video_id to metadata so we can filter later
    for chunk in chunks:
        chunk.metadata["video_id"] = video_id

    # 2. Store in Chroma DB
    vector_store = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=Constants.PERSIST_DIR,
        collection_name=Constants.YOUTUBE_COLLECTION
    )
    return vector_store