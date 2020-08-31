from django.urls import path
from gestao_rh.apps.employees.views import (
    EmployeesList, EmployeesUpdate, EmployeesDelete
)

urlpatterns = [
    path('', EmployeesList.as_view(), name='employees-list'),
    path('edit/<int:pk>/', EmployeesUpdate.as_view(), name='employees-update'),
    path('delete/<int:pk>/', EmployeesDelete.as_view(), name='employees-delete'),
]
