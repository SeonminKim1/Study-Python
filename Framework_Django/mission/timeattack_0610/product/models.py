from django.db import models
from user.models import User

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'Category'

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    price = models.FloatField()
    stock = models.IntegerField()

    class Meta:
        db_table = 'Product'
    
# 배송 상태
class OrderStatus(models.Model):
    status = models.CharField(max_length=10) # 주문 완료, 결제 완료, 취소, 배송출발, 배송완료

    class Meta:
        db_table = 'OrderStatus'

# 상품 갯수 저장 (주문정보)
class ProductOrder(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    class Meta:
        db_table = 'ProductOrder'
      
# User의 주문 정보
class UserOrder(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    now_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)

    address = models.CharField(max_length=100)
    order_time = models.DateTimeField(auto_now=True)
    all_product_price = models.FloatField()
    discount_rate = models.FloatField()
    final_price = models.FloatField()
    is_valid = models.BooleanField(default=False)
    class Meta:
        db_table = 'UserOrder'