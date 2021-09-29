from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    def __str__(self):
        return str(self.username)
class Group(models.Model):
    name = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)
