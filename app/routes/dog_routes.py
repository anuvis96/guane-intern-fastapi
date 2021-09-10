from fastapi import APIRouter, Response, status
from starlette import status
from app.models.dog import Dog
from starlette.status import HTTP_204_NO_CONTENT
from app.schemas.dog_schema import Dog_Schema
from app.models.dog import Dog
from typing import List


dog_router = APIRouter()

@dog_router.get('/dogs', response_model=List[Dog_Schema], tags=["dogs"])
async def get_all_dogs():
    dogs = await Dog.all() 
    return dogs