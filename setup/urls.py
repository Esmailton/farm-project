from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("", include("apps.address.urls")),
    path("", include("apps.person.urls")),
    path("", include("apps.farm.urls")),
    path("", include("apps.employee.urls")),
    path("", include("apps.workshop.urls")),
    path("", include("apps.vehicle.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
