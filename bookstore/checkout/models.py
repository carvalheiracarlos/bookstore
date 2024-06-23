from django.db import models
from django.core.validators import MinValueValidator

from customers.models import Customer
from books.models import Book
from core.models import BaseModel

class Order(BaseModel):
    class Status(models.IntegerChoices):
        CONFIRMED = 0, 'CONFIRMADO',
        REJECTED = 1, 'REJEITADO'
    
    customer = models.ForeignKey(Customer, verbose_name='Consumidor do Pedido', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name='Livro do Pedido', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField('Quantidade de Livros', validators=[MinValueValidator(0)])
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.REJECTED.value)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f'{self.customer.name} | {self.book.name}' 