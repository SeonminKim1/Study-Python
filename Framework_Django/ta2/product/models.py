from django.db import models
from sqlalchemy import ForeignKey

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=15),
    type = models.CharField(max_length=15),

class Drink(models.Model):
    name = models.CharField(max_length=15),
    category = ForeignKey('Category', on_delete=models.CASCADE)
    nutritional_info = models.CharField(max_length=100),
    allergy = models.CharField(max_length=100),


