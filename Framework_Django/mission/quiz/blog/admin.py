from django.contrib import admin
from .models import Article, Cateogory

# Register your models here.
admin.site.register(Article)
admin.site.register(Cateogory)