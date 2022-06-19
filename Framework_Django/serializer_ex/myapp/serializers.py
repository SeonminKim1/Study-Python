from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    text = serializers.CharField()
    
    class Meta:
        model = Post
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ("title", "text")