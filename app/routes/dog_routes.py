from datetime import date
from fastapi import APIRouter, Response, status
from starlette import status
from app.models.dog import Dog
from starlette.status import HTTP_204_NO_CONTENT
from app.schemas.dog_schema import Dog_Schema
from app.models.dog import Dog
from typing import List
from starlette.status import HTTP_204_NO_CONTENT



dog_router = APIRouter()

@dog_router.get('/dogs', response_model=List[Dog_Schema], tags=["dogs"])
async def get_all_dogs():
    dogs = await Dog.all() 
    return dogs

@dog_router.post("/dogs/", response_model=List[Dog_Schema])
async def create_dog(dogs: Dog):
   dog_entity =  dogs.dict()
   dog_data = Dog(**dog_entity)
   await dog_data.save()
   return dog_data


@dog_router.get('/dogs/{id}', response_model=List[Dog_Schema], tags=["dogs"])
async def find_dog(id: str):
    dog = await Dog.filter(id = id).first().values()
    return dog

##comentar control k + control c

# @dog_router.put("/dogs/{id}", response_model=Dog)
# async def update_dog(id: str, dog: Dog):
#     update_dog_encoded = jsonable_encoder(dog)
#     dog[id] = await update_dog_encoded
#     return update_dog_encoded  


@dog_router.delete('/dogs/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["dogs"])
async def delete_user(id: str):
     dog = await Dog.filter(id = id).first().delete()
     if not dog: 
         raise "El Dog con este Id no se encuentra."
     return f"El Dog con el Id {id} se borro exitosamente." 