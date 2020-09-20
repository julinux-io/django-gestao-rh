from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from gestao_rh.apps.core.models import Company, Department
from gestao_rh.apps.core.api.serializers import (
    CompanySerializer, DepartmentSerializer
)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
