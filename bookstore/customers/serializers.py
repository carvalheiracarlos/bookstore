from rest_framework import serializers
from django.contrib.auth import get_user_model 


from authentication.serializers import UserSerializer
from customers.models import Customer


User = get_user_model()

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = [
            'id',
            'user',
            'name',
            'cpf',
            'phone'
        ]
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data.pop('user'))
        return Customer.objects.create(user=user, **validated_data)