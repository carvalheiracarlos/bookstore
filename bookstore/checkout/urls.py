from rest_framework import routers

from checkout.views import OrderViewSet 


router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename='OrderViewSet')

app_name = "checkout"
urlpatterns = []
urlpatterns += router.urls