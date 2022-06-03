from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    class Meta:
        db_table = "custom_user"
    # 기본 값들은 다 Django의 AbstractUser 것들 따라쓸꺼임.
    etc_text = models.CharField(max_length=256, default='')