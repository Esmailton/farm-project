from apps.vehicle.forms import FleetForm
from apps.vehicle.models import Fleet
from django.urls import reverse_lazy
from django.views import generic


class FleetListView(generic.ListView):
    template_name = "fleet/fleet_list.html"
    model = Fleet
    paginate_by = 30
    queryset = Fleet.objects.all()


class FleetDetailView(generic.DetailView):
    template_name = "fleet/fleet_detail.html"
    model = Fleet


class FleetCreateView(generic.CreateView):
    template_name = "fleet/fleet_form.html"
    model = Fleet
    form_class = FleetForm
    success_url = reverse_lazy("vehicle:fleet_list")


class FleetUpdateView(generic.UpdateView):
    template_name = "fleet/fleet_form.html"
    model = Fleet
    form_class = FleetForm
    success_url = reverse_lazy("vehicle:fleet_list")


class FleetDeleteView(generic.DeleteView):
    template_name = "fleet/fleet_form.html"
    model = Fleet
    success_url = reverse_lazy("vehicle:fleet_list")
