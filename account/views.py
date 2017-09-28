# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from account.models import User
from account.serializers import UserSerializer
from account.permissions import UserPermissions

class UserViewSet(viewsets.ModelViewSet):
	"""User API view"""
 
	serializer_class = UserSerializer
	queryset = User.objects.all()
	permission_classes = (UserPermissions,)


class profileView(APIView):

    serializer_class = UserSerializer

    def get(self, request, format=None):

        user = User.objects.get(pk=self.request.user.id)
        data = self.serializer_class(user)
        return Response(data.data)