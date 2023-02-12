from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, obj, validated_data):
        obj.name = validated_data.get('name', obj.name)
        obj.price = validated_data.get('price', obj.price)
        obj.save()
        return obj

    def validate(self, value):
        if value.get('name') =='abc':
            raise serializers.ValidationError("Name must not be abc")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price is < 0")
        return value