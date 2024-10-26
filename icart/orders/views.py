from django.shortcuts import render,redirect
from . models import order,ordereditem 
from products.models import Products
# Create your views here.
def cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=order.objects.get_or_create(
        owner=customer,
        order_status=order.CART_STAGE
    )
    
    context={'cart_obj':cart_obj}

    return render(request,'cart.html',context)

def remove(request,pk):
    user=request.user
    customer=user.customer_profile
    cart_obj=order.objects.get(owner=customer,order_status=order.CART_STAGE)
    item=cart_obj.added_items.get(pk=pk)
    item.delete()
    cart_obj,created=order.objects.get_or_create(
        owner=customer,
        order_status=order.CART_STAGE
    )
    
    context={'cart_obj':cart_obj}

    return render(request,'cart.html',context)
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=request.POST.get('quantity')
        product_id=request.POST.get('product_id')
        cart_obj,created=order.objects.get_or_create(
            owner=customer,
            order_status=order.CART_STAGE
        )
        order_item,created=ordereditem.objects.get_or_create(
            owner=cart_obj,
            product=Products.objects.get(id=product_id)
        )
        if created:
            order_item.quantity=quantity
            order_item.save()
        else:
            order_item.quantity=order_item.quantity+int(quantity)
            order_item.save()
        return redirect('cart')