from django.views import generic
from django.urls import reverse_lazy
from apps.inventory.forms import ProductInventoryForm
from apps.inventory.models import ProductInventory

class ProductInventoryListView(generic.ListView):
    model = ProductInventory
    paginate_by = 10
    queryset = ProductInventory.objects.all()
    template_name = 'product_inventory/product_inventory_list.html'

class ProductInventoryCreateView(generic.CreateView):
    model = ProductInventory
    form_class = ProductInventoryForm
    success_url = reverse_lazy('business:product_inventory_list')
    queryset = ProductInventory.objects.all()
    template_name = 'product_inventory/product_inventory_form.html'

class ProductInventoryUpdateView(generic.UpdateView):
    model = ProductInventory
    form_class = ProductInventoryForm
    template_name = 'product_inventory/product_inventory_form.html'

class ProductInventoryDetailView(generic.DetailView):
    model = ProductInventory
    template_name = 'product_inventory/product_inventory_detail.html'

class ProductInventoryDeleteView(generic.DeleteView):
    model = ProductInventory
    success_url = reverse_lazy('person:product_inventory_list')
    template_name = 'product_inventory/product_inventory_confirm_delete.html'