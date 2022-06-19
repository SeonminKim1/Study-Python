from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission

from user.models import User
from .models import Article, Category
from .serializers import ArticleSerializer

from datetime import timedelta
from django.utils import timezone

class RegistedMoreThanMinutesUser(BasePermission):
    """
    가입 후 3분 이상 지난 사용자만 접근 가능
    """
    message = '가입 후 3일 이상 지난 사용자만 사용하실 수 있습니다.'
    # test_message = '가입 후 3분 이상 지난 사용자만 사용하실 수 있습니다.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.join_date < (timezone.now() - timedelta(days=3))) # (minutes=3)

class ArticleApiView(APIView):
    permission_classes = [RegistedMoreThanMinutesUser]

    # 글 조회
    def get(self, request):
        login_user = request.user
        login_user_id = login_user.id
        # Article queryset => Serializer Orderdict
        articles_queryset = Article.objects.filter(writer_id=login_user_id)
        serialized_article_data = ArticleSerializer(articles_queryset, many=True).data # type : orderdict 

        return Response({
            "message": "조회 성공!!", 
            'article_data':serialized_article_data,
        }, status=status.HTTP_200_OK)

    # 글 작성
    def post(self, request):
        login_user_id = (request.user).id
        title = request.data.get('title', '')
        category = request.data.get('category', '')
        contents = request.data.get('contents', '')
        print('===', title, category, contents)
        if len(title) <= 5: 
            return Response({"message":"글 작성 실패 - 글 제목 5자 이하"})
        if len(contents) <= 20:
            return Response({'message': "글 작성 실패 - 글 내용 20자 이하"})    
        if category == '':
            return Response({'message': "글 작성 실패 - 카테고리 지정 X"})
        
        # print(Category.objects.all().values())
        category_queryset = Category.objects.filter(name__in = [category])        
        # print('=== category_queryset', type(category_queryset))
        if len(category_queryset) == 0:
            return Response({'message': "글 작성 실패 - 카테고리 지정 X"})

        user_table = User.objects.get(id=login_user_id)
        Article.objects.create(
            writer=user_table,
            title=title,
            category=category_queryset[0],
            content=contents,
        )

        return Response({"message": "글 작성 성공!!"}, status=status.HTTP_200_OK)


