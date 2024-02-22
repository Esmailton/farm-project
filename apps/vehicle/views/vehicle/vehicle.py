from apps.vehicle.forms import VehicleForm
from apps.vehicle.models import Vehicle
from django.urls import reverse_lazy
from django.views import generic


class VehicleListView(generic.ListView):
    model = Vehicle
    paginate_by = 30
    queryset = Vehicle.objects.all()


class VehicleDetailView(generic.DetailView):
    model = Vehicle


class VehicleCreateView(generic.CreateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy("vehicle:vehicle_list")


class VehicleUpdateView(generic.UpdateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy("vehicle:vehicle_list")


class VehicleDeleteView(generic.DeleteView):
    model = Vehicle
    success_url = reverse_lazy("vehicle:vehicle_list")
