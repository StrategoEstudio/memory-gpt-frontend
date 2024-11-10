from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    redis_url: str  # Cambiar a `redis_url` para usar la URL completa de conexión

    class Config:
        env_file = ".env"

settings = Settings()
