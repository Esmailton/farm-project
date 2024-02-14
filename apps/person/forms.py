from django.forms import ModelForm
from apps.person.models import Person, Email, Phone

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ('name','document','rg','birth_date','addresses',)

class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ('email','person','type',)

class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = ('phone','person','type',)