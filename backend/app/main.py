from fastapi import FastAPI

from app.core.config import settings

from app.db.base import Base
from app.db.database import engine

# Import models so SQLAlchemy registers them
from app.models import Document


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/")
async def root():
    return {
        "message": "Research Agent API Running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }