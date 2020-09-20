from rest_framework import serializers

from gestao_rh.apps.core.models import (
    Department, Company
)


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name')


class DepartmentSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'company')
