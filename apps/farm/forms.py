from django.forms import ModelForm
from apps.farm.models import Farm, Department

class FarmForm(ModelForm):
    class Meta:
        model = Farm
        fields = ('name','owner','manager','latitude','longitude','location','size_hc', 'departments',)


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ('department', 'description',)