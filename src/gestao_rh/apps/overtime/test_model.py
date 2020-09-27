from django.test import TestCase

from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

from gestao_rh.apps.employees.models import Employee
from gestao_rh.apps.overtime.models import Overtime


class OvertimeModelTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user('testeuser', '123Mudar')
        employee_dict = dict(
            name='User Test', user=user, on_vacation=0, job_title='Developer'
        )
        employee = Employee.objects.create(**employee_dict)
        self.overtime = Overtime.objects.create(
            reason='Coding', employee=employee,
            starts=timezone.now() - timedelta(hours=6), ends=timezone.now()
        )

    def test_str(self):
        self.assertEqual('Coding', str(self.overtime))

    def test_get_interval(self):
        check_interval = self.overtime.ends - self.overtime.starts
        self.assertEqual(check_interval, self.overtime.get_interval)
