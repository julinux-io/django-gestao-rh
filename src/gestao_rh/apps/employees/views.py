from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from gestao_rh.apps.employees.models import Employee


class EmployeesList(ListView):
    model = Employee

    def get_queryset(self):
        current_company = self.request.user.employee.company
        return Employee.objects.filter(company=current_company)


class EmployeesUpdate(UpdateView):
    model = Employee
    fields = ['name', 'job_title', 'departments',
              'on_vacation', 'status']
    success_url = reverse_lazy('employees-list')


class EmployeesDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employees-list')
