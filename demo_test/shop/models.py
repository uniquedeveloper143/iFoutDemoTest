from django.db import models
from django.utils.translation import gettext_lazy as _


# Product models
class Product(models.Model):
    name = models.CharField(_('name'), max_length=128, blank=False, null=False)
    base_price = models.FloatField(_('base price'))

    def get_price(self, quantity=1):
        return self.base_price * quantity

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name

class SeasonalProduct(Product):
    season_discount = models.FloatField(default=0.0)

    def get_price(self, quantity=1):
        price = super().get_price(quantity)
        return price * (1 - self.season_discount / 100)

class BulkProduct(Product):
    def get_price(self, quantity=1):
        price = super().get_price(quantity)
        if 10 <= quantity <= 20:
            price *= 0.95
        elif 21 <= quantity <= 50:
            price *= 0.90
        elif quantity > 50:
            price *= 0.85
        return price

class PremiumProduct(Product):
    markup_percentage = models.FloatField(default=15.0)

    def get_price(self, quantity=1):
        price = super().get_price(quantity)
        return price * (1 + self.markup_percentage / 100)


# Discount models
class Discount(models.Model):
    name = models.CharField(_('name'), max_length=128, blank=False, null=False)
    priority = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def apply_discount(self, price):
        return price

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = _('Discounts')

    def __str__(self):
        return self.name

class PercentageDiscount(Discount):
    percentage = models.FloatField(default=0.0)

    def apply_discount(self, price):
        return price * (1 - self.percentage / 100)

class FixedAmountDiscount(Discount):
    amount = models.FloatField(default=0.0)

    def apply_discount(self, price):
        return max(price - self.amount, 0)


class TieredDiscount(Discount):
    # @staticmethod
    # def default_tiers():
    #     return {500: 5, 1000: 10}

    default_tiers = {500: 5, 1000: 10}
    tiers = models.JSONField(default=default_tiers)

    def apply_discount(self, price):
        discount = 0
        for threshold, percent in sorted(self.tiers.items()):
            if price >= threshold:
                discount = percent
        return price * (1 - discount / 100)

# Order models
class Order(models.Model):
    products = models.ManyToManyField(Product, through='OrderItem')
    discounts = models.ManyToManyField(Discount, blank=True)

    def calculate_total(self):
        subtotal = sum(item.get_total_price() for item in self.order_details.all())
        applicable_discounts = self.discounts.order_by('priority')
        total = subtotal
        for discount in applicable_discounts:
            total = discount.apply_discount(total)
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_details')
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = _('OrderItems')

    def get_total_price(self):
        return self.product.get_price(self.quantity)
