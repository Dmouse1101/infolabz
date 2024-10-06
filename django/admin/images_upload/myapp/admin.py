from django.contrib import admin
from .models import book
# Register your models here.
class showbook(admin.ModelAdmin):
    list_display = ["name","title","description","admin_photo","publish_date"]

admin.site.register(book,showbook)