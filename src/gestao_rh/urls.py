"""gestao_rh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from gestao_rh.apps.employees.api.views import EmployeeViewSet
from gestao_rh.apps.overtime.api.views import OvertimeViewSet
from gestao_rh.apps.core.api.views import CompanyViewSet, DepartmentViewSet

router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('overtimes', OvertimeViewSet)
router.register('departments', DepartmentViewSet)
router.register('companies', CompanyViewSet)

urlpatterns = [
    path('', include('gestao_rh.apps.core.urls')),
    path('employments/', include('gestao_rh.apps.employees.urls')),
    path('documents/', include('gestao_rh.apps.documents.urls')),
    path('overtime/', include('gestao_rh.apps.overtime.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
]
