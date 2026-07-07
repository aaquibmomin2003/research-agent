from fastapi import FastAPI

from app.core.config import settings

from app.db.base import Base
from app.db.database import engine

# Import models so SQLAlchemy registers them
from app.models import Document
from app.api.document_router import router as document_router
from app.api.chat_router import router as chat_router
from app.core.exceptions import register_exception_handlers
from app.api.system_router import router as system_router

Base.metadata.create_all(bind=engine)



app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)
register_exception_handlers(app)
app.include_router(document_router)
app.include_router(system_router)
app.include_router(chat_router)

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