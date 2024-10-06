from django.db import models

# Create your models here.
user_type = (           #dictionary of tuples
    ("User", "user"),
    ("Seller", "seller"),
    ("Admin", "admin")
)
class Role(models.Model):
    user_typename = models.CharField(max_length=10,choices=user_type)

    def __str__(self):
        return self.user_typename

user_status = (
    ("1","ACTIVE"),
    ("0","INACTIVE")
)
class user_detail(models.Model):
    u_name = models.CharField(max_length=30)
    u_password = models.CharField(max_length=10)
    u_email = models.EmailField()
    u_type = models.ForeignKey(Role,on_delete=models.CASCADE)
    u_status = models.CharField(max_length=1,choices=user_status)

    def __str__(self):
        return self.u_name

month = (
    ("1","1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
)

year = (
    ("2022", "2022"),
    ("2023", "2023"),
    ("2024", "2024"),
    ("2025", "2025"),
    ("2026", "2026"),
    ("2027", "2027"),
    ("2028", "2028"),
    ("2029", "2029"),
    ("2030", "2030"),
)
class bank_detail(models.Model):
    u_id = models.ForeignKey(user_detail,on_delete=models.CASCADE,verbose_name="user id")
    bank_name = models.CharField(max_length=10)
    digit_no = models.CharField(max_length=12,verbose_name="Account no")
    end_month = models.CharField(max_length=2,choices=month)
    end_year = models.CharField(max_length=4,choices=year)

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
    u_id = models.ForeignKey(user_detail, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=50)
    street_name = models.CharField(max_length=30)
    city = models.ForeignKey(city,on_delete=models.CASCADE)
    pin_code = models.CharField(max_length=6)
