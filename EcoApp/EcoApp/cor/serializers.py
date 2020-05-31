from django.contrib.auth.models import User, Group
from rest_framework import serializers
from EcoApp.cor.models import Productos, Component
from drf_firebase_auth.models import FirebaseUserProvider, FirebaseUser




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','first_name','last_name', 'email', 'groups']

class FirebaseUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = FirebaseUser
        fields = ['id','uid', 'user']




class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Component
        fields = ['code','name', 'recycleType','image' ]





class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Productos

        fields = ['id','code','format','name','image','fbuser','components', 'description','status','date']




class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Component
        fields = ['code','name', 'recycleType','image' ]


