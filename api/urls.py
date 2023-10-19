from django.urls import path

from . import views
from rest_framework.routers  import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet)
router.register('products', views.ProductViewSet)
router.register('orders', views.OrderViewSet)
urlpatterns=router.urls 