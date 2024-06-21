from rest_framework import routers

from books.views import BookViewSet, BookAuthorViewSet, BookCategoryViewSet 


router = routers.DefaultRouter()
router.register(r'authors', BookAuthorViewSet, basename='BookAuthorViewSet')

app_name = "books"
urlpatterns = []
urlpatterns += router.urls