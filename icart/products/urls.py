from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.index,name='home'),
    path('product_list/',views.list_products,name='list_product'),
    path('detail_product/<pk>/',views.detail_product,name='product_detail')
]