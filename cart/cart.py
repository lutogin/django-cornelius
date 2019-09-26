from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    def __init__(self, request):
        # Инициализация корзины пользователя
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # Сохраняем корзину пользователя в сессию
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, product: Product, quantity: int = 1, update_quantity: bool = False):
        """Добавляет товара в корзину пользователя или обновляет количества товара."""
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price), 'engraving': False}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def update(self, pid: int, quantity: int = None, engraving: bool = None, price: int = None):
        """Обновляет опции товара в корзине"""
        product = Product.objects.get(id=pid)
        quantity = quantity or self.cart[pid]['quantity']
        engraving = self.cart[pid]['engraving'] if engraving == None else engraving
        price = price or product.price
        # @todo пофиксить изменение цены при выборе гравировки

        self.cart[pid] = {'quantity': quantity, 'price': price, 'engraving': engraving}
        self.save()

    def save(self):
        """Сохраняет данные в сессию"""
        self.session[settings.CART_SESSION_ID] = self.cart
        # Указываем, что сессия изменена
        self.session.modified = True

    def remove(self, product):
        """Удаляет продукт с корзины"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # Итерация по товарам
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # Количество товаров
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Возвращает полную стоимость в корзине"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """Очищает корзину"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_counter_purchases(self):
        """Возвращает количество товара в корзине"""
        return len(self.cart)

    def get_cart_pid(self):
        product_ids = self.cart.keys()
        for pid in product_ids:
            yield pid
