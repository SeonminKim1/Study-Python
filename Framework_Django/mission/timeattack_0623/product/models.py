from django.db import models

# Create your models here.
class orders(models.Model):
    delivery_address = models.CharField('배달주소',max_length=100)
    order_date = models.DateField('주문일')

class items(models.Model):
    name = models.CharField('아이템 이름', max_length=100)
    image_url = models.CharField('이미지 원본 링크', max_length=200)
    category = models.ForeignKey(to='categories', on_delete=models.CASCADE)

class categories(models.Model):
    name = models.CharField('카테고리 이름', max_length=100)

class item_orders(models.Model):
    item_count = models.IntegerField(verbose_name='아이템 갯수')
    item = models.ForeignKey(to=items, on_delete=models.CASCADE)
    order = models.ForeignKey(to=orders, on_delete=models.CASCADE)
    