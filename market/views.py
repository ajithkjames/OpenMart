# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from account.models import User
from market.models import Category, Advertisement
from market.serializers import CategorySerializer, AdvertisementSerializer, AdvertisementCreateSerializer
from market.permissions import CategoryPermission, AdvertisementPermission



class CategoryViewSet(viewsets.ModelViewSet):
	"""Category API view"""

	serializer_class = CategorySerializer
	queryset = Category.objects.all()
	permission_classes = (CategoryPermission,)


class AdvertisementViewSet(viewsets.ModelViewSet):
	"""Advertisement API view"""

	serializer_class = AdvertisementSerializer
	queryset = Advertisement.objects.all()
	permission_classes = (AdvertisementPermission,)

	def get_serializer_class(self):
		if self.request.method != 'GET': 
			self.serializer_class = AdvertisementCreateSerializer 
		return self.serializer_class