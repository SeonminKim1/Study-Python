from django.db import models

class Product(models.Model):
    name = models.CharField("이름", max_length=20)
    price = models.IntegerField('가격', default=0)

    class Meta:        
        db_table = "PRODUCT"
