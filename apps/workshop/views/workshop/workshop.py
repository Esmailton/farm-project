from apps.workshop.forms import WorkshopForm
from apps.workshop.models import Workshop
from django.urls import reverse_lazy
from django.views import generic


class WorkshopListView(generic.ListView):
    model = Workshop
    paginate_by = 30
    template_name = "workshop/workshop_list.html"
    queryset = Workshop.objects.all()


class WorkshopDetailView(generic.DetailView):
    template_name = "workshop/workshop_detail.html"
    model = Workshop


class WorkshopCreateView(generic.CreateView):
    model = Workshop
    form_class = WorkshopForm
    template_name = "workshop/workshop_form.html"
    success_url = reverse_lazy("workshop:workshop_list")


class WorkshopUpdateView(generic.UpdateView):
    model = Workshop
    form_class = WorkshopForm
    template_name = "workshop/workshop_form.html"
    success_url = reverse_lazy("workshop:workshop_list")


class WorkshopDeleteView(generic.DeleteView):
    model = Workshop
    template_name = "workshop/workshop_confirm_delete.html"
    success_url = reverse_lazy("workshop:workshop_list")
