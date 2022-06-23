from django.contrib.auth import login, authenticate, logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer

class UserApiView(APIView):
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        
        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)

    # user 정보 조회
    def get(self, request):
        login_user = request.user
        print(login_user, type(login_user))
        if login_user != None:
            # login_user_id = login_user.id
            # user queryset => Serializer orderdict
            serialized_user_data = UserSerializer(login_user).data
            print(serialized_user_data, type(serialized_user_data))

            # Article queryset => Serializer Orderdict
            #articles_queryset = Article.objects.filter(writer_id=login_user_id)
            #serialized_article_data = ArticleSerializer(articles_queryset, many=True).data # type : orderdict 

            return Response({
                "message": "조회 성공!!", 
                'user_data': serialized_user_data, 
                #'article_data':serialized_article_data,
                }, status=status.HTTP_200_OK)
        return Response({'message':'로그인 된 유저가 없습니다'})

    # 로그아웃
    def delete(self, request):
        is_login = request.user.is_authenticated
        # print('== 로그인 상태 여부', is_login)
        if is_login:
            logout(request)
        return Response({"message": "로그아웃 성공!!"}, status=status.HTTP_200_OK)
    