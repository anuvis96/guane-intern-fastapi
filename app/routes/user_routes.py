from fastapi import APIRouter, Response, status
from starlette import status
from app.schemas.user_schema import In_User_Schema, Out_User_Schema
from app.models.user import User
from typing import List
from starlette.status import HTTP_204_NO_CONTENT

user_router = APIRouter()

@user_router.get('/users', response_model=List[Out_User_Schema], tags=["users"])
async def get_all_users():
    users = await User.all()
    return users


@user_router.post("/users/", response_model=In_User_Schema)
async def create_user(users: In_User_Schema):
    user_entity = users.dict()
    user_data = User(**user_entity)
    await user_data.save()
    return user_data


@user_router.get('/users/{id}', response_model=List[Out_User_Schema], tags=["users"])
async def find_user(id: int):
    user = await User.filter(id=id).first().values()
    return user

# comentar control k + control c

# @user_router.put("/users/{id}", response_model=OutUserSchema)
# async def update_user(id: str, user: OutUserSchema):
#     await 
#     return 


@user_router.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_user(id: int):
    user = await User.filter(id=id).first().delete()
    if not user:
        raise "El Usuario con este Id no se encuentra."
    return f"El Usuario con el Id {id} se borro exitosamente."
