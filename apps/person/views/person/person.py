from apps.person.forms import PersonForm
from apps.person.models import Person
from django.urls import reverse_lazy
from django.views import generic


class PersonListView(generic.ListView):
    model = Person
    paginate_by = 30
    template_name = "person/person_list.html"
    queryset = Person.objects.all()


class PersonDetailView(generic.DetailView):
    template_name = "person/person_detail.html"
    model = Person


class PersonCreateView(generic.CreateView):
    model = Person
    form_class = PersonForm
    template_name = "person/person_form.html"
    success_url = reverse_lazy("person:person_list")


class PersonUpdateView(generic.UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "person/person_form.html"
    success_url = reverse_lazy("person:person_list")


class PersonDeleteView(generic.DeleteView):
    model = Person
    template_name = "person/person_confirm_delete.html"
    success_url = reverse_lazy("person:person_list")
