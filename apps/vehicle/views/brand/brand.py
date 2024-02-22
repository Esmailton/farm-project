from apps.vehicle.forms import BrandForm
from apps.vehicle.models import Brand
from django.urls import reverse_lazy
from django.views import generic


class BrandListView(generic.ListView):
    template_name = "brand/brand_list.html"
    model = Brand
    paginate_by = 30
    queryset = Brand.objects.all()


class BrandDetailView(generic.DetailView):
    template_name = "brand/brand_detail.html"
    model = Brand


class BrandCreateView(generic.CreateView):
    model = Brand
    template_name = "brand/brand_form.html"
    form_class = BrandForm
    success_url = reverse_lazy("vehicle:brand_list")


class BrandUpdateView(generic.UpdateView):
    model = Brand
    template_name = "brand/brand_form.html"
    form_class = BrandForm
    success_url = reverse_lazy("vehicle:brand_list")


class BrandDeleteView(generic.DeleteView):
    model = Brand
    template_name = "brand/brand_confirm_delete.html"
    success_url = reverse_lazy("vehicle:brand_list")
