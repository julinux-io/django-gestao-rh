import io
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView
)

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import Employee


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


class EmployeesCreate(CreateView):
    model = Employee
    fields = ['name', 'job_title', 'status']
    success_url = reverse_lazy('employees-list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        user = obj.name.split(' ')
        username = f'{user[0]}.{user[1]}'.lower()
        obj.company = self.request.user.employee.company
        obj.user = User.objects.create(username=username)
        obj.on_vacation = False
        obj.save()
        return super(EmployeesCreate, self).form_valid(form)


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment;filename={filename}.pdf'
            return response
        else:
            return HttpResponse("error rendering PDF", status=400)


class Pdf(View):
    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request
        }
        return Render.render('employees/reports.html', params, 'report')
