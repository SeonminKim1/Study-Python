from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from .models import categories, item_orders, items, orders
from .serializers import CategorySerializer
# Create your views here.
class get_product(APIView):
    def get(self, request, category):
        
        filter_data = items.objects.filter(category=categories(category))
        print(filter_data)
        # serialized_data = CategorySerializer(filter_data, many=True)
        return Response({'message':'ok'}, status=status.HTTP_200_OK) 