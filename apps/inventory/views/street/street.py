from django.views import generic
from django.urls import reverse_lazy
from apps.inventory.forms import StreetForm
from apps.inventory.models import Street

class StreetListView(generic.ListView):
    model = Street
    paginate_by = 10
    queryset = Street.objects.all()
    template_name = 'street/street_list.html'

class StreetCreateView(generic.CreateView):
    model = Street
    form_class = StreetForm
    success_url = reverse_lazy('inventory:Street_list')
    queryset = Street.objects.all()
    template_name = 'street/street_form.html'

class StreetUpdateView(generic.UpdateView):
    model = Street
    form_class = StreetForm
    template_name = 'street/street_form.html'

class StreetDetailView(generic.DetailView):
    model = Street
    template_name = 'street/street_detail.html'

class StreetDeleteView(generic.DeleteView):
    model = Street
    success_url = reverse_lazy('person:Street_list')
    template_name = 'street/street_confirm_delete.html'