from peewee import Model
from .config import db

class BaseModel(Model):

    #@classmethod    
    #def create_item(cls, data:dict):
    #    return cls.create(**data)
    
    @classmethod    
    def delete_item(cls, id:int):
        return cls.delete().where(cls.id == id).execute()
    
    @classmethod    
    def get_by_id(cls, id:int):
        return cls.get_or_none(cls.id == id)
    
    @classmethod    
    def get_all(cls):
        return list(cls.select().dicts())
    
    @classmethod    
    def update_item(cls, id:int, data:dict):
        return cls.update(**data).where(cls.id == id).execute()
    
    @classmethod    
    def get_by_prop(cls, prop: dict):
        pass


    class Meta:
        database = db