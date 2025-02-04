from peewee import *

database = SqliteDatabase('personas.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Persona(BaseModel):
    fecha_nacimiento = DateField()
    nombre = CharField()

    class Meta:
        table_name = 'persona'

class Mascota(BaseModel):
    nombre = CharField()
    propietario = ForeignKeyField(column_name='propietario_id', field='id', model=Persona)
    tipo_animal = CharField()

    class Meta:
        table_name = 'mascota'

