from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(Login)
class loginuser(admin.ModelAdmin):
    list_display = ['id','firstname','lastname','email','phone','password','role','added_on']
    search_fields = ['firstname','lastname','email']

@admin.register(UserDetail)
class registeruser(admin.ModelAdmin):
    list_display = ['uid','dob','address','user_photo']
