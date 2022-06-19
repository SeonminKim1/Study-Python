from rest_framework import serializers
from .models import User, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    """
    외래 키는 UserProfile에서 User 테이블로 설정되어 있지만
    one to one 필드기 때문에 userprofile이라는 명칭으로 역참조가 가능하다.
    """
    userprofile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ["username", "password", "fullname", "email", "userprofile"]

''' blog/serializers.py 로 이전
from blog.models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
   # 1대1 관계가 아니면 many=True
   article_comment = CommentSerializer(many=True)
   class Meta:
        # serializer에 사용될 model, field지정
        model = Article
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["content", 'article_comment'] # 반드시 tuple or list
        # related name 과 같아야 됨.

'''