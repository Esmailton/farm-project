from django.db import models
from django.urls import reverse
from apps.core.models import Base
from django.utils.translation import gettext_lazy as _
from apps.vehicle.choices import (
    VEHICLE_TYPES_CHOICES,
    VEHICLE_STATUS_CHOICES,
    COLOR_CHOICES,
)
from apps.farm.models import Farm


class Brand(Base):
    name = models.CharField(_("Name"), max_length=150)
    description = models.CharField(_("Description"), max_length=255)

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vehicle:brand_detail", kwargs={"pk": self.pk})


class FleetCategory(Base):
    name = models.CharField(_("Name"), max_length=150)
    description = models.CharField(_("Description"), max_length=255)

    class Meta:
        verbose_name = _("Fleet Category")
        verbose_name_plural = _("Fleet Categories")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vehicle:fleet_category_detail", kwargs={"pk": self.pk})


class Fleet(Base):
    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField(_("Description"), blank=True, null=True)
    category = models.OneToOneField(
        FleetCategory,
        verbose_name=_("Category"),
        related_name="fleet",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Fleet")
        verbose_name_plural = _("Fleets")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vehicle:fleet_detail", kwargs={"pk": self.pk})


class VehicleModel(Base):
    name = models.CharField(_("Name"), max_length=150)
    description = models.CharField(_("Description"), max_length=255)

    class Meta:
        verbose_name = _("Vehicle Model")
        verbose_name_plural = _("Vehicle Models")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vehicle:model_detail", kwargs={"pk": self.pk})


class Vehicle(Base):
    name = models.CharField(_("Name"), max_length=150)
    type = models.CharField(_("Type"), choices=VEHICLE_TYPES_CHOICES, max_length=3)
    brand = models.OneToOneField(
        Brand,
        verbose_name=_("Brand"),
        related_name="vehicle",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    model = models.OneToOneField(
        VehicleModel,
        verbose_name=_("Model"),
        related_name="vehicle",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    year_of_manufacture = models.PositiveIntegerField(
        _("Year of Manufacture"), null=True, blank=True
    )
    serial_number = models.CharField(_("Serial Number"), max_length=150)
    plate = models.CharField(_("Plate"), max_length=15)
    hour_meter = models.CharField(_("Hour Meter"), max_length=15, null=True, blank=True)
    mileage = models.CharField(_("Mileage"), max_length=15, null=True, blank=True)
    status = models.CharField(_("Status"), choices=VEHICLE_STATUS_CHOICES, max_length=3)
    farm = models.OneToOneField(
        Farm,
        verbose_name=_("Farm"),
        related_name="vehicle",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    color = models.CharField(_("Color"), choices=COLOR_CHOICES, max_length=3)
    fleet = models.OneToOneField(
        Fleet,
        verbose_name=_("Fleet"),
        related_name="vehicle",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vehicle:vehicle_detail", kwargs={"pk": self.pk})


class MaintenanceHistory(models.Model):
    vehicle = models.ForeignKey(
        Vehicle, verbose_name=_("Vehicle"), on_delete=models.CASCADE
    )
    maintenance_date = models.DateField(_("Maintenance Date"))
    description = models.TextField(_("Description"))
    cost = models.DecimalField(_("Cost"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Maintenance History")
        verbose_name_plural = _("Maintenance Histories")

    def __str__(self):
        return f"{self.vehicle} - {self.maintenance_date}"

    def get_absolute_url(self):
        return reverse("vehicle:maintenance_history_detail", kwargs={"pk": self.pk})
