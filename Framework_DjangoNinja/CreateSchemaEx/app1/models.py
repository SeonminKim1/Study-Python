from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20, default="개발")


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
