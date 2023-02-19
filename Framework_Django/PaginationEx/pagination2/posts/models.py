from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta:
        db_table = "article"
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=256)