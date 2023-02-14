# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('page/', views.PostPagination4ViewSet.as_view({'get': 'list'})),
]