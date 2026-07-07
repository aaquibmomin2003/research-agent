from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.services.document_service import (
    DocumentService,
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    service = DocumentService(db)

    return await service.upload_document(file)


@router.get("/")
def health():

    return {

        "message": "Documents API Running"

    }