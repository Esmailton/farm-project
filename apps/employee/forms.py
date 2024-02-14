from django.forms import ModelForm
from apps.employee.models import Employee, Position

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ( 'person', 'department', 'position', 'status', 'farm',)

class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ( 'position', 'description',)