import django
from django.urls import path,include
from django import views
from . import views
from django.views import View
urlpatterns = [
  
  path('',views.m,name="m"),
  path('category/<int:categoryid>/',views.Category,name="Category"),
  path('product/<int:productid>/',views.product,name="Product"),
  

] 
