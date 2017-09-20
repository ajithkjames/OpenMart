from rest_framework import permissions
from rest_framework import authentication
from account.models import *
from market.models import *


class CategoryPermission(permissions.IsAuthenticated):


    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        else:
            if request.method in ('HEAD', 'OPTIONS', 'GET'):
                return True
            return False

class AdvertisementPermission(permissions.IsAuthenticated):


    def has_object_permission(self, request, view, obj):
        if obj.author== request.user or request.user.is_superuser:
            return True
        else:
            if request.method in ('HEAD', 'OPTIONS', 'GET'):
                return True
            return False
