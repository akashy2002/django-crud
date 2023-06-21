from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Registration(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    up_pic = models.ImageField(upload_to="picture")


class Crudcard(models.Model):
    roll = models.CharField(max_length=30, null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.BigIntegerField(default=0)
    address = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
