from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.core.cache import cache

CACHE_KEY = 'category_list3'

class cachingView(APIView):
    def get(self, request):
        cache_value = cache.get(CACHE_KEY, None)
        if cache_value == None:
            cache.set(CACHE_KEY, 'DB Value') # key, value, expriation time
            cache_value = 'DB Value'
        return Response({'cache_value' : cache_value}, status=status.HTTP_200_OK)