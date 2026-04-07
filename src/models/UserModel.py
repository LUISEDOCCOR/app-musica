from src.database import BaseModel
from peewee import CharField, DateTimeField
from datetime import datetime


class UserModel(BaseModel):
    name = CharField()
    username = CharField(unique=True)
    password = CharField()
    profile_img = CharField(default="")
    created_at = DateTimeField(default=datetime.now())
