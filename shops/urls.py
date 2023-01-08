from django.urls import path, include
from shops.views import ShopView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from shops.views import get_shop_status


router = DefaultRouter()
router.register('shops', ShopView, basename='shop')


 
urlpatterns = [
    path('', include(router.urls)),
    path('shop_status/', get_shop_status, name='status'),
    
] 
