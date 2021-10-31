from django.contrib.postgres.fields import JSONField
from django.contrib.sessions.models import Session
from django.db.models import CharField
from django.db.models import Model
from django.db.models import SET_NULL
from django.db.models import UniqueConstraint
from django.db.models.fields.related import ForeignKey


class Event(Model):
    name = CharField(max_length=100)
    category = CharField(max_length=100)
    payload = JSONField()
    session = ForeignKey(Session, on_delete=SET_NULL)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['name', 'category'], name='unique_event_type')
        ]
