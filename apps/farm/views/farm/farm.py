from apps.farm.forms import FarmForm
from apps.farm.models import Farm
from django.urls import reverse_lazy
from django.views import generic

class FarmListView(generic.ListView):
    model = Farm
    paginate_by = 30
    queryset = Farm.objects.all()

class FarmDetailView(generic.DetailView):
    model = Farm

class FarmCreateView(generic.CreateView):
    model = Farm
    form_class = FarmForm
    success_url=reverse_lazy('farm:farm_list')

class FarmUpdateView(generic.UpdateView):
    model = Farm
    form_class = FarmForm
    success_url=reverse_lazy('farm:farm_list')

class FarmDeleteView(generic.DeleteView):
    model = Farm
    success_url=reverse_lazy('farm:farm_list')