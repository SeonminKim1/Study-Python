from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductModelSerializer
from Serializer_Serializer.models import Product

'''
/product 
- POST : http://127.0.0.1:8000/product2
body : {
    "name":"ahhhh",
    "price":5
}
- GET : http://127.0.0.1:8000/product2?product_id=2
- PUT : http://127.0.0.1:8000/product2
body : {
    "id":3,
    "name":"acca",
    "price":10000
}
- DELETE : http://127.0.0.1:8000/product2?product_id=1
'''
class ProductModelAPIView(APIView):
    # 생성
    def post(self, request):
        product_serializer = ProductModelSerializer(data=request.data)
        product_serializer.is_valid(raise_exception=True) # 400 Response
        product_serializer.save() # .validated_data
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)

    # 수정
    def put(self, request):
        obj = Product.objects.get(id=request.data['id'])
        product_serializer = ProductModelSerializer(obj, data=request.data)
        product_serializer.is_valid(raise_exception=True) # 400 Response
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    # 모두 조회
    def get(self, request):
        data = Product.objects.get(id=int(request.query_params['product_id']))
        serializer_data = ProductModelSerializer(data).data
        return Response(serializer_data, status=status.HTTP_200_OK)

    # 삭제
    def delete(self, request):
        obj = Product.objects.get(id=int(request.query_params['product_id']))
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        