from django.db import models

# Create your models here.

class Tinyurl(models.Model):
    alias = models.CharField(max_length=128)
    long_url = models.CharField(max_length=256)
    domain = models.CharField(max_length=256)
    class Meta:
        db_table = "tiny_url"

