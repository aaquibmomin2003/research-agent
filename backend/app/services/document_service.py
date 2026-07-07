import shutil
import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.document import Document
from app.repositories.document_repository import DocumentRepository
from app.services.rag_service import RAGService
from app.utils.file_utils import validate_extension
from app.utils.hash_utils import sha256_file


class DocumentService:

    def __init__(self, db: Session):
        self.db = db
        self.repository = DocumentRepository(db)
        self.rag = RAGService()

    async def upload_document(self, file: UploadFile):

        validate_extension(file.filename)

        storage_path = Path(settings.DOCUMENT_STORAGE)
        storage_path.mkdir(parents=True, exist_ok=True)

        extension = Path(file.filename).suffix

        generated_name = f"{uuid.uuid4()}{extension}"

        destination = storage_path / generated_name

        try:

            with destination.open("wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            file_hash = sha256_file(destination)

            existing = self.repository.get_by_hash(file_hash)

            if existing:

                destination.unlink(missing_ok=True)

                raise HTTPException(
                    status_code=409,
                    detail="Document already exists.",
                )

            document = Document(
                filename=file.filename,
                file_hash=file_hash,
                file_path=str(destination),
                file_size=destination.stat().st_size,
                chunk_count=0,
            )

            saved = self.repository.create(document)

            chunk_count = await self.rag.ingest(saved.file_path)

            saved.chunk_count = chunk_count

            self.db.commit()

            self.db.refresh(saved)

            return saved

        except Exception:

            if destination.exists():
                destination.unlink(missing_ok=True)

            raise