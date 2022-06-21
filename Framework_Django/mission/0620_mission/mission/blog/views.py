from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission

from user.models import User
from .models import Article, Category
from .serializers import ArticleSerializer

from datetime import timedelta, datetime
from django.utils import timezone
from django.db.models import Q

from rest_framework.exceptions import APIException
from rest_framework import status

class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

class IsAdminOrIsAuthenticatedReadOnly(BasePermission):
    """
    admin 사용자는 모두 가능, 로그인 사용자는 조회만 가능
    """
    SAFE_METHODS = ('GET', )
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response ={
                    "detail": "서비스를 이용하기 위해 로그인 해주세요.",
                }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_authenticated and user.is_admin:
            return True
            
        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True
        
        return False
class RegistedMoreThan7daysUser(BasePermission):
    message = '가입 후 7일 이상 지난 사용자만 사용하실 수 있습니다.'
    # test_message = '가입 후 3분 이상 지난 사용자만 사용하실 수 있습니다.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.join_date < (timezone.now() - timedelta(days=3))) # (days=7)

class ArticleApiView(APIView):
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly, RegistedMoreThan7daysUser]

    # 글 조회
    def get(self, request):
        login_user = request.user
        login_user_id = login_user.id
        # Article queryset => Serializer Orderdict
        
        articles_queryset = Article.objects.filter(Q(writer_id=login_user_id) & Q(expose_start_date__lte=timezone.now()) & Q(expose_end_date__gte=timezone.now()))\
            .order_by('writing_date')
        serialized_article_data = ArticleSerializer(articles_queryset, many=True).data # type : orderdict 

        # 3. article view에 게시글 조회 기능을 만들되, 현재 일자를 기준으로 노출 시작 일자와 노출 종료 일자 사이에 있는 항목들만 리턴해주도록 필터를 설정해주세요
        # - 리턴 데이터는 게시글 작성일 기준으로 정렬하여 최근 쓴 글이 가장 먼저 올라오도록 해주세요
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
        expose_start_date = datetime.strptime(request.data.get('expose_start_date', datetime.now()), '%Y%m%d')
        expose_end_date = datetime.strptime(request.data.get('expose_end_date', datetime.now()), '%Y%m%d')

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
            expose_start_date = expose_start_date,
            expose_end_date = expose_end_date,
            writing_date = timezone.now()
        )

        return Response({"message": "글 작성 성공!!"}, status=status.HTTP_200_OK)


