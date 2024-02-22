from django.urls import path
from apps.farm.views.farm import farm
from apps.farm.views.department import department

app_name = "farm"

urlpatterns = [
    path("farm/list/", farm.FarmListView.as_view(), name="farm_list"),
    path("farm/create/", farm.FarmCreateView.as_view(), name="farm_create"),
    path("farm/<uuid:pk>/update/", farm.FarmUpdateView.as_view(), name="farm_update"),
    path("farm/<uuid:pk>/delete/", farm.FarmDeleteView.as_view(), name="farm_delete"),
    path("farm/<uuid:pk>/detail/", farm.FarmDetailView.as_view(), name="farm_detail"),
    path(
        "department/list/",
        department.DepartmentListView.as_view(),
        name="department_list",
    ),
    path(
        "department/create/",
        department.DepartmentCreateView.as_view(),
        name="department_create",
    ),
    path(
        "department/<uuid:pk>/update/",
        department.DepartmentUpdateView.as_view(),
        name="department_update",
    ),
    path(
        "department/<uuid:pk>/delete/",
        department.DepartmentDeleteView.as_view(),
        name="department_delete",
    ),
    path(
        "department/<uuid:pk>/detail/",
        department.DepartmentDetailView.as_view(),
        name="department_detail",
    ),
]
