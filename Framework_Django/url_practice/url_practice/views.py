from django.http import HttpResponse
from django.shortcuts import render

def http_response_view(request):
    return HttpResponse("HTTP Response를 사용했어요.")

def render_view(request):
    return render(request, 'project_base.html')