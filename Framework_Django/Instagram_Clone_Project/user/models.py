from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.TextField()
    name = models.TextField()
    nickname = models.TextField()
    profile_image = models.TextField()