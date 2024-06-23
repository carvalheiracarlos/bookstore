



class OrderManager(models.Manager):
    def my_orders(self, request_user):
        from checkout.models import Order 
        if request_user.is_superuser:
            return Order.objects.all()

        return Order.objects.filter(budget__cart__user_id=request_user.id)