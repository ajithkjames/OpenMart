# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.db.models import F
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
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
	queryset = Advertisement.objects.all().order_by('-created_at')
	parser_classes = (MultiPartParser, FormParser,)
	permission_classes = (AdvertisementPermission,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('title','category__name','description')

	def get_serializer_class(self):
		if self.request.method != 'GET': 
			self.serializer_class = AdvertisementCreateSerializer 
		return self.serializer_class

	def retrieve(self, request, pk=None):
		queryset = Advertisement.objects.all()
		advertisement = get_object_or_404(queryset, pk=pk)
		Advertisement.objects.filter(pk=pk).update(views=F('views') + 1)
		advertisement.views += 1 
		serializer = AdvertisementSerializer(advertisement)
		return Response(serializer.data)

	def perform_create(self, serializer):
		serializer.save(image=self.request.data.get('image'), author=self.request.user)
		return Response(serializer.data)