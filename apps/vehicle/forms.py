from django.forms import ModelForm
from apps.vehicle.models import Vehicle, Brand, Fleet, FleetCategory, VehicleModel


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = (
            "name",
            "type",
            "brand",
            "model",
            "year_of_manufacture",
            "serial_number",
            "plate",
            "hour_meter",
            "mileage",
            "status",
            "farm",
            "color",
            "fleet",
        )


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = (
            "name",
            "description",
        )


class FleetForm(ModelForm):
    class Meta:
        model = Fleet
        fields = (
            "name",
            "description",
        )


class FleetCategoryForm(ModelForm):
    class Meta:
        model = FleetCategory
        fields = (
            "name",
            "description",
        )


class VehicleModelForm(ModelForm):
    class Meta:
        model = VehicleModel
        fields = (
            "name",
            "description",
        )
