from django.views import generic
from django.urls import reverse_lazy
from apps.inventory.forms import ShelfForm
from apps.inventory.models import Shelf

class ShelfListView(generic.ListView):
    model = Shelf
    paginate_by = 10
    queryset = Shelf.objects.all()
    template_name = 'shelf/shelf_list.html'

class ShelfCreateView(generic.CreateView):
    model = Shelf
    form_class = ShelfForm
    success_url = reverse_lazy('inventory:shelf_list')
    queryset = Shelf.objects.all()
    template_name = 'shelf/shelf_form.html'

class ShelfUpdateView(generic.UpdateView):
    model = Shelf
    form_class = ShelfForm
    template_name = 'shelf/shelf_form.html'

class ShelfDetailView(generic.DetailView):
    model = Shelf
    template_name = 'shelf/shelf_detail.html'

class ShelfDeleteView(generic.DeleteView):
    model = Shelf
    success_url = reverse_lazy('person:shelf_list')
    template_name = 'shelf/shelf_confirm_delete.html'