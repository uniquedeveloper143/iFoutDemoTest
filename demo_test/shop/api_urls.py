from django.urls import path, include
from rest_framework import routers
from demo_test.shop import api

router = routers.SimpleRouter()

router.register('products', api.ProductViewSet, basename='products')
router.register('seasonal-products', api.SeasonalProductViewSet, basename='seasonal_products')
router.register('bulk-products', api.BulkProductViewSet, basename='bulk_products')
router.register('premium-products', api.PremiumProductViewSet, basename='premium_products')
router.register('discounts', api.DiscountViewSet, basename='discounts')
router.register('percentage-discounts', api.PercentageDiscountViewSet, basename='percentage_discounts')
router.register('fixed-discounts', api.FixedAmountDiscountViewSet, basename='fixed-discounts')
router.register('tiered-discounts', api.TieredDiscountViewSet, basename='tiered-discounts')
router.register('orders', api.OrderViewSet, basename='orders')

app_name = 'shop'

urlpatterns = [
    path('', include(router.urls)),
]
