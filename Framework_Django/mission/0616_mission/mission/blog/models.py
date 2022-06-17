from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    name = models.TextField('이름', max_length=20)
    description = models.TextField('설명', max_length=50)

    def __str__(self):
        return "category"

class Article(models.Model):
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.TextField('제목', max_length=20)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    content = models.TextField('글 내용', max_length=100)

    def __str__(self):
        return "article"
