from apps.farm.forms import DepartmentForm
from apps.farm.models import Department
from django.urls import reverse_lazy
from django.views import generic

class DepartmentListView(generic.ListView):
    model = Department
    paginate_by = 30
    queryset = Department.objects.all()
    template_name = 'department/department_list.html'

class DepartmentDetailView(generic.DetailView):
    model = Department
    template_name = 'department/department_detail.html'

class DepartmentCreateView(generic.CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'department/department_form.html'
    success_url=reverse_lazy('farm:department_list')

class DepartmentUpdateView(generic.UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'department/department_form.html'
    success_url=reverse_lazy('farm:department_list')

class DepartmentDeleteView(generic.DeleteView):
    model = Department
    template_name = 'department/department_detail.html'
    success_url=reverse_lazy('farm:department_list')