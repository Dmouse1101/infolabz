from django.contrib import admin
from .models import *
# Register your models here.

class display_role(admin.ModelAdmin):
    list_display = ["user_typename"]

admin.site.register(role,display_role)

class display_user_detail(admin.ModelAdmin):
    list_display = ["u_name","display_dp","u_gender","u_email","u_phone","u_type","u_status"]

admin.site.register(user_detail,display_user_detail)

class display_furniture_cat(admin.ModelAdmin):
    list_display = ['id',"cat_name","display_cat_picture","cat_description","cat_added"]
    list_filter = ["cat_name"]
    list_per_page = 1
    list_editable = ['cat_name','cat_description']
    search_fields = ['cat_name']

admin.site.register(furniture_cat,display_furniture_cat)

class display_country(admin.ModelAdmin):
    list_display = ["country_name"]
    search_fields = ['country_name']

admin.site.register(country,display_country)

class display_state(admin.ModelAdmin):
    list_display = ["country_id","state_name"]
    list_filter = ['country_id__country_name','state_name']
    search_fields = ['state_name']

admin.site.register(state,display_state)

class display_city(admin.ModelAdmin):
    list_display = ["state_id","city_name"]
    list_filter = ['state_id__state_name', 'city_name']
    search_fields = ['city_name']

admin.site.register(city,display_city)

class display_user_add(admin.ModelAdmin):
    list_display = ["u_id","build_name","street_name","city_name"]
    list_filter = ['city_name__city_name']
    search_fields = ['u_id']

admin.site.register(user_add,display_user_add)

class display_feedback_details(admin.ModelAdmin):
    list_display = ["f_title","f_description","f_by","f_on"]
    search_fields = ['f_by','f_on']

admin.site.register(feedback_details,display_feedback_details)

class display_complain_details(admin.ModelAdmin):
    list_display = ["c_name","c_detail","display_photo","c_by","c_on"]

admin.site.register(complain_details,display_complain_details)

#  2nd part of Woodsite project

class display_brand_table(admin.ModelAdmin):
    list_display = ["b_name","b_desc","display_photo"]

admin.site.register(brand_table,display_brand_table)

class display_new_furniture(admin.ModelAdmin):
    list_display = ["furniture_name","brand_name","furniture_desc","furniture_price","display_photo","furniture_type","Available_qty"]

admin.site.register(new_furniture,display_new_furniture)

class display_old_furniture(admin.ModelAdmin):
    list_display = ["o_furniture_name","o_brand_name","o_furniture_desc","o_furniture_price","display_photo","o_furniture_type","o_Available_qty"]

admin.site.register(old_furniture,display_old_furniture)

class display_rent_furniture(admin.ModelAdmin):
    list_display = ["r_furniture_name","r_brand_name","r_furniture_desc","r_furniture_price","display_photo","r_furniture_type","r_Available_qty"]

admin.site.register(rent_furniture,display_rent_furniture)

class display_newfurniture_buying(admin.ModelAdmin):
    list_display = ["furniture_id","user_id","booking_datetime"]

admin.site.register(newfurniture_buying,display_newfurniture_buying)

class display_oldfurniture_buying(admin.ModelAdmin):
    list_display = ["o_furniture_id","o_user_id","o_booking_datetime"]

admin.site.register(oldfurniture_buying,display_oldfurniture_buying)

class display_rent_furniture_order(admin.ModelAdmin):
    list_display = ["rent_furniture","rent_userid","rent_sartdate","rent_enddate"]

admin.site.register(rent_furniture_order,display_rent_furniture_order)

