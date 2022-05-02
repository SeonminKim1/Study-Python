# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

class Sub(APIView):
    def get(self, request):
        print('Get 호출')
        # return HttpResponse("Hello, world. You're at the polls index.")
        # return render(request, 'Instagram_Clone_Project/C.html')

    def post(self, request):
        print('Post 호출') 
        return HttpResponse("Hello, world. You're at the polls index.")
        # return render(request, 'Instagram_Clone_Project/templates/main.html')