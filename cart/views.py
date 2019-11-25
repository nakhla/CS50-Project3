from django.shortcuts import render, redirect, get_object_or_404
from orders.models import CartItem, RegularPizza,SicilianPizza,Sub,Pasta,Salad,SubTopping,PizzaTopping,DinnerPlatter, Order
from .cart import Cart
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from datetime import datetime
from django.contrib import messages
from django.utils.safestring import mark_safe

@login_required
def add_to_cart(request):
    # instantiate cart or get it from session
    cart = Cart(request)

    # start preparing cart item details
    quantity = request.POST['quantity']
    item_category = request.POST['item_cat']
    item_id = request.POST['item_id']
   
    if 'size' in request.POST:
        if request.POST['size'] == 'Large':
            item_size = 'Large'
        else:
            item_size = 'Small'
    else:
        item_size = 'Normal'

    if item_category == 'RegularPizza': 
        item = RegularPizza.objects.get(id=item_id)
        item_desc = 'Regular Pizza ' + item.name
        item_desc += '  ' + item_size
        item_price = item.price_l  if item_size == 'Large' else item.price_s
    elif item_category == 'SicilianPizza':
        item = SicilianPizza.objects.get(id=item_id)
        item_desc = 'Sicilian Pizza ' +  item.name
        item_desc += '  ' + item_size
        item_price = item.price_l  if item_size == 'Large' else item.price_s
    elif item_category == 'Sub':
        item = Sub.objects.get(id=item_id)
        item_desc = 'Sub ' + item.name
        item_desc += '  ' + item_size
        item_price = item.price_l  if item_size == 'Large' else item.price_s
    elif item_category == 'DinnerPlatter':
        item = DinnerPlatter.objects.get(id=item_id)
        item_desc = 'Dinner Platter ' + item.name
        item_desc += '  ' + item_size
        item_price = item.price_l  if item_size == 'Large' else item.price_s
    elif item_category == 'Pasta':
        item = Pasta.objects.get(id=item_id)
        item_desc = 'Pasta ' + item.name
        item_price = item.price
    elif item_category == 'Salad':
        item = Salad.objects.get(id=item_id)
        item_desc = 'Salad ' + item.name
        item_price = item.price
    
    
    if 'toppings' in request.POST:
        item_desc += ' Toppings: '
        toppings = request.POST.getlist('toppings')
        if item_category != 'Sub':
            item_desc += ', '.join(toppings)
        else:
            #if item_category == 'Sub':
            for topping in toppings:
                subTopping = SubTopping.objects.get(id=topping)
                item_desc += subTopping.name + ', '
                item_price += (Decimal(subTopping.price_l))  if item_size == 'Large' else (Decimal(subTopping.price_s))
            item_desc = item_desc[:-2] #Remove (trim) last comma and space

    
    cart.add(item_desc, item_price, quantity)
    messages.success(request, mark_safe(f'Added successfully <span class="badge badge-primary">{quantity}</span> {item_desc}'))
    return redirect('index')

@login_required
def cart_actions(request):
    if 'Bulk_Remove' in request.POST:
        remove_from_cart(request)
    elif 'Submit_Order' in request.POST:
        submit_order(request)
        return redirect('myOrders')

    return redirect('cart_items')


def remove_from_cart(request):
    # instantiate cart or get it from session
    cart = Cart(request)
    if 'DeletedID' in request.POST:
        deletedIDs = request.POST.getlist('DeletedID')
        for item_id in deletedIDs:
            cart.remove(item_id)
    #return render(request, "cart/cart_items.html", {'cart':cart})
    return redirect('cart_items')

def submit_order(request):
    # instantiate cart or get it from session
    cart = Cart(request)
    if len(cart.cart) > 0 :
        order = Order.objects.create(user=request.user, created=datetime.now(), modified=datetime.now())
        order.save()
        order_total_price = 0
        for item in cart:
            orderitem = CartItem.objects.get(id=item['id'])
            orderitem.orderID = order
            order_total_price += orderitem.total_price # Total_price of cart item
            orderitem.save()
        order.total_price = order_total_price
        order.save()
        cart.remove_all()
    messages.warning(request, mark_safe(f"Order No. <strong>{order.id}</strong> has been submitted "))
    return redirect('myOrders')

@login_required
def cart_items(request):
    cart = Cart(request)
    context ={
        'current_Page' : 'My Cart' ,
        'cart': cart,
        'cart_total_price': cart.calculate_total_price()
    }
    
    return render(request, "cart/cart_items.html", context)