from network.apps import NetworkConfig
from rest_framework.routers import DefaultRouter
from network.views import NetworkNodeViewSet

app_name = NetworkConfig.name
router = DefaultRouter()
router.register(r'', NetworkNodeViewSet, basename='network')

urlpatterns = [

] + router.urls
