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

        # def create(self, validated_data):
        #     """
        #     Create and return a new `Serie` instance, given the validated data.
        #     """
        #     return Component.objects.create(**validated_data)

        # def update(self, instance, validated_data):
        #     """
        #     Update and return an existing `Serie` instance, given the validated data.
        #     """
        #     instance.code = validated_data.get('code', instance.code)
        #     instance.name = validated_data.get('name', instance.name)
        #     instance.recicleType = validated_data.get('recicleType', instance.recicleType)
        #     instance.rating = validated_data.get('image', instance.image)
        #     instance.save()
        #     return instance



class ProductSerializer(serializers.HyperlinkedModelSerializer):
    #components = ComponentSerializer(many=True, read_only=False)
    #fbuser = FirebaseUserSerializer(many=False, read_only=True)
    #fbuser = FirebaseUser.uid
    class Meta:
        model = Productos

        fields = ['id','code','format','name','image','fbuser','components', 'description','status','date']

        # def create(self, validated_data):
        #     """
        #     Create and return a new `Serie` instance, given the validated data.
        #     """
        #     return Productos.objects.create(**validated_data)
        #
        # def update(self, instance, validated_data):
        #     """
        #     Update and return an existing `Serie` instance, given the validated data.
        #     """
        #     instance.id = validated_data.get('id', instance.id)
        #     instance.code = validated_data.get('code', instance.code)
        #     instance.format = validated_data.get('format', instance.format)
        #     instance.name = validated_data.get('name', instance.name)
        #     instance.url= validated_data.get('url', instance.url)
        #     instance.nick = validated_data.get('nick', instance.nick)
        #     instance.avatar = validated_data.get('avatar', instance.avatar)
        #     instance.components = validated_data.get('components', instance.components)
        #     instance.description = validated_data.get('description', instance.description)
        #     instance.status = validated_data.get('status', instance.status)
        #     instance.date = validated_data.get('date', instance.date)
        #     instance.save()
        #     return instance


class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Component
        fields = ['code','name', 'recycleType','image' ]

        # def create(self, validated_data):
        #     """
        #     Create and return a new `Serie` instance, given the validated data.
        #     """
        #     return Component.objects.create(**validated_data)

        # def update(self, instance, validated_data):
        #     """
        #     Update and return an existing `Serie` instance, given the validated data.
        #     """
        #     instance.code = validated_data.get('code', instance.code)
        #     instance.name = validated_data.get('name', instance.name)
        #     instance.recicleType = validated_data.get('recicleType', instance.recicleType)
        #     instance.rating = validated_data.get('image', instance.image)
        #     instance.save()
        #     return instance
