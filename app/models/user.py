from tortoise import Model, fields
from pydantic import BaseModel
from datetime import datetime


class User(Model):
    _id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=12, null=False, unique=True)
    last_name = fields.CharField(max_length=12, null=False, unique=False)
    email = fields.CharField(max_length=200, null=False, unique=True)
    password = fields.TextField(null=True)
    join_data = fields.DatetimeField(default=datetime.utcnow)
    
