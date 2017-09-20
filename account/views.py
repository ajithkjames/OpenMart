# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from account.models import User
from account.serializers import UserSerializer
from account.permissions import UserPermissions

class UserViewSet(viewsets.ModelViewSet):
	"""User API view"""
 
	serializer_class = UserSerializer
	queryset = User.objects.all()
	permission_classes = (UserPermissions,)
