from django.contrib import admin
from .models import category, product
# Register your models here.
class showcategory(admin.ModelAdmin):
    list_display = ["name"]
admin.site.register(category,showcategory)

class showproduct(admin.ModelAdmin):
    list_display = ["name","price","description","quantity","productcategory"]
admin.site.register(product,showproduct)