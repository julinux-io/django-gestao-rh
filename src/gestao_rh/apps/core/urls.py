from django.urls import path
from gestao_rh.apps.core import views


urlpatterns = [
    path('', views.home, name='home'),
]
