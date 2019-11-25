from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PizzaTopping(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class SubTopping(models.Model):
    name = models.CharField(max_length=64)
    price_s = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_l = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return self.name

class RegularPizza(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    slug = models.SlugField(max_length=64, db_index=True)
    image = models.ImageField(upload_to="images/", blank=True, default=None)
    price_s = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_l = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    toppings_limit = models.IntegerField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = ['id', 'slug']

    def __str__(self):
        return f"{self.name}"

class SicilianPizza(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    slug = models.SlugField(max_length=64, db_index=True)
    image = models.ImageField(upload_to="images/", blank=True, default=None)
    price_s = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_l = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    toppings_limit = models.IntegerField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = ['id', 'slug']

    def __str__(self):
        return f"{self.name}"


class Sub(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    slug = models.SlugField(max_length=64, db_index=True)
    image = models.ImageField(upload_to="images/", blank=True, default=None)
    price_s = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_l = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    topping = models.ManyToManyField(SubTopping, blank=True, related_name="SubToppings")

    class Meta:
        ordering = ('name',)
        index_together = ['id', 'slug']

    def __str__(self):
        return f"{self.name}"

class Pasta(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    slug = models.SlugField(max_length=64, db_index=True)
    image = models.ImageField(upload_to="images/", blank=True, default=None)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('name',)
        index_together = ['id', 'slug']

    def __str__(self):
        return f"{self.name}"


class Salad(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    slug = models.SlugField(max_length=64, db_index=True)
    image = models.ImageField(upload_to="images/", blank=True, default=None)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('name',)
        index_together = ['id', 'slug']

    def __str__(self):
        return f"{self.name}"

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    slug = models.SlugField(max_length=64, db_index=True)
    image = models.ImageField(upload_to="images/", blank=True, default=None)
    price_s = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_l = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        index_together = ['id', 'slug']

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    STATUS = [
        ("P","Pending"),
        ("C","Completed"),
        ("D","Delivered"),
        ("R","Refunded" ),
        ("N","Canceled")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=1, choices=STATUS, default="P")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) # Total Order Price (sum of all items total_price)

    def __str__(self):
        return f"{self.id} by {self.user}"


class CartItem(models.Model):
    item_description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2) #Price of item with toppings (if any ) WITHOUT multiplying by Quantity
    quantity = models.PositiveIntegerField(default=1)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders', blank=True, null=True)
    total_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) #Price * Quantity


    def __str__(self):
        return '{}'.format(self.id)
