from django.contrib import admin
from django.urls import path, include
from .views import SkillView, JobView

urlpatterns = [
    path('', SkillView.as_view()),
    path('job', JobView.as_view()),
]
