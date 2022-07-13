import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class TinyURL(models.Model):
    url = models.CharField(max_length=200)
    alias = models.CharField(max_length=100)
    class Meta:
        db_table = 'tinyurl'


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256, )
    overview = models.CharField(max_length=1000)
    genres = models.CharField(max_length=256)
    poster = models.CharField(max_length=256)
    class Meta:
        db_table = 'movie'


    
