from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict


class DocumentResponse(BaseModel):
    id: UUID

    filename: str

    file_size: int

    chunk_count: int

    uploaded_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )