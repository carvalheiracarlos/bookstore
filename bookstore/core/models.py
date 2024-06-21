from uuid import uuid4
from django.db import models
from behaviors.behaviors import Timestamped
from django_lifecycle import LifecycleModelMixin


class UUIDidentifier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


class BaseModel(LifecycleModelMixin, UUIDidentifier, Timestamped):
    objects = models.Manager()

    class Meta:
        abstract = True