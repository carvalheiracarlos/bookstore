from rest_framework import serializers
from django.shortcuts import get_object_or_404

from checkout.models import Order
from customers.models import Customer
from customers.serializers import CustomerSerializer
from books.serializers import BookSerializer

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order 
        fields = [
            'id',
            'book',
            'quantity',
        ]

    def to_representation(self, instance):
        self.fields['customer'] = CustomerSerializer()
        self.fields['book'] = BookSerializer()
        self.fields['status' ]= serializers.CharField(source='get_status_display')
        return super(OrderSerializer, self).to_representation(instance)

    def create(self, validated_data):
        customer = get_object_or_404(Customer, user=self.context['request'].user)
        validated_data['customer'] = customer
        return Order.objects.create(**validated_data)