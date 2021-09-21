from fastapi import FastAPI
from tortoise import models
from tortoise.contrib.fastapi import register_tortoise
from app.models import *
from app.routes.dog_routes import dog_router
from app.routes.user_routes import user_router
from app.config import Settings

app = FastAPI() 
app.include_router(dog_router)
app.include_router(user_router)

setting = Settings()

register_tortoise(app, db_url=setting.DB_URL, modules={"models": ["app.models"]}, generate_schemas=True, add_exception_handlers=True)
