from rest_framework import serializers
from account.models import User
from market.models import Category, Advertisement


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username','first_name','phone')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class AdvertisementSerializer(serializers.ModelSerializer):

    author = BaseUserSerializer(read_only=True)
    class Meta:
        model = Advertisement
        fields = ('author','title','description','price','category','views','image')


class AdvertisementCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ('author','title','description','price','category','views','image')
