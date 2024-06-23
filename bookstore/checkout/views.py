from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated

from checkout.models import Order
from checkout.serializers import OrderSerializer

class OrderViewSet(CreateModelMixin,
                   RetrieveModelMixin,
                   ListModelMixin,
                   GenericViewSet):

    serializer_class = OrderSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.my_orders(self.request.user)