#coding: utf-8 -*-
import uuid
import json

from django.db import models
from django.utils import timezone


# model of Component
# Class to store prototype of a component common to some of the products.
from django.utils.encoding import smart_str


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

    code = models.IntegerField(primary_key=True,unique=True,editable=False)
    name = models.CharField(max_length=200)
    recycleType = models.IntegerField(choices = Suit.choices, null = True)
    # a cambiar  recicleType = models.IntegerChoices('recicleType','Envases Vidrio Papel Organico Medicamentos Restos Punto_Limpio Pilas Aceite Ropa')
    #recicleType = models.IntegerField(null= True)
    image = models.ImageField(upload_to="Components/Images", height_field=None, width_field=None, max_length=100, )

    def __str__(self):
        return self.name

# script to load components from json



try:
    with open("components.json", "r",encoding='utf-8') as read_file:

        data = json .load(read_file )
        if 'components' in data:
            print('test1')
            for component in data['components']:
                print(component['name'])

                imagen = smart_str(component['image'])
                imagen = "/Components/Images/" + imagen.split("/media/Components/Images/")[1]

                componentdb = Component(code=component['code'], name=component['name'],
                                        recycleType=component['recycleType'], image=imagen)
                componentdb.save()
                print(componentdb)
except:
    print("error")





# model of product
# Class to store the data about a object with a code to identify it.



class Productos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(unique=True, max_length=200)
    format = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    components = models.ManyToManyField(Component)
    image = models.ImageField(upload_to="Products/Images", height_field=None, width_field=None, max_length=100,null=True)
#    uid = models.id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    fbuser = models.ForeignKey('auth.User',on_delete=models.DO_NOTHING , null=True ,default='1',editable=True)
    #nick = models.CharField(max_length=200)
    #avatar = models.ImageField(upload_to="Users/Avatars", height_field=None, width_field=None, max_length=100,)
    description = models.TextField(null=True, default="")
    status = models.IntegerField(default=1)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# with open("productos.json", "r") as read_file:
#     data = json.load(read_file)
#     if 'productos' in data:
#         print('test12')
#         for productos in data['productos']:
#             print('test22')
#             componentssaved = []
#             for compon in productos['components']:
#                 print('compon' + compon)
#                 componentssaved.append(compon)
#             produc = Productos(id=productos['id'], code=productos['code'], format=productos['format'],
#                                 image=productos['image'], fbuser=productos['fbuser'],
#                                description=productos['description'], status=productos['status'], date=productos['date'])
#             produc.components.set(compon)
#             produc.save()
#             print(produc)
