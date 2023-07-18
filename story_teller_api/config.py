import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import AnyUrl
from pydantic_settings import BaseSettings


load_dotenv()

def get_db_connection_url():
    DB_USER = os.getenv("DB_USERNAME")
    DB_PASS = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")

    if None in [DB_USER, DB_PASS, DB_NAME, DB_HOST, DB_PORT]:
        return None
    return "postgresql://{user}:{password}@{host}:{port}/{database}".format(
        user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT, database=DB_NAME
    )
class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")


settings = Settings()