from sqlalchemy.orm import Session

from app.repositories.document_repository import (
    DocumentRepository,
)


class DocumentService:

    def __init__(self, db: Session):

        self.repository = DocumentRepository(db)