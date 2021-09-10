from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Dog_Schema(BaseModel):      ## Clase pydantic = convertida a python
    name: str
    picture: str
    is_adopted: bool
    create_date: datetime 
    
    class Config:
        orm_mode = True

