from django_filters import rest_framework as filters

from checkout.models import Order


class OrderFilter(filters.FilterSet):
    customer_name = filters.CharFilter(field_name='customer__name', lookup_expr='icontains')
    customer_cpf = filters.CharFilter(field_name='customer__cpf', lookup_expr='icontains')
    release_year = filters.NumberFilter(field_name='book__release_year')
    author = filters.CharFilter(field_name='book__author__name', lookup_expr='icontains')
    category = filters.CharFilter(field_name='book__category__name', lookup_expr='icontains')
    order_by = filters.CharFilter(method='get_order_by', label='order_by')

    class Meta:
        model = Order 
        fields = [
            'customer_name',
            'customer_cpf',
            'release_year'
            'author',
            'category',
            'order_by'
        ]

    def get_order_by(self, queryset, name, value):
        if value is None:
            return queryset
        else:
            return queryset.order_by(value)