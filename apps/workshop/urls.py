from django.urls import path
from apps.workshop.views.workshop import workshop

app_name = "workshop"

urlpatterns = [
    path("workshop/list/", workshop.WorkshopListView.as_view(), name="workshop_list"),
    path(
        "workshop/create/",
        workshop.WorkshopCreateView.as_view(),
        name="workshop_create",
    ),
    path(
        "workshop/<uuid:pk>/update/",
        workshop.WorkshopUpdateView.as_view(),
        name="workshop_update",
    ),
    path(
        "workshop/<uuid:pk>/delete/",
        workshop.WorkshopDeleteView.as_view(),
        name="workshop_delete",
    ),
    path(
        "workshop/<uuid:pk>/detail/",
        workshop.WorkshopDetailView.as_view(),
        name="workshop_detail",
    ),
]
