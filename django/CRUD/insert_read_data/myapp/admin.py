from django.contrib import admin
from .models import *
# Register your models here.

class showproduct(admin.ModelAdmin):
    list_display = ['propname','proprice','prodesc','product_image']
admin.site.register(productdetails,showproduct)