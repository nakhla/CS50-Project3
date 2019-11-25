from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("orders/", views.ordersList, name="ordersList"),
    path("orders/<int:order_id>", views.orderItems, name="orderItems"),
    path("myorders/", views.myOrders, name="myOrders"),
    path("myorders/<int:order_id>", views.myOrderItems, name="myOrderItems"),
    path("updateorderstatus", views.updateOrderStatus, name="updateOrderStatus"),

]
