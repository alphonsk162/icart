from django.db import models
from customers.models import Customer
from products.models import Products

# Create your models here.
class order(models.Model):
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='orders',null=True)
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_PROCESSED,"ORDER_PROCESSED"),
                   (ORDER_CONFIRMED,"ORDER_CONFIRMED"),
                   (ORDER_DELIVERED,"ORDER_DELIVERED"))
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
class ordereditem(models.Model):
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,related_name="added_carts",null=True)
    owner=models.ForeignKey(order,on_delete=models.CASCADE,related_name="added_items")
    quantity=models.IntegerField(default=1)
