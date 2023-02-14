from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer

# url : posts/page/1
class DjangoPagination(APIView):
    def get(self, request):
        # pagination
        page = request.GET.get("page", 1) # 내가 로드하고자 하는 Page
        posts = Post.objects.all() # 전체 Load
        paginator = Paginator(posts, 3) # 한 페이지에 3개를 넘겨주는 paginator
        post_per_page = paginator.get_page(page) # 데이터에서 3단위로 나눠진 페이지의 N번째 페이지

        # serializer
        results = PostSerializer(post_per_page, many=True).data
        return Response(results, status=status.HTTP_200_OK)