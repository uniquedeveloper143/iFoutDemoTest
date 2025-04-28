from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path('api/', include([
        path('custom_auth/', include('demo_test.custom_auth.api_urls')),
        path('shop/', include('demo_test.shop.api_urls')),

    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
