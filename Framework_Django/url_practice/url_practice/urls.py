"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

from p_app1 import views as app1
urlpatterns = [
    # case1 . Function Views
    path('admin/', admin.site.urls),
    path('test1/', views.http_response_view),  # HTTP Response
    path('test2/', views.render_view), # render 방법

    # case 2. direct app view
    path('test3/', app1.app_render_view), # render 방법

    # case 3. include  - path 앞 부분은 prefix 개념.
    path('test4/', include('p_app1.urls')), # p_app1의 url들과 연결
]
