from django.test import TestCase

from django.contrib.auth import get_user_model

from gestao_rh.apps.employees.models import Employee


class EmployeeModelTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user('testuser', '123Mudar')
        employee_dict = {
            'name': 'User Test',
            'user': user,
            'job_title': 'Developer',
            'on_vacation': 0,
        }

        self.employee = Employee.objects.create(**employee_dict)

    def test_str(self):
        self.assertEqual('User Test', str(self.employee))
