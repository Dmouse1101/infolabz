from django.urls import path
from .views import *
urlpatterns = [
    path('',showindex,name="index"),
    path('bookmetro',bookmetro,name="bookmetro"),
]