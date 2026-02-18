import os
from pathlib import Path

project_name = "backend"

list_of_files = [

    # -----------------------------
    # FRONTEND
    # -----------------------------
    "frontend/index.html",
    "frontend/upload.html",
    "frontend/chat.html",
    "frontend/css/style.css",
    "frontend/js/app.js",

    # -----------------------------
    # BACKEND CORE
    # -----------------------------
    "backend/__init__.py",
    "backend/app.py",

    # -----------------------------
    # CONFIG
    # -----------------------------
    "backend/config/__init__.py",
    "backend/config/settings.py",
    "backend/config/logging.py",

    # -----------------------------
    # API ROUTES
    # -----------------------------
    "backend/api/__init__.py",
    "backend/api/upload_routes.py",
    "backend/api/chat_routes.py",
    "backend/api/health_routes.py",

    # -----------------------------
    # SERVICES (Business Logic)
    # -----------------------------
    "backend/services/__init__.py",
    "backend/services/document_service.py",
    "backend/services/chat_service.py",
    "backend/services/summarizer_service.py",

    # -----------------------------
    # RAG PIPELINE ⭐
    # -----------------------------
    "backend/rag/__init__.py",
    "backend/rag/ingest.py",
    "backend/rag/retriever.py",
    "backend/rag/generator.py",
    "backend/rag/embeddings.py",
    "backend/rag/prompt_templates.py",

    # -----------------------------
    # DATA MODELS (Pydantic)
    # -----------------------------
    "backend/models/__init__.py",
    "backend/models/schemas.py",

    # -----------------------------
    # UTILS
    # -----------------------------
    "backend/utils/__init__.py",
    "backend/utils/file_loader.py",
    "backend/utils/chunking.py",
    "backend/utils/helpers.py",

    # -----------------------------
    # DATA STORAGE (Local Dev)
    # -----------------------------
    "data/raw_docs/.gitkeep",
    "data/processed_docs/.gitkeep",
    "data/vector_store/.gitkeep",

    # -----------------------------
    # TESTING
    # -----------------------------
    "tests/__init__.py",
    "tests/test_api.py",

    # -----------------------------
    # DOCKER & DEPLOYMENT
    # -----------------------------
    "docker/.gitkeep",
    ".github/workflows/ci_cd.yml",

    # -----------------------------
    # ROOT FILES
    # -----------------------------
    ".env",
    ".env.example",
    ".gitignore",
    "requirements.txt",
    "Dockerfile",
    "docker-compose.yml",
    "README.md",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # create file if not exists or empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"File already exists at: {filepath}")

print("✅ RAG Project structure created successfully!")
