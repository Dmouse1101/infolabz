from django.db import models
from django.utils.safestring import mark_safe
user_role =(
        ("User","user"),
        ("Buyer","buyer"),
        ("Seller","seller"),
        ("Rent","rent")
)

user_gender = (
    ("Male","male"),
    ("Female","female"),
    ("Other","other")
)

user_status = (
    ("0","Active"),
    ("1","Inactive")
)

quantity = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
    ("11","11"),
    ("12","12"),
    ("13","13"),
    ("14","14"),
    ("15","15"),
    ("16","16"),
    ("17","17"),
    ("18","18"),
    ("19","19"),
    ("20","20")
)
# Create your models here.
class role(models.Model):
    user_typename = models.CharField(max_length=10,choices=user_role)

    def __str__(self):
        return self.user_typename

class user_detail(models.Model):
    u_name = models.CharField(max_length=30)
    u_dp = models.ImageField(upload_to='photos')
    u_gender = models.CharField(max_length=6,choices=user_gender)
    u_email = models.EmailField()
    u_phone = models.BigIntegerField()
    u_type = models.ForeignKey(role,on_delete=models.CASCADE)
    u_status = models.CharField(max_length=1,choices=user_status)

    def display_dp(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.u_dp.url))

    def __str__(self):
        return self.u_name

class furniture_cat(models.Model):
    cat_name = models.CharField(max_length=20)
    cat_picture = models.ImageField(upload_to='photos')
    cat_description = models.TextField()
    cat_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name
    def display_cat_picture(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.cat_picture.url))


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

class user_add(models.Model):
    u_id = models.ForeignKey(user_detail,on_delete=models.CASCADE)
    build_name = models.TextField()
    street_name = models.CharField(max_length=20)
    city_name =  models.ForeignKey(city,on_delete=models.CASCADE)

class feedback_details(models.Model):
    f_title = models.CharField(max_length=20)
    f_description = models.TextField()
    f_by = models.ForeignKey(user_detail,on_delete=models.CASCADE)
    f_on = models.DateTimeField(auto_now_add=True)

class complain_details(models.Model):
    c_name = models.CharField(max_length=20)
    c_detail = models.TextField()
    c_photo = models.ImageField(upload_to='photos')
    c_by = models.ForeignKey(user_detail,on_delete=models.CASCADE)
    c_on = models.DateTimeField(auto_now_add=True)

    def display_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.c_photo.url))


#  2nd part of Woodsite project
class brand_table(models.Model):
    b_name = models.CharField(max_length=20)
    b_desc = models.TextField()
    b_logo = models.ImageField(upload_to='photos/brand')

    def __str__(self):
        return self.b_name

    def display_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.b_logo.url))

class new_furniture(models.Model):
    furniture_name = models.CharField(max_length=20)
    brand_name = models.ForeignKey(brand_table,on_delete=models.CASCADE)
    furniture_desc = models.TextField()
    furniture_price = models.FloatField()
    furniture_image = models.ImageField(upload_to='photos/furniture')
    furniture_type = models.ForeignKey(furniture_cat,on_delete=models.CASCADE)
    Available_qty = models.CharField(max_length=20,choices=quantity)

    def display_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.furniture_image.url))

    def __str__(self):
        return self.furniture_name

class old_furniture(models.Model):
    o_furniture_name = models.CharField(max_length=20)
    o_brand_name = models.ForeignKey(brand_table,on_delete=models.CASCADE)
    o_furniture_desc = models.TextField()
    o_furniture_price = models.FloatField()
    o_furniture_image = models.ImageField(upload_to='photos/furniture')
    o_furniture_type = models.ForeignKey(furniture_cat, on_delete=models.CASCADE)
    o_Available_qty = models.CharField(max_length=20, choices=quantity)

    def display_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.o_furniture_image.url))

    def __str__(self):
        return self.o_furniture_name
class rent_furniture(models.Model):
    r_furniture_name = models.CharField(max_length=20)
    r_brand_name = models.ForeignKey(brand_table, on_delete=models.CASCADE)
    r_furniture_desc = models.TextField()
    r_furniture_price = models.FloatField()
    r_furniture_image = models.ImageField(upload_to='photos/furniture')
    r_furniture_type = models.ForeignKey(furniture_cat, on_delete=models.CASCADE)
    r_Available_qty = models.CharField(max_length=20, choices=quantity)

    def display_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.r_furniture_image.url))

    def __str__(self):
        return self.r_furniture_name

class newfurniture_buying(models.Model):
    furniture_id = models.ForeignKey(new_furniture, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user_detail, on_delete=models.CASCADE)
    booking_datetime = models.DateTimeField(auto_now_add=True)

class oldfurniture_buying(models.Model):
    o_furniture_id = models.ForeignKey(old_furniture, on_delete=models.CASCADE)
    o_user_id = models.ForeignKey(user_detail, on_delete=models.CASCADE)
    o_booking_datetime = models.DateTimeField(auto_now_add=True)

class rent_furniture_order(models.Model):
    rent_furniture = models.ForeignKey(rent_furniture,on_delete=models.CASCADE)
    rent_userid = models.ForeignKey(user_detail, on_delete=models.CASCADE)
    rent_sartdate = models.DateField()
    rent_enddate = models.DateField()
