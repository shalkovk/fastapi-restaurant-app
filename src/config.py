import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env"))


class Settings:
    MODE: str = os.environ.get("MODE")

    DB_HOST: str = os.environ.get("POSTGRES_HOST")
    DB_PORT: int = os.environ.get("POSTGRES_PORT")
    DB_USER: str = os.environ.get("POSTGRES_USER")
    DB_PASS: str = os.environ.get("POSTGRES_PASSWORD")
    DB_NAME: str = os.environ.get("POSTGRES_DB")

    DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


settings = Settings()
