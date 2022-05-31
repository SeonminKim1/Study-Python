from django.db import models

# Create your models here.
class Cateogory(models.Model):
    class Meta:
        db_table = "category"

    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "article"

    title = models.CharField(max_length=256)
    category = models.ForeignKey(Cateogory, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)


