from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView

from gestao_rh.apps.core.models import Company


@login_required
def home(request):
    data = {}
    data['user'] = request.user
    return render(request, 'core/index.html', data)


class CompanyCreate(CreateView):
    model = Company
    fields = ['name']
    success_url = reverse_lazy('home')
