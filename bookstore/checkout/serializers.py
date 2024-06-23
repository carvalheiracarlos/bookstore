from rest_framework import serializers

from checkout.models import Order
from customers.serializers import CustomerSerializer
from books.serializers import BookSerializer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = [
            'id',
            'book',
            'quantity',
            'status',
        ]

    def to_representation(self, instance):
        self.fields['customer'] = CustomerSerializer()
        self.fields['book'] = BookSerializer()
        self.fields['status'] = serializers.CharField(source='get_status_display')
        return super(OrderSerializer, self).to_representation(instance)