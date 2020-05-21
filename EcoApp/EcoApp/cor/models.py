import uuid

from django.db import models
from django.db import models
from django.utils import timezone

#model of component
"""
class Component(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

"""




# model of product
class Productos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=200)
    format = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    url =models.ImageField(upload_to="Products/Images", height_field=None, width_field=None, max_length=100)
    uid = models.id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    nick = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to="Users/Avatars", height_field=None, width_field=None, max_length=100)
    description = models.TextField()
    status = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)



