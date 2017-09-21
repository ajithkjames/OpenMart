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
        fields = ('id','name','created_at','updated_at')


class AdvertisementSerializer(serializers.ModelSerializer):

    author = BaseUserSerializer(read_only=True)
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
     )
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id','author','title','description','price','category','views','image','created_at','updated_at')


class AdvertisementCreateSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
    )
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id','author','title','description','price','category','image')
