from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_hunter_io: str = "api_secret"

    class Config:
        env_file = ".env"
        enf_file_encoding = "utf-8"


settings = Settings()
