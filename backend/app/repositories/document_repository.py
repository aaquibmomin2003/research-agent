from uuid import UUID

from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, document):
    
        self.db.add(document)

        self.db.commit()

        self.db.refresh(document)

        return document

    def get_by_id(self, document_id: UUID):

        return (
            self.db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    def get_by_hash(self, file_hash: str):

        return (
            self.db.query(Document)
            .filter(Document.file_hash == file_hash)
            .first()
        )

    def list_documents(self):

        return (
            self.db.query(Document)
            .order_by(Document.uploaded_at.desc())
            .all()
        )

    def delete(self, document: Document):

        self.db.delete(document)

        self.db.commit()
    