from apps.vehicle.forms import FleetCategoryForm
from apps.vehicle.models import FleetCategory
from django.urls import reverse_lazy
from django.views import generic


class FleetCategoryListView(generic.ListView):
    template_name = "fleet_category/fleet_category_list.html"
    model = FleetCategory
    paginate_by = 30
    queryset = FleetCategory.objects.all()


class FleetCategoryDetailView(generic.DetailView):
    template_name = "fleet_category/fleet_category_detail.html"
    model = FleetCategory


class FleetCategoryCreateView(generic.CreateView):
    template_name = "fleet_category/fleet_category_form.html"
    model = FleetCategory
    form_class = FleetCategoryForm
    success_url = reverse_lazy("vehicle:fleet_category_list")


class FleetCategoryUpdateView(generic.UpdateView):
    template_name = "fleet_category/fleet_category_form.html"
    model = FleetCategory
    form_class = FleetCategoryForm
    success_url = reverse_lazy("vehicle:fleet_category_list")


class FleetCategoryDeleteView(generic.DeleteView):
    template_name = "fleet_category/fleet_category_confirm_delete.html"
    model = FleetCategory
    success_url = reverse_lazy("vehicle:fleet_category_list")
