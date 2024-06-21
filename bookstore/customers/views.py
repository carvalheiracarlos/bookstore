from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from drf_yasg.utils import swagger_auto_schema

from customers.models import Customer
from customers.serializers import CustomerSerializer
from core.mixins import PermissionsByActionMixin, SerializerClassByActionMixin


User = get_user_model()

class CustomerViewSet(CreateModelMixin,
                      ListModelMixin,
                      RetrieveModelMixin,
                      PermissionsByActionMixin, 
                      SerializerClassByActionMixin, 
                      GenericViewSet):

    queryset = Customer.objects.all()
    filter_backends = [DjangoFilterBackend]
    pagination_class = None
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