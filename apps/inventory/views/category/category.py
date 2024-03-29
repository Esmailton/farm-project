from django.views import generic
from django.urls import reverse_lazy
from apps.inventory.forms import CategoryForm
from apps.inventory.models import Category

class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 10
    queryset = Category.objects.all()
    template_name = 'category/category_list.html'

class CategoryCreateView(generic.CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('inventory:category_list')
    queryset = Category.objects.all()
    template_name = 'category/category_form.html'

class CategoryUpdateView(generic.UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'category/category_detail.html'

class CategoryDeleteView(generic.DeleteView):
    model = Category
    success_url = reverse_lazy('person:category_list')
    template_name = 'category/category_confirm_delete.html'