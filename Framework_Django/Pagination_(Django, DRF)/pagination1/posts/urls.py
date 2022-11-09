# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('page/', views.DjangoPagination.as_view()),
]