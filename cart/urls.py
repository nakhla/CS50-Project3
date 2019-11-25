from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_to_cart, name='cart_add'),
    path('cart_items/', views.cart_items, name='cart_items'),
    path('cart_actions/', views.cart_actions, name='cart_actions'),
]