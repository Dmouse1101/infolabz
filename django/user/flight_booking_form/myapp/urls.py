from django.urls import path
from . import views
urlpatterns = [
    path('',views.indexpage,name='index'),
    path('submited',views.submited,name='submited')
]