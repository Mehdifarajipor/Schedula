from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):

    # postgres database
    DB_NAME: str
    DB_USER: str
    DB_USER_PASS: str
    DB_PORT: int
    DB_HOST: str

    # smtp gmail app

    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str


    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")

config_settings = Settings()
