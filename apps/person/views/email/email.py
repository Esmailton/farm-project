from apps.person.forms import EmailForm
from apps.person.models import Email
from django.urls import reverse_lazy
from django.views import generic

class EmailListView(generic.ListView):
    model = Email
    paginate_by = 30
    template_name = 'email/email_list.html'
    queryset = Email.objects.all()

class EmailDetailView(generic.DetailView):
    model = Email
    template_name = 'email/email_detail.html'

class EmailCreateView(generic.CreateView):
    model = Email
    form_class = EmailForm
    template_name = 'email/email_form.html'

    success_url=reverse_lazy('person:email_list')

class EmailUpdateView(generic.UpdateView):
    model = Email
    form_class = EmailForm
    template_name = 'email/email_form.html'

    success_url=reverse_lazy('person:email_list')

class EmailDeleteView(generic.DeleteView):
    model = Email
    template_name = 'email/email_form.html'
    success_url=reverse_lazy('person:email_list')