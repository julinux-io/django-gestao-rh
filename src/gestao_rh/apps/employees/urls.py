from django.urls import path
from gestao_rh.apps.employees import views

urlpatterns = [
    path('', views.get_employees, name='employees')
]
