from django.views import generic
from django.urls import reverse_lazy
from apps.inventory.forms import ProductForm
from apps.inventory.models import Product

class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10
    queryset = Product.objects.all()
    template_name = 'product/product_list.html'

class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('inventory:product_list')
    queryset = Product.objects.all()
    template_name = 'product/product_form.html'     

class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product/product_detail.html'

class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('person:product_list')
    template_name = 'product/product_confirm_delete.html'