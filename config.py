from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    database_url: str = "sqlite:///./weather.db"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()