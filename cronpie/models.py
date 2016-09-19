from peewee import Model, CharField, IntegerField, DateTimeField

database = SqliteDatabase('measures.db')

class BaseModel(Model):
    class Meta:
        database = database


class Command(BaseModel):
    command = CharField()


class Run(BaseModel)
    command = ForeignKeyField(Command, related_name='runs')
    run_time = IntegerField()


class Measure(BaseModel):
    run = ForeignKeyField(Run, related_name='measures')
    cpu = IntegerField()
    memory = IntegerField()

