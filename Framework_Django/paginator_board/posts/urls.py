from django.urls import path

from . import views

urlpatterns = [
    path('page/', views.expagination.as_view()),
]
