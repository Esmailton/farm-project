from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from apps.farm.models import Farm
from apps.core.models import Base
from django.db.models import UniqueConstraint


class Workshop(Base, models.Model):
    name = models.CharField(_("name"), max_length=50)
    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="farm_workshop",
    )

    class Meta:
        verbose_name = _("Workshop")
        ordering = ["-created_at"]

        constraints = [
            UniqueConstraint(
                "name",
                "farm",
                name="unique_farm_workshop_name",
            ),
        ]

    def get_absolute_url(self):
        return reverse("workshop:workshop_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
