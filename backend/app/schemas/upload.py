from uuid import UUID

from pydantic import BaseModel


class UploadResponse(BaseModel):

    id: UUID

    filename: str

    message: str