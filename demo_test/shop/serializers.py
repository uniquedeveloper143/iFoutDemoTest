from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'base_price', 'price']

    def get_price(self, obj):
        return obj.get_price()

class SeasonalProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = SeasonalProduct
        fields = '__all__'

    def get_price(self, obj):
        return obj.get_price()

class BulkProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = BulkProduct
        fields = '__all__'

    def get_price(self, obj):
        return obj.get_price()

class PremiumProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = PremiumProduct
        fields = '__all__'

    def get_price(self, obj):
        return obj.get_price()


# Discount Serializer
class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = '__all__'


class PercentageDiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = PercentageDiscount
        fields = '__all__'


class FixedAmountDiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = FixedAmountDiscount
        fields = '__all__'


class TieredDiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = TieredDiscount
        fields = '__all__'


# Order Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, write_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'order_items', 'discounts', 'total']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        discounts_data = validated_data.pop('discounts', [])

        order = Order.objects.create(**validated_data)

        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)

        if discounts_data:
            order.discounts.set(discounts_data)

        return order

    def get_total(self, obj):
        return obj.calculate_total()
