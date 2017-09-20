from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from market.views import CategoryViewSet, AdvertisementViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, 'categories')
router.register(r'advertisement', AdvertisementViewSet, 'advertisements')

urlpatterns = [
	
]

urlpatterns += router.urls