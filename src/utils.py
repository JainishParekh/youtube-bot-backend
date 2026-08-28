def concat_context_docs(context_docs):
    return "\n\n".join([doc.page_content for doc in context_docs])