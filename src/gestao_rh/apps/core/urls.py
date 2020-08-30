from django.urls import path
from gestao_rh.apps.core.views import (
    home, CompanyCreate, CompanyUpdate
)


urlpatterns = [
    path('', home, name='home'),
    path('new/', CompanyCreate.as_view(), name='company-create'),
    path('update/<int:pk>/', CompanyUpdate.as_view(), name='company-update'),
]
