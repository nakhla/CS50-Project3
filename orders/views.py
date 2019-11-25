from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.utils.safestring import mark_safe



from .models import RegularPizza, SicilianPizza, Sub, Pasta, Salad, DinnerPlatter, PizzaTopping, SubTopping, Order, CartItem

# Create your views here.
#@login_required(login_url='/login/')
def index(request):
    # if user is not logged in redirect him to login page
    #if not request.user.is_authenticated:
    #    return render(request, "orders/login.html", {"message": None})
    context = {
        "RegularPizza": RegularPizza.objects.all(),
        "SicilianPizza": SicilianPizza.objects.all(),
        "Sub": Sub.objects.all(),
        "DinnerPlatter": DinnerPlatter.objects.all(),
        "Pasta": Pasta.objects.all(),
        "Salad": Salad.objects.all(),
        "PizzaTopping": PizzaTopping.objects.all(),
        "SubTopping": SubTopping.objects.all(),
        "user": request.user,
        'current_Page' : 'Menu'
    }
    return render(request, "orders/index.html", context)

@staff_member_required
def ordersList(request):
    context = {
        "orders": Order.objects.all(),
        'current_Page': 'Orders Dashboard'
    }
    return render(request, "orders/orders.html", context)

@staff_member_required
def orderItems(request, order_id):
    order = Order.objects.filter(pk=order_id).first()
    if order == None:
        #raise Http404("Order does not exist")
        messages.warning(request, f"No orders with that Order ID {order_id}")
        return redirect('ordersList')
    context = {
        "orderitems": CartItem.objects.all().filter(orderID_id=order_id),
        "order": Order.objects.filter(id=order_id),
        "Order_Statuses": Order.STATUS
    }
    return render(request, "orders/order_items.html", context)

@login_required
def myOrders(request):
    context = {
        "orders": Order.objects.filter(user=request.user),
        'current_Page' : 'My Orders'
    }
    return render(request, "orders/myorders.html", context)

@login_required
def myOrderItems(request, order_id):
    order = Order.objects.filter(pk=order_id, user=request.user).first()
    if order == None:
        #raise Http404("Order does not exist")
        messages.warning(request, f"You have No orders with that Order ID {order_id}")
        return redirect('myOrders')
    context = {
        "orderitems": CartItem.objects.all().filter(orderID_id=order_id, orderID__user= request.user),
        "order": Order.objects.filter(id=order_id)
    }
    return render(request, "orders/myorder_items.html", context)

@staff_member_required
def updateOrderStatus(request):
    status = request.POST['status']
    order_id = request.POST['order_id']
    order = Order.objects.get(pk=order_id)
    order.status = status
    order.save()
    messages.success(request, f"Order ID {order_id} has been {order.get_status_display()}")
    return redirect('ordersList')
 



