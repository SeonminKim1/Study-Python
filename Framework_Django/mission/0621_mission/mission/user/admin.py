from django.contrib import admin
from .models import User, UserProfile, Hobby

from django.contrib.auth.admin import UserAdmin

class UserProfileAdmin(UserAdmin):
    list_display = ('introduction','birthday','age') # 'user','hobby',
    list_display_links = ('introduction',)
    list_filter = ('age', )
    search_fields = ('birthday', 'age', )
    ordering = ('introduction',)

    fieldsets = (
        ("info", {'fields': ('introduction', 'birthday', 'age',)},),
        )

    filter_horizontal = []

class UserAdmin(UserAdmin):
    list_display = ('id', 'username', 'fullname', 'email')
    list_display_links = ('username', )
    list_filter = ('username', )
    search_fields = ('username', 'email', )

    fieldsets = (
        ("info", {'fields': ('username', 'password', 'email', 'fullname', 'join_date',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active', )}),)

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date', )
        else:
            return ('join_date', )

#admin.site.register(User)
admin.site.register(User)
admin.site.register(UserProfile, UserProfileAdmin) # 
admin.site.register(Hobby)