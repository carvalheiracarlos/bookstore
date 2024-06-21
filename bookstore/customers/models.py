from django.db import models
from django.contrib.auth import get_user_model 


from core.models import BaseModel
from core.validators import validate_phone, validate_cpf


User = get_user_model()

class Customer(BaseModel):
    user = models.OneToOneField(User, verbose_name='usuário', on_delete=models.CASCADE)
    name = models.CharField('nome', max_length=255)
    phone = models.CharField('contato', max_length=20, blank=False, null=False, validators=[validate_phone])
    cpf = models.CharField('CPF', max_length=14, validators=[validate_cpf], unique=True)


    class Meta:
        verbose_name_plural = 'Customer'
        verbose_name = 'Customers'
        ordering = ('-created',)

    def __str__(self):
        return self.name

    @property
    def _name(self):
        return self.user.first_name

    @property
    def _last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email