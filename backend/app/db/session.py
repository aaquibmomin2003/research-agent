"""
Database dependency for FastAPI.
"""

from app.db.database import SessionLocal


def get_db():
    """
    Creates a new database session
    for every request.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()