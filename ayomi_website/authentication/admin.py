from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ayomi_website.authentication.models import MyUser

admin.site.register(MyUser, UserAdmin)
