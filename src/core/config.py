from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "urlshortner"
    app_env: str = "development"
    database_url: str = "postgresql+psycopg://postgres:postgres@db:5432/urlshortner"
    redis_url: str = "redis://redis:6379/0"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
