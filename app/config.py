from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DB_URL: str = Field(...)
    CELERY_BROKER: str = 'localhots:5672//rabbitmq'
    CELERY_BACKEND = 'redis://localhost:6379'