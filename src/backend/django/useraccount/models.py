from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=256, primary_key=True)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=256, null=True)
    address = models.CharField(max_length=256, null = True)
