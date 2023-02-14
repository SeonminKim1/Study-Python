# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('page/', views.PostPagination2ViewSet.as_view({'get': 'list'})),
]