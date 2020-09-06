from django.forms import ModelForm
from .models import Overtime
from gestao_rh.apps.employees.models import Employee


class OvertimeForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(OvertimeForm, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(
            company=user.employee.company
        )

    class Meta:
        model = Overtime
        fields = ['reason', 'employee', 'starts', 'ends']
