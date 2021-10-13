from app.models.user import User
from app.config import settings
from app.infra.httpx.client import HTTPClient
from app.infra.services.responses import Responses
from app.schemas.user_schema import In_User_Schema, Out_User_Schema



class UserService:

    # crear un servicio que se pegue al ms database utilizando httpxclient
    def __init__(
        self, *, client: HTTPClient = HTTPClient(), check_codes: Responses = Responses()
    ):
        self.__client = client
        self.__check_codes = check_codes

    async def get_by_id(self, *, id: int) -> User:
        url = f"{settings.GUANE_INTERN_DATABASE_SERVICE}/api/users/{id}"
        header = {"Content-Type": "application/json"}
        response = await self.__client.get(url_service=url, headers=header, timeout=40)
        await self.__check_codes.check_codes(response=response)
        response = response.json()
        return User(**response)
    """
 async def get_all_users():  # Obtener todos los usuarios
    users = await User.all()
    return users


# Obtener los users mediante el id
async def find_user_by_id(id: int):
    user = await User.filter(id=id).first().values()
    return user


async def create_user(users: In_User_Schema):  # Ingresar un nuevo user
    user_data = User(name=users.name, last_name=users.last_name, email=users.email,
                     password=users.password, create_date=users.create_date)
    await user_data.save()
    return user_data

# Actualizar un user existente por el id


async def update_user(id: int, user_schema: Out_User_Schema):
    user_data = await User.get(id=id)
    user_data.name = user_schema.name
    user_data.last_name = user_schema.last_name
    user_data.email = user_schema.email
    await user_data.save()
    return True


# Borrar los users mediante el id
async def delete_users_by_id(id: int):
    user = await User.filter(id=id).first().delete()
    if not user:
        raise "El User con este Id no se encuentra."
    return f"El User con el Id {id} se borro exitosamente."
"""

user_service = UserService()
