from django.urls import path
from .views import (
    home, CompanyCreate, CompanyUpdate,
    DepartmentsList
)


urlpatterns = [
    path('', home, name='home'),
    path('companies/new/', CompanyCreate.as_view(), name='company-create'),
    path('companies/update/<int:pk>/', CompanyUpdate.as_view(), name='company-update'),
    path('departments/', DepartmentsList.as_view(), name="departments-list"),
]
