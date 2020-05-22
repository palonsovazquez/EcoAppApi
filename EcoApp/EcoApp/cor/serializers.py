from django.contrib.auth.models import User, Group
from rest_framework import serializers
from EcoApp.cor.models import Productos, Component


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productos
        fields = ['id','code','format','format','name','url', 'nick', 'avatar','components', 'description','status','date']


class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Component
        fields = ['code','name', 'recicleType','image' ]
