from rest_framework import viewsets

from gestao_rh.apps.employees.models import Employee
from gestao_rh.apps.employees.api.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
