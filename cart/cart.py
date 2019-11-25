from decimal import Decimal
from django.conf import settings
from orders.models import CartItem

class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
            self.cart = cart
        else:
            self.cart = cart
    def add(self, item_description, price, quantity ):
        """
        Create item in DB then add it to Cart session
        """
        item = CartItem.objects.create(item_description=item_description, price=price, quantity=int(quantity), total_price=price * int(quantity))
        item.save()
        self.cart[item.id] = {'id': item.id,
                                'item': item.item_description,
                                'price': str(item.price),
                                'quantity': item.quantity,
                                'total_price' : str(item.total_price) }
        self.save()


    def save(self):
        self.session.modified = True




    def remove(self, item_id):
        item_id = str(item_id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()
            #Remove Item from db
            CartItem.objects.filter(id=item_id).delete()
   
   #used to Empty the cart as it's submitted as an Order
    def remove_all(self): 
        self.cart.clear()
        self.save()
 
    def __iter__(self):
        item_ids = self.cart.keys()
        items = CartItem.objects.filter(id__in=item_ids)
        cart = self.cart.copy()
        for item in items:
            cart[str(item.id)]['item_id'] = item
        for item in cart.values():
            item['item'] = item['item']
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['total_price']
            yield item
            

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def calculate_total_price(self):
        total_price = 0.0
        for cartItem in self.cart:
            total_price += float(self.cart[str(cartItem)]['total_price'])

        return total_price
