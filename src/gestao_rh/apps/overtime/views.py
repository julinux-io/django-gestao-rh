from django.urls import reverse_lazy
from django.views.generic import ListView
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
