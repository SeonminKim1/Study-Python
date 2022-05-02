from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed, Reply
from user.models import User
# Create your views here.
class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all()
        relpy_list = Reply.objects.all()
        user = User.objects.all()
        return render(request, 'main/main_page.html', context=dict(feeds=feed_list, replys = relpy_list, user = user[0]))