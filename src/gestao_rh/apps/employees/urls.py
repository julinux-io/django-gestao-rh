from django.urls import path
from .views import (
    EmployeesList, EmployeesUpdate, EmployeesDelete, EmployeesCreate, Pdf
)

urlpatterns = [
    path('', EmployeesList.as_view(), name='employees-list'),
    path('new/', EmployeesCreate.as_view(), name='employees-create'),
    path('edit/<int:pk>/', EmployeesUpdate.as_view(), name='employees-update'),
    path('delete/<int:pk>/', EmployeesDelete.as_view(), name='employees-delete'),
    path('report/', Pdf.as_view(), name='employees-report'),
]
