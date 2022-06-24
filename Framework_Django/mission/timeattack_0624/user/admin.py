from django.contrib import admin
from . import models

from django.contrib.auth.admin import UserAdmin


# admin.site.register(models.User)
admin.site.register(models.UserType)
admin.site.register(models.UserLog)


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ("email", )
    # pass
