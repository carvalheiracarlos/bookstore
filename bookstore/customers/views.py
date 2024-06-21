from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from drf_yasg.utils import swagger_auto_schema

from customers.models import Customer
from customers.serializers import CustomerSerializer
from core.mixins import PermissionsByActionMixin, SerializerClassByActionMixin


User = get_user_model()

class CustomerViewSet(CreateModelMixin, 
                      PermissionsByActionMixin, 
                      SerializerClassByActionMixin, 
                      GenericViewSet):

    queryset = Customer.objects.all()
    filter_backends = [DjangoFilterBackend]
    pagination_class = None
    serializer_class = CustomerSerializer
    permission_classes_by_action = {
        'me': [IsAuthenticated],
    }

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user) if not self.request.user.is_anonymous \
            else self.queryset.none()

    @swagger_auto_schema(operation_description='Detail current user information')
    @action(detail=False, methods=['get'], name='my-profile')
    def me(self, request):
        instance = get_object_or_404(User, user__id=request.user.id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)