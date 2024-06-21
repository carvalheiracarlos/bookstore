from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from books.models import Book, BookCategory, BookAuthor
from books.serializers import BookSerializer, BookCategorySerializer, BookAuthorSerializer
from books.filters import BookFilter
from core.mixins import PermissionsByActionMixin

class BookViewSet(CreateModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  ListModelMixin,
                  PermissionsByActionMixin,
                  GenericViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    filter_class = BookFilter 
    permission_classes_by_action = {
        'create': [IsAdminUser],
        'destory': [IsAdminUser],
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
    }

class BookCategoryViewSet(CreateModelMixin,
                          RetrieveModelMixin,
                          ListModelMixin,
                          PermissionsByActionMixin,
                          GenericViewSet):

    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer 
    permission_classes_by_action = {
        'create': [IsAdminUser],
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
    }
class BookAuthorViewSet(CreateModelMixin,
                        RetrieveModelMixin,
                        ListModelMixin,
                        GenericViewSet):

    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    permission_classes_by_action = {
        'create': [IsAdminUser],
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
    }