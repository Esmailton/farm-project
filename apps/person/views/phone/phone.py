from apps.person.forms import PhoneForm
from apps.person.models import Phone
from django.urls import reverse_lazy
from django.views import generic

class PhoneListView(generic.ListView):
    model = Phone
    paginate_by = 30
    template_name = 'phone/phone_list.html'
    queryset = Phone.objects.all()

class PhoneDetailView(generic.DetailView):
    template_name = 'phone/phone_detail.html'
    model = Phone

class PhoneCreateView(generic.CreateView):
    model = Phone
    form_class = PhoneForm
    template_name = 'phone/phone_form.html'
    success_url=reverse_lazy('person:phone_list')

class PhoneUpdateView(generic.UpdateView):
    model = Phone
    form_class = PhoneForm
    template_name = 'phone/phone_form.html'
    success_url=reverse_lazy('person:phone_list')

class PhoneDeleteView(generic.DeleteView):
    model = Phone
    template_name = 'phone/phone_form.html'
    success_url=reverse_lazy('person:phone_list')