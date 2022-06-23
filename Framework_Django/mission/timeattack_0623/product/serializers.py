from rest_framework import serializers
from .models import categories, item_orders, items, orders

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):
    pass