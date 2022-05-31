from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator
# from django.core.validators import validate_email

class UserModel(models.Model):
    class Meta:
        db_table = "my_user"
    email = models.CharField(max_length=20, null=False, validators=[EmailValidator])
    password = models.CharField(max_length=256, null=False, validators=[MinLengthValidator(4)])