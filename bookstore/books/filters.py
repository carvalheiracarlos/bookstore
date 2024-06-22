from django_filters import rest_framework as filters

from books.models import Book


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    release_year = filters.NumberFilter(field_name='release_year')
    author = filters.CharFilter(field_name='book___author_name', lookup_expr='icontains')
    category = filters.CharFilter(field_name='book___category_name', lookup_expr='icontains')
    order_by = filters.CharFilter(method='get_order_by', label='order_by')

    class Meta:
        model = Book
        fields = [
            'title',
            'release_year',
            'author',
            'category',
            'order_by'
        ]

    def get_order_by(self, queryset, name, value):
        if value is None:
            return queryset
        else:
            return queryset.order_by(value)