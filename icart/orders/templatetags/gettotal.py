from django import template
register=template.Library()

@register.simple_tag(name='gettotal')
def gettotal(cart):
    s=0
    for cart_item in cart.added_items.all():
        s=s+float(cart_item.quantity)*float(cart_item.product.price)
    return s
        
            