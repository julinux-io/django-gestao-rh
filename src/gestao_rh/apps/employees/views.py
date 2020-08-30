from django.http import HttpResponse


def get_employees(request):
    return HttpResponse('<h1>Nothing Here</h1>')
