from rest_framework import routers

from customers.views import CustomerViewSet 


router = routers.DefaultRouter()
router.register(r'', CustomerViewSet, basename='CustomerViewSet')

app_name = "customers"
urlpatterns = []
urlpatterns += router.urls