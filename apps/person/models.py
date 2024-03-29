from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import Base
from django.urls import reverse
from django.db.models import UniqueConstraint
from .choices import CONTACT_TYPE
from ..address.models import Address


class Person(Base, models.Model):
    name = models.CharField(_("Full Name"), max_length=200)
    document = models.CharField(
        _("Document CPF/CNPJ"), max_length=14, null=True, blank=True, unique=True
    )
    rg = models.CharField(_("RG"), max_length=30, null=True, blank=True)
    birth_date = models.DateField(_("Birth Date"), null=True, blank=True)
    addresses = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="persons_addresses",
    )

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")
        ordering = ["-created_at"]
        constraints = [
            UniqueConstraint(
                "name",
                "document",
                name="unique_name_document",
            ),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("person:person_detail", kwargs={"pk": self.id})


class Email(Base, models.Model):
    email = models.EmailField(_("E-mail"), blank=True, null=True, unique=True)
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="person_email"
    )
    type = models.CharField(
        _("E-mail Type"), max_length=14, choices=CONTACT_TYPE, default="1"
    )

    class Meta:
        verbose_name = _("E-mail")
        verbose_name_plural = _("E-mails")
        ordering = ["-created_at"]

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("person:email_detail", kwargs={"pk": self.pk})


class Phone(Base, models.Model):
    phone = models.CharField(
        _("Number contact"), max_length=14, blank=True, null=True, unique=True
    )
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="person_phone"
    )
    type = models.CharField(
        _("Phone Type"), max_length=2, choices=CONTACT_TYPE, default="1"
    )

    class Meta:
        verbose_name = _("Phone")
        verbose_name_plural = _("Phones")
        ordering = ["-created_at"]

    def __str__(self):
        return self.phone

    def get_absolute_url(self):
        return reverse("person:phone_detail", kwargs={"pk": self.pk})
