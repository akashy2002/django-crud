from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Registration(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=50, )
    password2 = models.CharField(max_length=50,)

    def __str__(self):
        return self.username


class Crudcard(models.Model):
    roll = models.CharField(max_length=30, null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.BigIntegerField(default=0)
    address = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
