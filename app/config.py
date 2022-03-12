from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool


def get_settings():
    raise NotImplementedError
