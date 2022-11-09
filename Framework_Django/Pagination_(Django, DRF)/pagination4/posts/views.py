from rest_framework import viewsets
from rest_framework.pagination import CursorPagination # Cursor 기반 (next, prev 버튼) Pagination

from .models import Post
from .serializers import PostSerializer

class Pagination4(CursorPagination): # settings.py의 CursorPagination 상속
    page_size = 3 # Default 2 => 3으로 
    ordering = 'title' # 정렬 기준도 가능


# url : posts/page?limit=4&offset=2
class PostPagination4ViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = Pagination4 #