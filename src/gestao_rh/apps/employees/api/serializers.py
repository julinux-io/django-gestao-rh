from rest_framework import serializers
from gestao_rh.apps.employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'job_title', 'user', 'departments',
                  'company', 'on_vacation', 'status')
