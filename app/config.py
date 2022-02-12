from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DEBUG: bool


@lru_cache
def get_settings():
    return Settings()
