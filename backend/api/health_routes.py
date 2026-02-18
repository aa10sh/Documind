from fastapi import APIRouter
from datetime import datetime

from backend.config.settings import APP_NAME, APP_VERSION

router = APIRouter(tags=["Health"])

# ---------------------------------------------------
# Health Check Endpoint
# ---------------------------------------------------
@router.get("/health")
def health_check():
    """
    Health check endpoint used by:
    - Docker
    - AWS Load Balancer
    - CI/CD pipelines
    """
    return {
        "status": "healthy",
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "timestamp": datetime.utcnow()
    }
