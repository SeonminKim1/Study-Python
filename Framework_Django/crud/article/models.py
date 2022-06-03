from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=20)
    number = models.IntegerField(default=0)
    content = models.TextField(max_length=256)
    
