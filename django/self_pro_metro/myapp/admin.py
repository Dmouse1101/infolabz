from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(station)
class showStation(admin.ModelAdmin):
    list_display=('id','station_name','station_duration','station_price')
