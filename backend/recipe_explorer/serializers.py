from rest_framework import serializers
from django.contrib.auth.models import User
from recipe_explorer.models import FavoriteModel 

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = FavoriteModel
        fields = "__all__"