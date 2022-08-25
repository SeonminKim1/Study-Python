from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import postSerializer

class expagination(APIView):
    def get(self, request):
        # pagination
        page = request.GET.get("page", 1)
        posts = Post.objects.all() # posts
        paginator = Paginator(posts, 3) # paginator
        post_per_page = paginator.get_page(page)

        # serializer
        results = postSerializer(post_per_page, many=True).data
        return Response(results, status=status.HTTP_200_OK)
