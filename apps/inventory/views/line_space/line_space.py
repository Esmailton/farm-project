from django.views import generic
from django.urls import reverse_lazy
from apps.inventory.forms import LineSpaceForm
from apps.inventory.models import LineSpace

class LineSpaceListView(generic.ListView):
    model = LineSpace
    paginate_by = 10
    queryset = LineSpace.objects.all()
    template_name = 'line_space/line_space_list.html'

class LineSpaceCreateView(generic.CreateView):
    model = LineSpace
    form_class = LineSpaceForm
    success_url = reverse_lazy('inventory:line_space_list')
    queryset = LineSpace.objects.all()
    template_name = 'line_space/line_space_form.html'

class LineSpaceUpdateView(generic.UpdateView):
    model = LineSpace
    form_class = LineSpaceForm
    template_name = 'line_space/line_space_form.html'

class LineSpaceDetailView(generic.DetailView):
    model = LineSpace
    template_name = 'line_space/line_space_detail.html'

class LineSpaceDeleteView(generic.DeleteView):
    model = LineSpace
    success_url = reverse_lazy('line_space:line_space_list')
    template_name = 'line_space/line_space_confirm_delete.html'



