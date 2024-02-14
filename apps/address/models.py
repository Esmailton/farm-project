from django.db import models
from django.urls import reverse
from apps.core.models import Base
from django.utils.translation import gettext_lazy as _
from django.db.models import UniqueConstraint


class Country(Base, models.Model):
    name = models.CharField(_("Country"), max_length=100, unique=True)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countrys")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class UF(Base, models.Model):
    name = models.CharField(_("State"), unique=True, max_length=50)
    acronym = models.CharField(_("Acronym"), unique=True, max_length=2)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="country_uf",
        verbose_name=_("Country"),
    )

    class Meta:
        verbose_name = _("UF")
        verbose_name_plural = _("UFs")
        ordering = ["-created_at"]
        constraints = [
            UniqueConstraint(
                "name",
                "acronym",
                name="unique_uf_name_acronym",
            ),
        ]

    def __str__(self):
        return f"{self.name}-{self.acronym}"


class City(Base, models.Model):
    name = models.CharField(
        _("City"),
        max_length=255,
    )
    uf = models.ForeignKey(UF, on_delete=models.CASCADE, related_name="uf_city")

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Citys")
        ordering = ["-created_at"]
        constraints = [
            UniqueConstraint(
                "name",
                "uf",
                name="unique_uf_city",
            ),
        ]

    def __str__(self):
        return f"{self.name}-{self.uf.acronym}"


class Address(Base, models.Model):
    logradouro = models.CharField(_("Logradouro"), max_length=150)
    number = models.CharField(_("Number"))
    zipcode = models.CharField(_("Zip Code"), blank=True, null=True, max_length=9)
    neighborhood = models.CharField(_("Neighborhood"), max_length=100)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="address_city"
    )

    def get_absolute_url(self):
        return reverse("address:address_detail", kwargs={"pk": self.id})

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Address")
        ordering = ["-created_at"]

    def __str__(self):
        return self.logradouro
