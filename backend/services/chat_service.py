from backend.rag.retriever import retrieve_relevant_chunks
from backend.rag.generator import generate_answer
from backend.config.logging import logger


# Chat with Document (RAG)
def chat_with_document(question: str):
    """
    Handles user question and returns answer using RAG.
    """

    logger.info(f"Received question: {question}")

    # 1️ Retrieve relevant chunks from vector DB
    chunks = retrieve_relevant_chunks(question)

    # 2️ Generate answer using LLM
    answer = generate_answer(question, chunks)

    logger.info("Answer generated successfully")

    return {
        "answer": answer,
        "source_chunks": chunks
    }
