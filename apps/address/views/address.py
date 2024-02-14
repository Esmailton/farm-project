from apps.address.forms import AddressForm
from apps.address.models import Address
from django.urls import reverse_lazy
from django.views import generic


class AddressListView(generic.ListView):
    model = Address
    paginate_by = 30
    queryset = Address.objects.all()


class AddressDetailView(generic.DetailView):
    model = Address


class AddressCreateView(generic.CreateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy("address:address_list")


class AddressUpdateView(generic.UpdateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy("address:address_list")


class AddressDeleteView(generic.DeleteView):
    model = Address
    success_url = reverse_lazy("address:address_list")
