from django.views import generic
from django.urls import reverse_lazy
from apps.inventory.forms import ColumnSpaceForm
from apps.inventory.models import ColumnSpace

class ColumnSpaceListView(generic.ListView):
    model = ColumnSpace
    paginate_by = 10
    queryset = ColumnSpace.objects.all()
    template_name = 'column_space/column_space_list.html'

class ColumnSpaceCreateView(generic.CreateView):
    model = ColumnSpace
    form_class = ColumnSpaceForm
    success_url = reverse_lazy('inventory:column_space_list')
    queryset = ColumnSpace.objects.all()
    template_name = 'column_space/column_space_form.html'

class ColumnSpaceUpdateView(generic.UpdateView):
    model = ColumnSpace
    form_class = ColumnSpaceForm
    template_name = 'column_space/column_space_form.html'

class ColumnSpaceDetailView(generic.DetailView):
    model = ColumnSpace
    template_name = 'column_space/column_space_detail.html'

class ColumnSpaceDeleteView(generic.DeleteView):
    model = ColumnSpace
    success_url = reverse_lazy('column_space:column_space_list')
    template_name = 'column_space/column_space_confirm_delete.html'