from django.urls import path
from apps.person.views.person import person
from apps.person.views.email import email
from apps.person.views.phone import phone

app_name = 'person'

urlpatterns = [
    path('person/list/', person.PersonListView.as_view(), name='person_list'),
    path('person/create/', person.PersonCreateView.as_view(), name='person_create'),    
    path('person/<uuid:pk>/update/', person.PersonUpdateView.as_view(), name='person_update'),
    path('person/<uuid:pk>/delete/', person.PersonDeleteView.as_view(), name='person_delete'),
    path('person/<uuid:pk>/detail/', person.PersonDetailView.as_view(), name='person_detail'),
    path('email/list/', email.EmailListView.as_view(), name='email_list'),
    path('email/create/', email.EmailCreateView.as_view(), name='email_create'),    
    path('email/<uuid:pk>/update/', email.EmailUpdateView.as_view(), name='email_update'),
    path('email/<uuid:pk>/delete/', email.EmailDeleteView.as_view(), name='email_delete'),
    path('email/<uuid:pk>/detail/', email.EmailDetailView.as_view(), name='email_detail'),
    path('phone/list/', phone.PhoneListView.as_view(), name='phone_list'),
    path('phone/create/', phone.PhoneCreateView.as_view(), name='phone_create'),    
    path('phone/<uuid:pk>/update/', phone.PhoneUpdateView.as_view(), name='phone_update'),
    path('phone/<uuid:pk>/delete/', phone.PhoneDeleteView.as_view(), name='phone_delete'),
    path('phone/<uuid:pk>/detail/', phone.PhoneDetailView.as_view(), name='phone_detail'),
]