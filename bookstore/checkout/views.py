from django_filters import rest_framework as filters
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated

from checkout.models import Order
from checkout.serializers import OrderSerializer
from checkout.filters import OrderFilter

class OrderViewSet(CreateModelMixin,
                   RetrieveModelMixin,
                   ListModelMixin,
                   GenericViewSet):

    serializer_class = OrderSerializer 
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OrderFilter

    def get_queryset(self):
        return Order.objects.my_orders(self.request.user)