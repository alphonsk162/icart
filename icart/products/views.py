from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured=Products.objects.order_by('-priority')[:4]
    latest=Products.objects.order_by('-id')[:4]
    context={'featured':featured,'latest':latest}
    return render(request,'index.html',context)
def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('page')
    products_list=Products.objects.order_by('-priority')
    product_paginator=Paginator(products_list,2)
    products_list=product_paginator.get_page(page)
    context={'products':products_list}
    return render(request,'products.html',context)
def detail_product(request,pk):
    product=Products.objects.get(pk=pk)
    context={'product':product}
    return render(request,'product_detail.html',context)
