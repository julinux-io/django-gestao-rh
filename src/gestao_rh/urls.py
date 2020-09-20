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
