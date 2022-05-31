from django.urls import path
from . import views

urlpatterns = [
    path('test4/', views.app_render_view2) # user앱의 urls.py와 연결
]
