from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.constants import Constants
from src.utils import concat_context_docs
from dotenv import load_dotenv

load_dotenv()

def generate_answer(context_docs, query):
    
    llm = ChatGroq(model=Constants.GORQ_MODEL, temperature=0.2)
    
    # Combine the retrieved chunks into a single string
    context_text = concat_context_docs(context_docs)

    prompt = ChatPromptTemplate.from_template("""
    You are a helpful assistant. Answer the user's question based ONLY on the following context.
    If the answer is not in the context, say "I couldn't find the answer in the video transcript."
    
    Context:
    {context}
    
    Question: {question}
    """)
    
    chain = prompt | llm
    response = chain.invoke({"context": context_text, "question": query})
    return response.content