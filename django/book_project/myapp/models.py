from django.utils.safestring import mark_safe
from django.db import models

cat_name = (
    ('1','Fiction'),
    ('2','Mythology'),
    ('3','Horror'),
    ('4','study'),
    ('5','UPSC'),
    )

# Create your models here.
class category(models.Model):
    cat_name = models.CharField(max_length=1,choices=cat_name)

    def __str__(self):
        return self.cat_name

class bookinfo(models.Model):
    b_name = models.CharField(max_length=20)
    b_info = models.CharField(max_length=40)
    b_price = models.FloatField()
    b_desc = models.TextField()
    b_pages = models.IntegerField()
    b_image = models.ImageField(upload_to='photos')
    cat_name = models.ForeignKey(category,on_delete=models.CASCADE)

    def book_pic(self):
        return mark_safe('<img src="{}" width="100" height="100"/>'.format(self.b_image.url))

    def __str__(self):
        return self.b_name

gender = (
    ('1','Male'),
    ('2','Female')
)

class author(models.Model):
    a_name = models.CharField(max_length=20)
    a_gender = models.CharField(max_length=1,choices=gender)
    a_email = models.EmailField()
    a_profile_pic = models.ImageField(upload_to='photos')
    a_desc = models.TextField()

    def auth_pic(self):
        return mark_safe('<img src="{}" width="100" height="100"/>'.format(self.a_profile_pic.url))

    def __str__(self):
        return self.a_name


class country(models.Model):
    country_name = models.CharField(max_length=20)
    def __str__(self):
        return self.country_name

class state(models.Model):
    country_name = models.ForeignKey(country,on_delete=models.CASCADE)
    state_name = models.CharField(max_length=20)

    def __str__(self):
        return self.state_name

class city(models.Model):
    state_name = models.ForeignKey(state, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=20)

    def __str__(self):
        return self.city_name