from django.views import View
from apps.employee.forms import EmployeeForm
from apps.employee.models import Employee
from django.urls import reverse_lazy
from django.views import generic

class EmployeeListView(generic.ListView):
    model = Employee
    paginate_by = 30
    queryset = Employee.objects.all()

class EmployeeDetailView(generic.DetailView):
    model = Employee

class EmployeeCreateView(generic.CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url=reverse_lazy('employee:employee_list')

class EmployeeUpdateView(generic.UpdateView):
    model = Employee
    form_class = EmployeeForm
    success_url=reverse_lazy('employee:employee_list')

class EmployeeDeleteView(generic.DeleteView):
    model = Employee
    success_url=reverse_lazy('employee:employee_list')