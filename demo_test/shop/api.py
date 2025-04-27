from rest_framework import viewsets
from rest_framework import permissions
from demo_test.utils.permissions import IsAPIKEYAuthenticated
from .models import *
from .serializers import *


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [permissions.IsAuthenticated, IsAPIKEYAuthenticated]

    def get_queryset(self):
        return Product.objects.all().order_by('-id')


class SeasonalProductViewSet(viewsets.ModelViewSet):
    queryset = SeasonalProduct.objects.all()
    serializer_class = SeasonalProductSerializer

    permission_classes = [permissions.IsAuthenticated, IsAPIKEYAuthenticated]

    def get_queryset(self):
        return SeasonalProduct.objects.all().order_by('-id')


class BulkProductViewSet(viewsets.ModelViewSet):
    queryset = BulkProduct.objects.all()
    serializer_class = BulkProductSerializer

    permission_classes = [permissions.IsAuthenticated, IsAPIKEYAuthenticated]

    def get_queryset(self):
        return BulkProduct.objects.all().order_by('-id')


class PremiumProductViewSet(viewsets.ModelViewSet):
    queryset = PremiumProduct.objects.all()
    serializer_class = PremiumProductSerializer

    permission_classes = [permissions.IsAuthenticated, IsAPIKEYAuthenticated]

    def get_queryset(self):
        return PremiumProduct.objects.all().order_by('-id')


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

    permission_classes = [permissions.IsAuthenticated, IsAPIKEYAuthenticated]

    def get_queryset(self):
        return Discount.objects.all().order_by('-id')


class PercentageDiscountViewSet(viewsets.ModelViewSet):
    queryset = PercentageDiscount.objects.all()
    serializer_class = PercentageDiscountSerializer

    permission_classes = [permissions.IsAuthenticated, IsAPIKEYAuthenticated]

    def get_queryset(self):
        return PercentageDiscount.objects.all().order_by('-id')


class FixedAmountDiscountViewSet(viewsets.ModelViewSet):
    queryset = FixedAmountDiscount.objects.all()
    serializer_class = FixedAmountDiscountSerializer

    permission_classes = [permissions.IsAuthenticated, IsAPIKEYAuthenticated]

    def get_queryset(self):
        return FixedAmountDiscount.objects.all().order_by('-id')


class TieredDiscountViewSet(viewsets.ModelViewSet):
    queryset = TieredDiscount.objects.all()
    serializer_class = TieredDiscountSerializer

    permission_classes = [permissions.IsAuthenticated, IsAPIKEYAuthenticated]

    def get_queryset(self):
        return TieredDiscount.objects.all().order_by('-id')


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    permission_classes = [permissions.IsAuthenticated, IsAPIKEYAuthenticated]

    def get_queryset(self):
        return Order.objects.all().order_by('-id')



