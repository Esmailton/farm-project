from django.views import View
from apps.employee.forms import PositionForm
from apps.employee.models import Position
from django.urls import reverse_lazy
from django.views import generic

class PositionListView(generic.ListView):
    model = Position
    paginate_by = 30
    queryset = Position.objects.all()
    template_name = 'position/position_list.html'

class PositionDetailView(generic.DetailView):
    model = Position
    template_name = 'position/position_detail.html'

class PositionCreateView(generic.CreateView):
    model = Position
    form_class = PositionForm
    success_url=reverse_lazy('employee:position_list')
    template_name = 'position/position_form.html'

class PositionUpdateView(generic.UpdateView):
    model = Position
    form_class = PositionForm
    success_url=reverse_lazy('employee:position_list')
    template_name = 'position/position_form.html'

class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url=reverse_lazy('employee:position_list')
    template_name = 'position/position_list.html'