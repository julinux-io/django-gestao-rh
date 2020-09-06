from django.views.generic import ListView
from .models import Overtime


class OvertimeList(ListView):
    model = Overtime

    def get_queryset(self):
        company = self.request.user.employee.company
        return Overtime.objects.filter(employee__company=company)
