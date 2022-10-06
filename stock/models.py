
from django.db import models
from django.contrib.auth.models import User

class UpdateCreate(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name



class Brand(models.Model):
    name=models.CharField(max_length=35)

    def __str__(self):
        return self.name


    



