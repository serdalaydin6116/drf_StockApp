
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


class Product(UpdateCreate):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='c_products')
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='b_products')
    stock=models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Firm(UpdateCreate):
    name=models.CharField(max_length=25)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=200)  ##textfield gereksiz uzun yer kaplar..

    def __str__(self):
        return self.name

