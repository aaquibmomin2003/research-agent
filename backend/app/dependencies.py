from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.services.chat_service import ChatService
from app.services.document_service import DocumentService


def get_db():

    db: Session = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def get_chat_service():

    return ChatService()


def get_document_service(
    db: Session,
):

    return DocumentService(db)