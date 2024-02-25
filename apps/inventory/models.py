from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import Base
from apps.farm.models import Farm
from django.db.models import UniqueConstraint
from django.urls import reverse


class Inventory(Base, models.Model):
    name = models.CharField(_("Name"), max_length=150)
    farm = models.ForeignKey(
        Farm, on_delete=models.CASCADE, related_name="farm_inventory"
    )

    class Meta:
        verbose_name = _("Inventory")
        verbose_name_plural = _("Inventories")
        ordering = ["-created_at"]
        constraints = [
            UniqueConstraint(
                "name",
                name="unique_farm_name",
            ),
        ]

    def get_absolute_url(self):
        return reverse("inventory:inventory_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.name

class Street(Base, models.Model):
    name = models.CharField(_("Name"), max_length=150)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="streets")
    description = models.TextField(_("Description"), max_length=100)

    class Meta:
        verbose_name = _("Street")
        verbose_name_plural = _("Streets")
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("inventory:street_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.name


class Shelf(Base, models.Model):
    name = models.CharField(_("Name"), max_length=150)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name="street")

    class Meta:
        verbose_name = _("Shelf")
        verbose_name_plural = _("Shelfies")
        ordering = ["-created_at"]
        constraints = [
            UniqueConstraint(
                "name",
                "street",
                name="unique_name_street",
            )
        ]

    def get_absolute_url(self):
        return reverse("inventory:shelf_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.name


class LineSpace(Base, models.Model):
    line = models.CharField(_("Line"), max_length=150)
    shelf = models.ForeignKey(
        Shelf, on_delete=models.CASCADE, related_name="line_spaces"
    )

    class Meta:
        verbose_name = _("Line Space")
        verbose_name_plural = _("Line Spaces")
        ordering = ["-created_at"]
        constraints = [
            UniqueConstraint(
                "line",
                "shelf",
                name="unique_shelf_line",
            )
        ]

    def get_absolute_url(self):
        return reverse("inventory:line_space_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.line


class ColumnSpace(Base, models.Model):
    column = models.CharField(_("Column"), max_length=150)
    shelf = models.ForeignKey(
        Shelf, on_delete=models.CASCADE, related_name="column_spaces"
    )

    class Meta:
        verbose_name = _("Column Space")
        verbose_name_plural = _("Column Spaces")
        ordering = ["-created_at"]
        constraints = [
            UniqueConstraint(
                "column",
                "shelf",
                name="unique_shelf_column",
            )
        ]

    def get_absolute_url(self):
        return reverse("inventory:column_space_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.column

class Category(Base, models.Model):
    name = models.CharField(_("Name"), max_length=100)
    description = models.CharField(_("Description"), max_length=100)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["-created_at"]
        constraints = [
            UniqueConstraint(
                "name",
                name="unique_name_category",
            )
        ]

    def get_absolute_url(self):
        return reverse("inventory:category_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.name


class MeasureType(Base, models.Model):
    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField(blank=True, null=True)
    acronym = models.CharField(_("acronym"), max_length=4)
    measure_type = models.CharField(
        _("Measure Type"), max_length=100, blank=True, null=True
    )

    class Meta:
        verbose_name = _("Measure Type")
        verbose_name_plural = _("Measures Types")
        ordering = ["-created_at"]
        constraints = [
            UniqueConstraint(
                "name",
                "acronym",
                name="unique_name_acronym_measure_type",
            )
        ]

    def get_absolute_url(self):
        return reverse("inventory:measure_type_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.name


class Product(Base, models.Model):
    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField(_("Description"), blank=True, null=True)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    picture = models.ImageField(
        _("Picture"), upload_to="img/thumb/%Y/%m/%d", blank=True, null=True
    )
    bar_code = models.CharField(_("Bar Code"), max_length=255, null=True, blank=True)
    qr_code = models.CharField(_("Qr Code"), max_length=255, null=True, blank=True)
    internal_code = models.CharField(
        _("Internal Code"), max_length=255, null=True, blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="product_category",
    )
    measuretype = models.ForeignKey(
        MeasureType,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="product_measure",
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["-created_at"]
        constraints = [
            UniqueConstraint(
                "name",
                "category",
                name="unique_product_category_name",
            ),
            models.CheckConstraint(
                check=models.Q(price__gte=0), name="positive_price_constraint_product"
            ),
        ]

    def get_absolute_url(self):
        return reverse("inventory:product_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.name


class ProductInventory(Base, models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="product_inventory",
    )
    street = models.ForeignKey(
        Street,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="product_street",
    )
    
    shelf = models.ForeignKey(
        Shelf,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="product_shelf",
    )
    line_space = models.ForeignKey(
        LineSpace,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="product_line_space",
    )
    column_space = models.ForeignKey(
        ColumnSpace,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="product_column_space",
    )
    quantity = models.DecimalField(_("Quantity"), max_digits=10, decimal_places=2)
    reorder_point = models.PositiveIntegerField(_("Reorder Point"), default=10)

    class Meta:
        verbose_name = _("Product inventory")
        verbose_name_plural = _("Products inventory")
        ordering = ["-created_at"]
        constraints = [
            UniqueConstraint(
                "product",
                "street",
                "shelf",
                "line_space",
                "column_space",
                name="unique_product_location_constraint",
            ),
            models.CheckConstraint(
                check=models.Q(quantity__gte=0),
                name="positive_quantity_constraint_product",
            ),
        ]

    def get_absolute_url(self):
        return reverse("inventory:product_inventory_detail", kwargs={"pk": self.id})

    def __str__(self):
        return f"{self.product} - {self.quantity}"
