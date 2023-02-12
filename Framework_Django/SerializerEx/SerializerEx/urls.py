from django.contrib import admin
from django.urls import path
from Serializer_Serializer.views import ProductAPIView
from Serializer_ModelSerializer.views import ProductModelAPIView

urlpatterns = [
    path('product', ProductAPIView.as_view()),
    path('product2', ProductModelAPIView.as_view())
]