from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Company, Department

from .tasks import send_report


def celery(request):
    send_report.delay()
    return HttpResponse('Task added to queue')


@login_required
def home(request):
    data = {'user': request.user}
    return render(request, 'core/index.html', data)


class CompanyCreate(CreateView):
    model = Company
    fields = ['name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save()
        employee = self.request.user.employee
        employee.company = obj
        employee.save()
        return super().form_valid(form)


class CompanyUpdate(UpdateView):
    model = Company
    fields = ['name']
    success_url = reverse_lazy('home')


class DepartmentsList(ListView):
    model = Department

    def get_queryset(self):
        company = self.request.user.employee.company
        return Department.objects.filter(company=company)


class DepartmentsCreate(CreateView):
    model = Department
    fields = ['name']
    success_url = reverse_lazy('departments-list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user.employee.company
        obj.save()
        return super(DepartmentsCreate, self).form_valid(form)


class DepartmentsUpdate(UpdateView):
    model = Department
    fields = ['name']
    success_url = reverse_lazy('departments-list')


class DepartmentsDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('departments-list')
