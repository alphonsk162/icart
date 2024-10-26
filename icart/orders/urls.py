from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('orders/',views.cart,name='cart'),
    path('addtocart/',views.add_to_cart,name='addtocart'),
    path('remove/<pk>',views.remove,name='remove')
    
]