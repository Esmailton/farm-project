from django.urls import path
from apps.vehicle.views.vehicle import vehicle
from apps.vehicle.views.brand import brand
from apps.vehicle.views.fleet import fleet
from apps.vehicle.views.fleet_category import fleet_category
from apps.vehicle.views.vehicle_model import vehicle_model


app_name = "vehicle"

urlpatterns = [
    path("vehicle/list/", vehicle.VehicleListView.as_view(), name="vehicle_list"),
    path("vehicle/create/", vehicle.VehicleCreateView.as_view(), name="vehicle_create"),
    path(
        "vehicle/<uuid:pk>/update/",
        vehicle.VehicleUpdateView.as_view(),
        name="vehicle_update",
    ),
    path(
        "vehicle/<uuid:pk>/delete/",
        vehicle.VehicleDeleteView.as_view(),
        name="vehicle_delete",
    ),
    path(
        "vehicle/<uuid:pk>/detail/",
        vehicle.VehicleDetailView.as_view(),
        name="vehicle_detail",
    ),
    path("brand/list/", brand.BrandListView.as_view(), name="brand_list"),
    path("brand/create/", brand.BrandCreateView.as_view(), name="brand_create"),
    path(
        "brand/<uuid:pk>/update/",
        brand.BrandUpdateView.as_view(),
        name="brand_update",
    ),
    path(
        "brand/<uuid:pk>/delete/",
        brand.BrandDeleteView.as_view(),
        name="brand_delete",
    ),
    path(
        "brand/<uuid:pk>/detail/",
        brand.BrandDetailView.as_view(),
        name="brand_detail",
    ),
    path("fleet/list/", fleet.FleetListView.as_view(), name="fleet_list"),
    path("fleet/create/", fleet.FleetCreateView.as_view(), name="fleet_create"),
    path(
        "fleet/<uuid:pk>/update/",
        fleet.FleetUpdateView.as_view(),
        name="fleet_update",
    ),
    path(
        "fleet/<uuid:pk>/delete/",
        fleet.FleetDeleteView.as_view(),
        name="fleet_delete",
    ),
    path(
        "fleet/<uuid:pk>/detail/",
        fleet.FleetDetailView.as_view(),
        name="fleet_detail",
    ),
    path(
        "fleet_category/list/",
        fleet_category.FleetCategoryListView.as_view(),
        name="fleet_category_list",
    ),
    path(
        "fleet_category/create/",
        fleet_category.FleetCategoryCreateView.as_view(),
        name="fleet_category_create",
    ),
    path(
        "fleet_category/<uuid:pk>/update/",
        fleet_category.FleetCategoryUpdateView.as_view(),
        name="fleet_category_update",
    ),
    path(
        "fleet_category/<uuid:pk>/delete/",
        fleet_category.FleetCategoryDeleteView.as_view(),
        name="fleet_category_delete",
    ),
    path(
        "fleet_category/<uuid:pk>/detail/",
        fleet_category.FleetCategoryDetailView.as_view(),
        name="fleet_category_detail",
    ),
    path(
        "vehicle_model/list/",
        vehicle_model.VehicleModelListView.as_view(),
        name="vehicle_model_list",
    ),
    path(
        "vehicle_model/create/",
        vehicle_model.VehicleModelCreateView.as_view(),
        name="vehicle_model_create",
    ),
    path(
        "vehicle_model/<uuid:pk>/update/",
        vehicle_model.VehicleModelUpdateView.as_view(),
        name="vehicle_model_update",
    ),
    path(
        "vehicle_model/<uuid:pk>/delete/",
        vehicle_model.VehicleModelDeleteView.as_view(),
        name="vehicle_model_delete",
    ),
    path(
        "vehicle_model/<uuid:pk>/detail/",
        vehicle_model.VehicleModelDetailView.as_view(),
        name="vehicle_model_detail",
    ),
]
