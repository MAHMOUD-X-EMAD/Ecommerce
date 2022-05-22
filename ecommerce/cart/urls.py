from django.urls import re_path
from django.urls import path,include
from django import views
from . import views

app_name = 'cart'

urlpatterns = [
	path('',views.cart_detail,name='cart_detail'),
    path('<int:productid>/',views.cart_add,name='cart_add'),
    path('remove/<int:productid>/',views.cart_remove,name='cart_remove'),
]