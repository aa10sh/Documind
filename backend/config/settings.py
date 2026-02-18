import os
from pathlib import Path
from dotenv import load_dotenv

# Explicitly load .env from project root
ENV_PATH = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=ENV_PATH)

print("ENV PATH:", ENV_PATH)


# PROJECT ROOT PATH
BASE_DIR= Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DOCS_DIR = DATA_DIR / "raw_docs"
PROCESSED_DOCS_DIR = DATA_DIR / "processed_docs"
VECTOR_STORE_DIR = DATA_DIR / "vector_store"

# Create directories if not exist
RAW_DOCS_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DOCS_DIR.mkdir(parents=True, exist_ok=True)
VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)


LLM_PROVIDER =os.getenv("LLM_PROVIDER","openai")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")

# MODEL CONFIGURATION

# OpenAI Models
OPENAI_CHAT_MODEL = "gpt-4o-mini"
OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"

# HuggingFace Models
HF_CHAT_MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"
HF_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# RAG CONFIGURATION
CHUNK_SIZE = 800
CHUNK_OVERLAP = 200
TOP_K_RESULTS = 4

# VECTOR DATABASE
VECTOR_DB_TYPE = "faiss"   # faiss / chroma

# APP CONFIG
APP_NAME = "DocuMind AI"
APP_VERSION = "1.0.0"
DEBUG = True

print("LLM_PROVIDER =", LLM_PROVIDER)
