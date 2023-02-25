from django.db import models


# Create your models here.
class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    writer = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
