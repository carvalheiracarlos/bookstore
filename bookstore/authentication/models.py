import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class AuthUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('Endereço de Email', blank=False, null=False, unique=True)

    class Meta:
        db_table = 'auth_user'