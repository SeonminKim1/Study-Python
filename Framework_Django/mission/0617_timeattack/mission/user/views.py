from django.shortcuts import render

from django.contrib.auth import login, authenticate, logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User

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

    # 글 조회
    def get(self, request):
        login_user = request.user
        if login_user:
            login_user_id = login_user.id
            print(login_user_id)
            # articles = Article.objects.filter(writer_id=login_user_id)
            # article_list = [article.title for article in articles]
            # return Response({"message": "글 조회 성공!!", 'article_list':article_list}, status=status.HTTP_200_OK)
        return Response({'message':'로그인 된 유저가 없습니다'})

    # 로그아웃
    def delete(self, request):
        is_login = request.user.is_authenticated
        # print('== 로그인 상태 여부', is_login)
        if is_login:
            logout(request)
        return Response({"message": "로그아웃 성공!!"}, status=status.HTTP_200_OK)
    