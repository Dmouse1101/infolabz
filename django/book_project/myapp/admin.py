from django.contrib import admin

# Register your models here.
from .models import *

class show_category(admin.ModelAdmin):
    list_display = ['cat_name']
admin.site.register(category,show_category)

class show_bookinfo(admin.ModelAdmin):
    list_display = ['b_name','b_info','b_price','b_desc','b_pages','book_pic']
admin.site.register(bookinfo,show_bookinfo)

class show_author(admin.ModelAdmin):
    list_display = ['a_name','a_gender','a_email','auth_pic','a_desc']
admin.site.register(author,show_author)

class show_country(admin.ModelAdmin):
    list_display = ['country_name']
admin.site.register(country,show_country)

class show_state(admin.ModelAdmin):
    list_display = ['country_name','state_name']
admin.site.register(state,show_state)

class show_city(admin.ModelAdmin):
    list_display = ['state_name','city_name']
admin.site.register(city,show_city)