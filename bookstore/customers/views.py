from django.contrib.auth import get_user_model
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet

from customers.models import Customer
from customers.serializers import CustomerSerializer
from core.mixins import PermissionsByActionMixin


User = get_user_model()

class CustomerViewSet(CreateModelMixin,
                      ListModelMixin,
                      RetrieveModelMixin,
                      PermissionsByActionMixin, 
                      GenericViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes_by_action = {
        'create': [AllowAny],
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated]
    }

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Customer.objects.all()

        return Customer.objects.filter(user__id=self.request.user.id)