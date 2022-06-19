from .serializers import PostSerializer
from .models import Post

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PostView(APIView):
    def get(self ,request):
        queryset = Post.objects.all()
        print('=== Queryset Data : ', queryset)

        # serializer에 queryset을 인자로 줄 경우 many=True 옵션을 사용해야 한다.
        serializer_class = PostSerializer(queryset, many=True) # OrderedDict
        print('=== Serializer Data : ', serializer_class.data)
        # Signature: Response(data, status=None, template_name=None, headers=None, content_type=None)
        return Response(data = serializer_class.data, status=status.HTTP_200_OK)

