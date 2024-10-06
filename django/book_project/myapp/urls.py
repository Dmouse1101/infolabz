from django.urls import path
from . import views
urlpatterns = [
    path('',views.indexpage,name='home'),
    path('book',views.bookspage,name='book'),
    path('purchase',views.purchasepage,name='purchase')
]