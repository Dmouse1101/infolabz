from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexpage,name='index'),
    path('index.html',views.indexpage,name='index'),
    path('about.html', views.aboutpage,name='about'),
    path('services.html', views.servicepage,name='service'),
    path('blog.html', views.blogpage,name='blog'),
    path('blog-single.html', views.single_blogpage,name='single-blog'),
    path('error.html', views.errorpage,name='error'),
    path('elements.html', views.elementpage,name='element'),
    path('contact.html', views.contactpage,name='contact'),
    path('login.html', views.loginpage,name='login'),
    path('loginuser', views.loginuser,name='luser'),
    path('logoutuser', views.logoutuser,name='logoutuser'),
    path('registeruser', views.registeruser,name='registeruser'),
    path('registerpage', views.registerpage,name='registerpage'),
]