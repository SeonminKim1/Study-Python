from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def read_article(request):
    # Read
    if request.method == 'GET':
        all_article = Article.objects.all()
        return render(request, 'base.html', {'all_article':all_article})

def create_article(request):
    if request.method =='POST':
        article = Article()  # 글쓰기 모델 가져오기
        article.author = request.POST.get('author', ' ')
        article.title = request.POST.get('title', ' ')
        article.number = int(request.POST.get('number', 0))
        article.content = request.POST.get('content', ' ')
        article.save()
        return redirect('/')
    
def update_article(request):
    if request.method =='POST':
        number = int(request.POST.get('number', 0))
        article = Article.objects.get(number=int(number))
        article.author = request.POST.get('author', ' ')
        article.title = request.POST.get('title', ' ')
        article.content = request.POST.get('content', ' ')
        article.save()
        return redirect('/')

def delete_article(request, number):
    article = Article.objects.get(number=int(number))
    article.delete()
    return redirect('/')
