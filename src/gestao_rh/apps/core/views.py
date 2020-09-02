from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Company, Department


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
