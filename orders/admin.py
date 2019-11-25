from django.contrib import admin
from .models import RegularPizza, SicilianPizza, Sub, Pasta, Salad, DinnerPlatter, PizzaTopping, SubTopping, Order
# Register your models here.
admin.site.register(PizzaTopping)
admin.site.register(SubTopping)
#admin.site.register(Order)

@admin.register(RegularPizza, SicilianPizza, Sub, Pasta, Salad, DinnerPlatter)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'status', 'user', 'total_price')