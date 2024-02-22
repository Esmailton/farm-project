from apps.vehicle.forms import VehicleModelForm
from apps.vehicle.models import VehicleModel
from django.urls import reverse_lazy
from django.views import generic


class VehicleModelListView(generic.ListView):
    template_name = "vehicle_model/vehicle_model_list.html"
    model = VehicleModel
    paginate_by = 30
    queryset = VehicleModel.objects.all()


class VehicleModelDetailView(generic.DetailView):
    template_name = "vehicle_model/vehicle_model_detail.html"
    model = VehicleModel


class VehicleModelCreateView(generic.CreateView):
    template_name = "vehicle_model/vehicle_model_form.html"
    model = VehicleModel
    form_class = VehicleModelForm
    success_url = reverse_lazy("vehicle:vehicle_model_list")


class VehicleModelUpdateView(generic.UpdateView):
    template_name = "vehicle_model/vehicle_model_form.html"
    model = VehicleModel
    form_class = VehicleModelForm
    success_url = reverse_lazy("vehicle:vehicle_model_list")


class VehicleModelDeleteView(generic.DeleteView):
    template_name = "vehicle_model/vehicle_model_confirm_delete.html"
    model = VehicleModel
    success_url = reverse_lazy("vehicle:vehicle_model_list")
