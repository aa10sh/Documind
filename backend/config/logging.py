from loguru import logger
import sys
from pathlib import Path

# Logs directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

# Remove default logger
logger.remove()

# Console Logger (for local development)
logger.add(
    sys.stdout,
    format="<green>{time}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
    level="INFO",
)


# File Logger (for production & AWS)
logger.add(
    LOG_FILE,
    rotation="10 MB",        # create new log file after 10MB
    retention="10 days",     # keep logs for 10 days
    compression="zip",       # compress old logs
    level="INFO"
)

logger.info("Logging system initialized!!")