from celery import Celery
from .config import Settings

setting = Settings()
celery_task = Celery('tasks', broker=setting.CELERY_BROKER, backend=setting.CELERY_BACKEND)