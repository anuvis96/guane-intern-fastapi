from fastapi import FastAPI
from tortoise import models
from tortoise.contrib.fastapi import register_tortoise
from app.models import *
from app.routes.dog_routes import dog_router

app = FastAPI() 
app.include_router(dog_router)

register_tortoise(app, db_url="sqlite://database.sqlite3", modules={"models": [
                  "main"]}, generate_schemas=True, add_exception_handlers=True)
