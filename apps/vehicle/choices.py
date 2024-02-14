from django.utils.translation import gettext_lazy as _

VEHICLE_TYPES_CHOICES = [
    ("1", _("Tractor")),
    ("2", _("Harvester")),
    ("3", _("Truck")),
    ("4", _("Car")),
    ("5", _("Agricultural Implement")),
    ("6", _("Agricultural Machine")),
    ("0", _("Other")),
]


VEHICLE_STATUS_CHOICES = [
    ("1", _("Operational")),
    ("2", _("Under Maintenance")),
    ("3", _("Awaiting Parts")),
    ("4", _("Out of Service")),
    ("5", _("Active")),
    ("6", _("Inactive")),
    ("7", _("In Maintenance")),
    ("0", _("Other")),
]


COLOR_CHOICES = [
    ("1", _("Black")),
    ("2", _("White")),
    ("3", _("Silver")),
    ("4", _("Gray")),
    ("5", _("Red")),
    ("6", _("Blue")),
    ("7", _("Green")),
    ("8", _("Yellow")),
    ("9", _("Orange")),
    ("10", _("Purple")),
    ("11", _("Brown")),
    ("12", _("Pink")),
    ("13", _("Beige")),
    ("14", _("Gold")),
    ("15", _("Other")),
]
