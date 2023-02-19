from ninja import NinjaAPI
from django.contrib import admin
from django.urls import path

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app1.router.api import router as app1_router

api = NinjaAPI()
api.add_router("/app1/", app1_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]