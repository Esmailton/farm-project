from django.forms import ModelForm
from apps.workshop.models import Workshop


class WorkshopForm(ModelForm):
    class Meta:
        model = Workshop
        fields = ("name", "farm")
