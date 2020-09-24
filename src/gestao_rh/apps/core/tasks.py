from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail

from gestao_rh.apps.core.models import Company


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_companies():
    return Company.objects.count()


@shared_task
def send_report():
    total_companies = Company.objects.count()
    result = send_mail(
        'Celery Report',
        f'Total of Companies: {total_companies}',
        'contato@vespene.com.br',
        ['monitoring@vespene.com.br'],
        fail_silently=False
    )
    return result
