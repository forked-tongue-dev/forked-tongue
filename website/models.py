from django.db.models import Model, TextField, BooleanField, CharField


class Mirrors(Model):
    host_name = CharField(max_length=40)
    url = TextField()
    host_description = TextField()
    active = BooleanField()