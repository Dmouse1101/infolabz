from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
user_typename = (
    ('0','user'),
    ('0','buyer'),
    ('0','rent')
)

gender =(
    ('0','Male'),
    ('1','Female')
)

active = (
    ('0','Active'),
    ('1','Inactive')
)

modelyear = (
    ('2005','2005'),
    ('2006','2006'),
    ('2007','2007'),
    ('2008','2008'),
    ('2009','2009'),
    ('2010','2010'),
    ('2011','2011'),
    ('2012','2012'),
    ('2013','2013'),
    ('2014','2014'),
    ('2015','2015'),
    ('2016','2016'),
    ('2017','2017'),
    ('2018','2018'),
    ('2019','2019'),
    ('2020','2020'),
    ('2021','2021'),
    ('2022','2022')
)
class role(models.Model):
    user_type = models.CharField(max_length=1,choices=user_typename)

    def __str__(self):
        return self.user_type

class user_detail(models.Model):
    u_name = models.CharField(max_length=20)
    u_dp = models.ImageField(upload_to='photos')
    u_gender = models.CharField(max_length=1,choices=gender)
    u_email = models.EmailField()
    u_phone = models.CharField(max_length=10)
    u_type = models.ForeignKey(role,on_delete=models.CASCADE)
    u_status = models.CharField(max_length=1,choices=active)

    def user_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.u_dp.url))

    def __str__(self):
        return self.u_name


class car_category(models.Model):
    cat_name = models.CharField(max_length=20)
    cat_picture = models.ImageField(upload_to='photos')
    cat_desc = models.TextField()
    cat_date = models.DateTimeField(auto_now_add=True)

    def cat_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.cat_picture.url))

    def __str__(self):
        return self.cat_name


class country(models.Model):
    country_name = models.CharField(max_length=20)

    def __str__(self):
        return self.country_name

class state(models.Model):
    country_id = models.ForeignKey(country,on_delete=models.CASCADE)
    state_name = models.CharField(max_length=20)

    def __str__(self):
        return self.state_name

class city(models.Model):
    state_id = models.ForeignKey(state,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=20)

    def __str__(self):
        return self.city_name

class user_address(models.Model):
    u_id = models.ForeignKey(user_detail,models.CASCADE)
    building_name = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    city_name = models.ForeignKey(city,models.CASCADE)
    pincode = models.CharField(max_length=6)

class feedback_details(models.Model):
    f_title = models.CharField(max_length=20)
    f_desc = models.TextField()
    f_by = models.ForeignKey(user_detail,on_delete=models.CASCADE)
    f_on = models.DateTimeField(auto_now_add=True)

class complain_details(models.Model):
    c_name = models.CharField(max_length=20)
    c_detail = models.TextField()
    c_photo = models.ImageField(upload_to='photos')
    c_by = models.ForeignKey(user_detail,on_delete=models.CASCADE)
    c_on = models.DateTimeField(auto_now_add=True)

    def complain_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.c_photo.url))



#  carplus part 2

class company_table(models.Model):
    comp_name = models.CharField(max_length=20)
    comp_desc = models.TextField()
    comp_logo = models.ImageField(upload_to='photos')

    def company_logo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.comp_logo.url))

    def __str__(self):
        return self.comp_name

class new_cars(models.Model):
    car_name = models.CharField(max_length=20)
    comp_name = models.ForeignKey(company_table,on_delete=models.CASCADE)
    car_model = models.CharField(max_length=10)
    showroom_price = models.IntegerField()
    milage_info = models.CharField(max_length=20)
    passenger_capacity = models.CharField(max_length=1)
    car_type = models.ForeignKey(car_category,on_delete=models.CASCADE)

    def __str__(self):
        return self.car_name

class old_cars(models.Model):
    oldcar_name = models.CharField(max_length=20)
    comp_name = models.ForeignKey(company_table, on_delete=models.CASCADE)
    oldcar_modelyear = models.CharField(max_length=4,choices=modelyear)
    car_totkm = models.IntegerField()
    owner_name = models.ForeignKey(user_detail,on_delete=models.CASCADE)
    old_category = models.ForeignKey(car_category,on_delete=models.CASCADE)

    def __str__(self):
        return self.oldcar_name

class rent_cars(models.Model):
    rent_carname = models.CharField(max_length=20)
    rent_carcomp = models.ForeignKey(company_table,on_delete=models.CASCADE)
    rent_carmodelyear = models.CharField(max_length=4,choices=modelyear)
    rent_permonth = models.IntegerField()
    terms = models.TextField()
    car_category = models.ForeignKey(car_category,on_delete=models.CASCADE)

    def __str__(self):
        return self.rent_carname

class newcar_booking(models.Model):
    car_id = models.ForeignKey(new_cars,on_delete=models.CASCADE)
    user_id = models.ForeignKey(user_detail,on_delete=models.CASCADE)
    book_datetime = models.DateTimeField(auto_now_add=True)

class oldcar_booking(models.Model):
    oldcar_id = models.ForeignKey(old_cars,on_delete=models.CASCADE)
    userbooking_id = models.ForeignKey(user_detail,on_delete=models.CASCADE)
    oldbooking_datetime = models.DateTimeField(auto_now_add=True)

class rent_carbooking(models.Model):
    rent_carid = models.ForeignKey(rent_cars,on_delete=models.CASCADE)
    rent_userid = models.ForeignKey(user_detail,on_delete=models.CASCADE)
    rent_startdate = models.DateField()
    rent_enddate = models.DateField()
    rentbook_datetime = models.DateTimeField(auto_now_add=True)