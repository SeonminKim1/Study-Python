from django.shortcuts import render
from .models import Category

def main_view(requst):
    if requst.method == 'GET':
        category = list(Category.objects.all())
        render('a.html', {'category':category})

# Create your views here.
