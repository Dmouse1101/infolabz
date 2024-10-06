from django.contrib import admin
from .models import *
# Register your models here.
class displayMovieCategory(admin.ModelAdmin):
    list_display = ['category_name']

admin.site.register(movie_category,displayMovieCategory)


class displayMaleActor(admin.ModelAdmin):
    list_display = ['m_name','m_dob','male_pict']

admin.site.register(male_actor, displayMaleActor)

class displayFemaleActor(admin.ModelAdmin):
    list_display = ['f_name','f_dob','female_pict']

admin.site.register(female_actor, displayFemaleActor)

class displayMovie(admin.ModelAdmin):
    list_display = ['movie_name','movie_decription','male_name','female_name','cat_name']

admin.site.register(movie, displayMovie)