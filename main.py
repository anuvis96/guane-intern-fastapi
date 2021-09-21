from fastapi import FastAPI
from tortoise import models
from tortoise.contrib.fastapi import register_tortoise
from app.models import *
from app.routes.dog_routes import dog_router
from app.routes.user_routes import user_router

app = FastAPI() 
app.include_router(dog_router)
app.include_router(user_router)

register_tortoise(app, db_url="postgres://postgres:5432/guane_intern_db", modules={"models": [
                  "main"]}, generate_schemas=True, add_exception_handlers=True)
