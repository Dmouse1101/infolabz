from django.contrib import admin
from .models import *
# Register your models here.

class showrole(admin.ModelAdmin):
    list_display = ["user_typename"]
admin.site.register(Role,showrole)

class showuser(admin.ModelAdmin):
    list_display = ["u_name","u_password","u_email","u_type","u_status"]
admin.site.register(user_detail,showuser)

class showbankdetails(admin.ModelAdmin):
    list_display = ["u_id","bank_name","digit_no","end_month","end_year"]
admin.site.register(bank_detail,showbankdetails)

class showcountry(admin.ModelAdmin):
    list_display = ["country_name"]
admin.site.register(country,showcountry)

class showstate(admin.ModelAdmin):
    list_display = ["country_id","state_name"]
admin.site.register(state,showstate)

class showcity(admin.ModelAdmin):
    list_display = ["state_id","city_name"]
admin.site.register(city,showcity)
class showuseraddress(admin.ModelAdmin):
    list_display = ["u_id","building_name","street_name","city","pin_code"]
admin.site.register(user_address,showuseraddress)