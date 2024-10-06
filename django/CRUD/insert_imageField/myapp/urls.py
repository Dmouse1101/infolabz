from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage,name='showproduct'),
    path('showproduct',views.addproduct,name='addproduct'),
    path('insertproduct',views.insertproduct,name='insertdetails'),
    path('singleproduct/<int:pid>',views.singleproduct,name='singleproduct')
]
