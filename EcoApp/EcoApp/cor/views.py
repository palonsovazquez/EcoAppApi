from django.contrib.auth.models import User, Group
from drf_firebase_auth.models import FirebaseUserProvider, FirebaseUser
from rest_framework import viewsets
from rest_framework import permissions
from EcoApp.cor.serializers import UserSerializer, GroupSerializer, ProductSerializer, ComponentSerializer, \
    FirebaseUserSerializer
from EcoApp.cor.models import Productos, Component
from django_filters.rest_framework import DjangoFilterBackend

class FirebaseUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FirebaseUser.objects.all().order_by('uid')
    serializer_class = FirebaseUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['uid']
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComponentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Product to be viewed or edited.
    """
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code']





class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Product to be viewed or edited.
    """
    queryset = Productos.objects.all().order_by(('date')).reverse()  ## cambiar por asc() si no funciona bien
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code','fbuser']


