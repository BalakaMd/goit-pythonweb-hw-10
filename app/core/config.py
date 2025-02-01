from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Need use from .env. Just for teacher purposes only
    PROJECT_NAME: str = "Contact Book API"
    ALLOWED_ORIGINS: str = "http://localhost:8000"
    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"

settings = Settings()