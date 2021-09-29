# from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import User, Group



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'group']
