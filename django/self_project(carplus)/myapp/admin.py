from django.contrib import admin
from .models import *
# Register your models here.

class showrole(admin.ModelAdmin):
    list_display = ['user_type']

admin.site.register(role,showrole)


class showuserdetail(admin.ModelAdmin):
    list_display = ['u_name','user_photo','u_gender','u_email','u_phone','u_type','u_status']


admin.site.register(user_detail, showuserdetail)

class showcar_category(admin.ModelAdmin):
    list_display = ['cat_name','cat_photo','cat_desc','cat_date']

admin.site.register(car_category,showcar_category)

class showcountry(admin.ModelAdmin):
    list_display = ['country_name']

admin.site.register(country,showcountry)

class showstate(admin.ModelAdmin):
    list_display = ['country_id','state_name']

admin.site.register(state,showstate)

class showcity(admin.ModelAdmin):
    list_display = ['state_id','city_name']

admin.site.register(city,showcity)

class showuser_address(admin.ModelAdmin):
    list_display = ['u_id','building_name','street_name','city_name','pincode']

admin.site.register(user_address,showuser_address)

class showfeedback(admin.ModelAdmin):
    list_display = ['f_title','f_desc','f_by','f_on']

admin.site.register(feedback_details,showfeedback)

class showcomplain(admin.ModelAdmin):
    list_display = ['c_name','c_detail','complain_photo','c_by','c_on']

admin.site.register(complain_details,showcomplain)


# carplus part 2


class show_company(admin.ModelAdmin):
    list_display = ['comp_name','comp_desc','company_logo']
admin.site.register(company_table,show_company)

class show_newcars(admin.ModelAdmin):
    list_display = ['car_name','comp_name','car_model','showroom_price','milage_info','passenger_capacity','car_type']
admin.site.register(new_cars,show_newcars)

class show_oldcars(admin.ModelAdmin):
    list_display = ['oldcar_name','comp_name','oldcar_modelyear','car_totkm','owner_name','old_category']
admin.site.register(old_cars,show_oldcars)

class show_rentcars(admin.ModelAdmin):
    list_display = ['rent_carname','rent_carcomp','rent_carmodelyear','rent_permonth','terms','car_category']
admin.site.register(rent_cars,show_rentcars)

class show_newcar_book(admin.ModelAdmin):
    list_display = ['car_id','user_id','book_datetime']
admin.site.register(newcar_booking,show_newcar_book)

class show_oldcar_book(admin.ModelAdmin):
    list_display = ['oldcar_id','userbooking_id','oldbooking_datetime']
admin.site.register(oldcar_booking,show_oldcar_book)

class show_rentcar_book(admin.ModelAdmin):
    list_display = ['rent_carid','rent_userid','rent_startdate','rent_enddate','rentbook_datetime']


