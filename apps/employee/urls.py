from django.urls import path
from apps.employee.views.employee import employee
from apps.employee.views.position import position

app_name = 'employee'

urlpatterns = [
    path('employee/list/', employee.EmployeeListView.as_view(), name='employee_list'),
    path('employee/create/', employee.EmployeeCreateView.as_view(), name='employee_create'),    
    path('employee/<uuid:pk>/update/', employee.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<uuid:pk>/delete/', employee.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employee/<uuid:pk>/detail/', employee.EmployeeDetailView.as_view(), name='employee_detail'),
    path('position/list/', position.PositionListView.as_view(), name='position_list'),
    path('position/create/', position.PositionCreateView.as_view(), name='position_create'),    
    path('position/<uuid:pk>/update/', position.PositionUpdateView.as_view(), name='position_update'),
    path('position/<uuid:pk>/delete/', position.PositionDeleteView.as_view(), name='position_delete'),
    path('position/<uuid:pk>/detail/', position.PositionDetailView.as_view(), name='position_detail'),
]