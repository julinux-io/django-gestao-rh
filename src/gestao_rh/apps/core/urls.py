from django.urls import path
from .views import (
    home, CompanyCreate, CompanyUpdate,
    DepartmentsList, DepartmentsCreate,
    DepartmentsUpdate, DepartmentsDelete
)


urlpatterns = [
    path('', home, name='home'),
    path('companies/new/', CompanyCreate.as_view(), name='company-create'),
    path('companies/edit/<int:pk>/', CompanyUpdate.as_view(), name='company-update'),
    path('departments/', DepartmentsList.as_view(), name="departments-list"),
    path('departments/new/', DepartmentsCreate.as_view(), name='departments-create'),
    path('departments/edit/<int:pk>/', DepartmentsUpdate.as_view(), name='departments-update'),
    path('departments/delete/<int:pk>/', DepartmentsDelete.as_view(), name='departments-delete'),
]
