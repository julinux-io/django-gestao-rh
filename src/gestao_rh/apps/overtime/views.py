import csv
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Overtime
from .forms import OvertimeForm


class OvertimeList(ListView):
    model = Overtime

    def get_queryset(self):
        company = self.request.user.employee.company
        return Overtime.objects.filter(employee__company=company)


class OvertimeCreate(CreateView):
    model = Overtime
    form_class = OvertimeForm
    success_url = reverse_lazy('overtime-list')

    def get_form_kwargs(self):
        kwargs = super(OvertimeCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class OvertimeUpdate(UpdateView):
    model = Overtime
    form_class = OvertimeForm

    def get_form_kwargs(self):
        kwargs = super(OvertimeUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class OvertimeDelete(DeleteView):
    model = Overtime
    success_url = reverse_lazy('overtime-list')


class ReportCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=report.csv'

        company = request.user.employee.company

        overtimes = Overtime.objects.filter(employee__company=company)
        writer = csv.writer(response)
        writer.writerow(['reason', 'employee', 'starts', 'ends', 'interval'])
        for overtime in overtimes:
            writer.writerow([overtime.reason, overtime.employee, overtime.starts,
                             overtime.ends, overtime.get_interval])
        return response
