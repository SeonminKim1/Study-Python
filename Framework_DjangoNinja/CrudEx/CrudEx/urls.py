from ninja import NinjaAPI
from django.contrib import admin
from django.urls import path

from .basicDemo.api import router as basic_router
from .crudDemo.api import router as crud_router

api = NinjaAPI()
api.add_router("/basic/", basic_router)
api.add_router("/crud/", crud_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]