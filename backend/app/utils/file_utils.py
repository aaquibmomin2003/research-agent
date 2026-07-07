from pathlib import Path

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".txt",
    ".docx",
}


def validate_extension(filename: str):
    suffix = Path(filename).suffix.lower()

    if suffix not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f"{suffix} is not supported."
        )