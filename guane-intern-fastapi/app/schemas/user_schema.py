from pydantic import BaseModel
from datetime import datetime


class InUser(BaseModel):  # Clase pydantic = convertida a python
    name: str
    last_name: str
    email: str
    password: str
    create_date: datetime

    class Config:
        orm_mode = True


class OutUser(BaseModel):
    name: str
    last_name: str
    email: str
