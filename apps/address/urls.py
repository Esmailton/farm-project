from django.urls import path
from apps.address.views import address

app_name = "address"

urlpatterns = [
    path("address/list/", address.AddressListView.as_view(), name="address_list"),
    path("address/create/", address.AddressCreateView.as_view(), name="address_create"),
    path(
        "address/<uuid:pk>/update/",
        address.AddressUpdateView.as_view(),
        name="address_update",
    ),
    path(
        "address/<uuid:pk>/delete/",
        address.AddressDeleteView.as_view(),
        name="address_delete",
    ),
    path(
        "address/<uuid:pk>/detail/",
        address.AddressDetailView.as_view(),
        name="address_detail",
    ),
]
