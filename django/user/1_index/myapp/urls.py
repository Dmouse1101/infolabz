from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexpage,name="index"),
    path('about',views.aboutpage,name="about")
]
