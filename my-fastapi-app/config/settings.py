from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    frontend_url: str = "http://frontend:3000"
    cors_origins: list[str] = ["http://frontend:3000"]
    cors_methods: list[str] = ["*"]
    cors_headers: list[str] = ["*"]

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()