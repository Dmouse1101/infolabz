from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexpage,name='index'),
    path('fetchcontactus',views.fetchcontactus,name='fetchcontactus')
]
