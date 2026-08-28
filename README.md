YouTube RAG Bot (Retrieval-Augmented Generation)
================================================

An asynchronous FastAPI application that extracts transcripts from YouTube videos, chunks them, creates vector embeddings using HuggingFace, stores them in ChromaDB, and uses an LLM (Groq/Open AI) to answer user queries based _only_ on the video's content.

🛠 Tech Stack
-------------

*   **Framework:** FastAPI (Async)
    
*   **LLM Orchestration:** LangChain
    
*   **Vector Database:** ChromaDB
    
*   **Embeddings:** HuggingFace (all-MiniLM-L6-v2)
    
*   **LLM:** Groq (Open AI/ GPT-OSS-20b)
    
*   **Containerization:** Docker
    

🏗 Architecture & RAG Pipeline
------------------------------

1.  **Ingestion:** Client provides a YouTube video ID. The server asynchronously fetches the transcript.
    
2.  **Indexing:** The transcript is split into chunks and embedded into ChromaDB, tagged with the video\_id metadata.
    
3.  **Retrieval:** When a user asks a question, the system performs a similarity search in the vector space.
    
4.  **Generation:** The retrieved context and user query are passed to the LLM to generate an accurate, context-aware response.
    

🚀 API Endpoints
----------------

*   POST /api/process-video: Fetches transcript and indexes it into the vector database.
    
*   POST /api/ask: Retrieves relevant context and generates an answer.
    

💻 Local Setup
--------------

1.  Clone the repository.
    
2.  Create a virtual environment: python -m venv venv
    
3.  Activate it: source venv/bin/activate (or venv\\Scripts\\activate on Windows)
    
4.  Install dependencies: pip install -r requirements.txt
    
5.  Create a .env file and add your GROQ\_API\_KEY.
    
6.  Run the server: \`uvicorn main:app --reload