from rest_framework import serializers
from gestao_rh.apps.overtime.models import Overtime


class OvertimeSerializer(serializers.ModelSerializer):
    employee = serializers.ModelSerializer

    class Meta:
        model = Overtime
        fields = ('id', 'reason', 'employee', 'starts', 'ends', 'get_interval')
