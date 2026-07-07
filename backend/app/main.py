from fastapi import FastAPI

from app.core.config import settings
from app.core.logger import logger


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/")
async def root():

    logger.info("Root endpoint called.")

    return {
        "message": "Research Agent API Running"
    }


@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }