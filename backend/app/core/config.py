from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    DATABASE_URL: str

    DOCUMENT_STORAGE: str
    MAX_FILE_SIZE: int

    CHROMA_PATH: str
    EMBED_MODEL: str
    OLLAMA_MODEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()