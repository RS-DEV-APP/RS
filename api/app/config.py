from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    POSTGRES_USER: str = "app"
    POSTGRES_PASSWORD: str = "app"
    POSTGRES_DB: str = "bms"
    POSTGRES_PORT: int = 5432
    API_PORT: int = 8000
    JWT_SECRET: str = "change-me"
    TZ: str = "Europe/Berlin"
    REDIS_PORT: int = 6379

    @property
    def database_url(self) -> str:
        return f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@db:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore
