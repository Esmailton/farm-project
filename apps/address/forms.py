from django.forms import ModelForm
from apps.address import models


class CountryForm(ModelForm):
    class Meta:
        model = models.Country
        fields = ('name',)

class UFForm(ModelForm):
    class Meta:
        model = models.UF
        fields = ('name', 'acronym', 'country',)

class CityForm(ModelForm):
    class Meta:
        model = models.City
        fields = ('name', 'uf',)

class AddressForm(ModelForm):
    class Meta:
        model = models.Address
        fields = ('logradouro', 'number', 'zipcode','neighborhood', 'city',)
