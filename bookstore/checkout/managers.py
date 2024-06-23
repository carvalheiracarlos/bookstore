from django.db import models
from django.shortcuts import get_object_or_404


from core.validators import validate_book_quantity

class OrderManager(models.Manager):
    def create(self, **obj_data):
        from books.models import Book
        from checkout.models import Order

        Status = Order.Status
        book = get_object_or_404(Book, pk=obj_data['book'].id)
        validate_book_quantity(obj_data['quantity'])
        quantity_ballance = book.quantity - obj_data['quantity']

        if quantity_ballance >= 0:
            book.quantity = quantity_ballance
            book.save()
            obj_data['status'] = Status.CONFIRMED

        return super().create(**obj_data)

    def my_orders(self, request_user):
        from checkout.models import Order 
        if request_user.is_superuser:
            return Order.objects.all()

        return Order.objects.filter(customer__user_id=request_user.id)