from django.contrib import admin
from .models import User, UserProfile, Hobby

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Hobby)