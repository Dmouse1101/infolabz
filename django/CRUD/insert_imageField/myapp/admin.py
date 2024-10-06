from django.contrib import admin
from .models import insertproductdata
# Register your models here.
class showproduct(admin.ModelAdmin):
    list_display = ['id','pname','pprice','pdesc','product_photo']

admin.site.register(insertproductdata,showproduct)