from fastapi import FastAPI
from tortoise import models
from tortoise.contrib.fastapi import register_tortoise
from app.models import *
from app.api.endpoints.dog_routes import dog_router
from app.api.endpoints.user_routes import user_router
from .debugger import initialize_fastapi_server_debugger_if_needed
from app.api.api import api_router
from app.config import Settings

application = FastAPI() 
##app.include_router(dog_router)
##app.include_router(user_router)

def create_application() -> FastAPI:
    initialize_fastapi_server_debugger_if_needed()
    application = FastAPI()
    application.include_router(api_router, prefix="/api")
    return application

setting = Settings()

register_tortoise(application, db_url=setting.DB_URL, modules={"models": ["app.models"]}, generate_schemas=True, add_exception_handlers=True)
