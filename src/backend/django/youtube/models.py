from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=256)
    origin_url = models.CharField(max_length=256)
    description = models.CharField(max_length=256, null = True)
    s3_url = models.CharField(max_length=256, null = True)
    class Meta:
        db_table = "Video"
