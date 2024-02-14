from django.db import models
from django.urls import reverse
from apps.person.models import Person
from django.utils.translation import gettext_lazy as _
from apps.core.models import Base
from apps.farm.models import Department
from apps.employee.choices import EMPLOYEE_STATUS_TYPE
from apps.farm.models import Farm


class Position(Base, models.Model):
    position = models.CharField(_("Position"), max_length=50, unique=True)
    description = models.CharField(_("Description"), max_length=200)

    class Meta:
        verbose_name = _("Position")
        verbose_name_plural = _("Positions")
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("employee:position_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.position


class Employee(Base, models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name="employee_person",
        verbose_name=_("Person"),
    )
    department = models.OneToOneField(
        Department,
        on_delete=models.CASCADE,
        related_name="department_employee",
        verbose_name=_("Department"),
    )
    position = models.OneToOneField(
        Position,
        on_delete=models.CASCADE,
        related_name="position_employee",
        verbose_name=_("Position"),
    )
    status = models.CharField(_("Status"), choices=EMPLOYEE_STATUS_TYPE, max_length=3)
    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        related_name="farm_employee",
        verbose_name=_("Farm"),
    )

    def get_absolute_url(self):
        return reverse("employee:employee_detail", kwargs={"pk": self.id})

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.person.name}"
