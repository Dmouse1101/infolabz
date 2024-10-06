from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage,name="index"),
    path('first',views.firstpage,name="first_page"),
    path('second',views.secondpage,name="second_page"),
    path('third', views.thirdpage, name="third"),
    path('fourth',views.fourthpage,name="fourth"),
    path('fifth',views.fifthpage,name="fifth"),
]
