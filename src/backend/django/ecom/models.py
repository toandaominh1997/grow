from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    image_url = models.CharField(max_length=256)
    class Meta:
        db_table = "product"
