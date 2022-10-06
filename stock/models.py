
from django.db import models
from django.contrib.auth.models import User

class UpdateCreate(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
    



