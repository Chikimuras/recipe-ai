import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings using Pydantic for configuration management.
    """
    # Database configuration
    DATABASE_URL: str = "sqlite:///./dev.db"
    # ChromaDB settings
    CHROMADB_HOST: str = "localhost"
    CHROMADB_PORT: int = 8000