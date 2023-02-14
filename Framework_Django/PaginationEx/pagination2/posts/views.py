from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination # 페이지 기반 파지네이션 import

from .models import Post
from .serializers import PostSerializer

class Pagination2(PageNumberPagination): # settings.py의 PageNumberPagination 상속
    page_size = 3 # Default 2 => 3으로

# url : posts/page/1
class PostPagination2ViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = Pagination2 # 