from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination # Limit Offset 기반 Pagination

from .models import Post
from .serializers import PostSerializer

class Pagination3(LimitOffsetPagination): # settings.py의 LimitOffsetPagination 상속
    # 몇개의 Object를 가져올건지
    default_limit = 3 # Default 2 => 3으로 (사실상 PAGE_SIZE와 같은 역할을 함)

# url : posts/page?limit=4&offset=2
class PostPagination3ViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = Pagination3 #