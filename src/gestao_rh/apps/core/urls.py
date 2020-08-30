from django.urls import path
from gestao_rh.apps.core.views import home, CompanyCreate


urlpatterns = [
    path('', home, name='home'),
    path('new/', CompanyCreate.as_view(), name='company-create')
]
