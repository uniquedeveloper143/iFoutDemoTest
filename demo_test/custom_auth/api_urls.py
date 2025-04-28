from django.urls import path, include
from rest_framework import routers
from demo_test.custom_auth import api

router = routers.SimpleRouter()
router.register('auth', api.UserAuthViewSet, basename='auth')

app_name = 'custom-auth'

urlpatterns = [
    path('', include(router.urls)),
]
