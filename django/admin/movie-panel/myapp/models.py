from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class movie_category(models.Model):
    category_name = models.CharField(max_length=30)
    def __str__(self):
        return self.category_name

class male_actor(models.Model):
    m_name = models.CharField(max_length=20)
    m_dob = models.DateField()
    m_pic = models.ImageField(upload_to='photo')

    def male_pict(self):
         return mark_safe('<img src="{}" width="100"/>'.format(self.m_pic.url))

    male_pict.allow_tags = True
    def __str__(self):
        return self.m_name

class female_actor(models.Model):
    f_name = models.CharField(max_length=20)
    f_dob = models.DateField()
    f_pic = models.ImageField(upload_to='photo')

    def female_pict(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.f_pic.url))

    female_pict.allow_tags = True
    def __str__(self):
        return self.f_name

class movie(models.Model):
    movie_name = models.CharField(max_length=30)
    movie_decription = models.TextField()
    male_name = models.ForeignKey(male_actor,on_delete=models.CASCADE)
    female_name = models.ForeignKey(female_actor,on_delete=models.CASCADE)
    cat_name = models.ForeignKey(movie_category,on_delete=models.CASCADE)