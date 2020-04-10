from decimal import Decimal
from django.conf import settings
from planome.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price), 'off_price': str(product.off_price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            if item.get('off_price') and item['off_price'] != 'None':
                print(item)
                item['off_price'] = Decimal(item['off_price'])
                item['total_off_price'] = item['off_price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity']//item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def get_total_off_price(self):
        total_off_price = 0
        for item in self.cart.values():
            if item.get('off_price') and item['off_price'] != 'None':
                total_off_price += (Decimal(item['price']) - Decimal(item['off_price'])) * item['quantity']
        return total_off_price

    def get_total_final_price(self):
        total_price = self.get_total_price()
        total_off_price = self.get_total_off_price()
        return total_price - total_off_price

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
