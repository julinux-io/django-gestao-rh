from rest_framework import viewsets

from gestao_rh.apps.overtime.models import Overtime
from gestao_rh.apps.overtime.api import serializers


class OvertimeViewSet(viewsets.ModelViewSet):
    queryset = Overtime.objects.all()
    serializer_class = serializers.OvertimeSerializer
