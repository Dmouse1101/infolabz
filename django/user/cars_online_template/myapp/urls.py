from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexpage,name="index"),
    path('index.html', views.indexpage,name="index"),
    path('about.html', views.aboutpage,name="index"),
    path('contact.html', views.contactpage,name="index"),
    path('new.html', views.newpage,name="index"),
    path('single.html', views.singlepage,name="index"),
    path('specials.html', views.specialpage,name="index"),
    path('404.html', views.fourpage,name="index"),
]
