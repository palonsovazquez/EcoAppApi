import uuid

from django.db import models
from django.db import models
from django.utils import timezone
from drf_firebase_auth.models import FirebaseUser





#model of Component




class Component(models.Model):
    class Suit(models.IntegerChoices):
        Envases = 1
        Vidrio = 2
        Papel = 3
        Organico = 4
        Medicamentos = 5
        Restos = 6
        Punto_Limpio = 7
        Pilas = 8
        Aceite = 9
        Ropa = 10

    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    recicleType = models.IntegerField(choices = Suit.choices, null = True)
    # a cambiar  recicleType = models.IntegerChoices('recicleType','Envases Vidrio Papel Organico Medicamentos Restos Punto_Limpio Pilas Aceite Ropa')
    #recicleType = models.IntegerField(null= True)
    image = models.ImageField(upload_to="Components/Images", height_field=None, width_field=None, max_length=100, )

    def __str__(self):
        return self.name


# model of product




class Productos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(unique=True, max_length=200)
    format = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    components = models.ManyToManyField(Component)
    url = models.ImageField(upload_to="Products/Images", height_field=None, width_field=None, max_length=100,)
    uid = models.id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    fbuser = models.ForeignKey(FirebaseUser,on_delete=models.DO_NOTHING , null=True)
    nick = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to="Users/Avatars", height_field=None, width_field=None, max_length=100,)
    description = models.TextField()
    status = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name



