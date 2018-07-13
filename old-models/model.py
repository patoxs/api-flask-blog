from peewee import *

# importar bd desde base de datos existente con peewee
# python -m pwiz -e postgresql -u pato -P postgres -H 144.217.240.227 -p 5432 -s araucaria > model.py
#

database = PostgresqlDatabase('postgres', **{'host': '144.217.240.227', 'password': 'inxs0175', 'user': 'pato', 'port': 5432})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Config(BaseModel):
    id = BigIntegerField(primary_key=True)
    param = CharField()
    status = IntegerField()
    type_config = CharField(null=True)
    value = TextField()

    class Meta:
        db_table = 'config'
        schema = 'araucaria'

class Media(BaseModel):
    description = TextField()
    id = BigIntegerField(primary_key=True)
    media = CharField()
    owner = BigIntegerField(null=True)
    ping = IntegerField(null=True)
    url = TextField()

    class Meta:
        db_table = 'media'
        schema = 'araucaria'

class PersonType(BaseModel):
    id = BigIntegerField(primary_key=True)
    description = TextField()
    person_type = CharField()

    class Meta:
        db_table = 'person_type'
        schema = 'araucaria'

class Person(BaseModel):
    email = CharField()
    id = BigIntegerField(primary_key=True)
    id_person_type = ForeignKeyField(db_column='id_person_type', null=True, rel_model=PersonType, to_field='id')
    image = CharField(null=True)
    key_activate = CharField(null=True)
    login = CharField()
    nicename = TextField(null=True)
    password = TextField()
    status = IntegerField()

    class Meta:
        db_table = 'person'
        schema = 'araucaria'

class Post(BaseModel):
    content = TextField(null=True)
    datetime = DateTimeField()
    excerpt = TextField()
    id = BigIntegerField(primary_key=True)
    id_person = ForeignKeyField(db_column='id_person', rel_model=Person, to_field='id')
    modified = DateTimeField()
    parent = BigIntegerField(null=True)
    password = CharField(null=True)
    ping = IntegerField(null=True)
    post_order = IntegerField(null=True)
    status = IntegerField()
    title = TextField()
    url = TextField()

    class Meta:
        db_table = 'post'
        schema = 'araucaria'

class Taxonomy(BaseModel):
    id = BigIntegerField(primary_key=True)
    description = TextField()
    parent = IntegerField(null=True)
    status = IntegerField()
    taxonomy = CharField()

    class Meta:
        db_table = 'taxonomy'
        schema = 'araucaria'

class PostTaxonomy(BaseModel):
    id_post = ForeignKeyField(db_column='id_post', rel_model=Post, to_field='id')
    id_taxonomy = ForeignKeyField(db_column='id_taxonomy', rel_model=Taxonomy, to_field='id')

    class Meta:
        db_table = 'post_taxonomy'
        schema = 'araucaria'
        primary_key = False

