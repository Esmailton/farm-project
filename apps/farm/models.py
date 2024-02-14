from django.db import models
from django.urls import reverse
from apps.core.models import Base
from django.utils.translation import gettext_lazy as _
from apps.person.models import Person
from apps.address.models import Address


class Farm(Base, models.Model):
    name = models.CharField(_("Name"), max_length=150)
    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="farm_owner",
        blank=True,
        null=True,
        verbose_name=_("Owner"),
    )
    manager = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="farm_manager",
        blank=True,
        null=True,
        verbose_name=_("Manager"),
    )
    latitude = models.CharField(_("Longitude"), max_length=100, blank=True, null=True)
    longitude = models.CharField(_("Latitude"), max_length=100, blank=True, null=True)
    location = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        related_name="farm_address",
        blank=True,
        null=True,
        verbose_name=_("Address"),
    )
    size_hc = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_("Size")
    )
    departments = models.ManyToManyField(
        "Department", related_name="departments", verbose_name=_("Department")
    )

    class Meta:
        verbose_name = _("Farm")
        verbose_name_plural = _("Farms")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("farm:farm_detail", kwargs={"pk": self.id})


class Department(Base, models.Model):
    department = models.CharField(_("Department"), max_length=50)
    description = models.TextField(_("Description"))

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")
        ordering = ["-created_at"]

    def __str__(self):
        return self.department

    def get_absolute_url(self):
        return reverse("farm:department_detail", kwargs={"pk": self.id})
