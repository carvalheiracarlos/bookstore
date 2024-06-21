from rest_framework import routers

from books.views import BookViewSet, BookAuthorViewSet, BookCategoryViewSet 


router = routers.DefaultRouter()
router.register(r'book', BookViewSet, basename='BookViewSet')
router.register(r'authors', BookAuthorViewSet, basename='BookAuthorViewSet')
router.register(r'category', BookCategoryViewSet, basename='BookCategoryViewSet')

app_name = "books"
urlpatterns = []
urlpatterns += router.urls