from django.test import TestCase

from gestao_rh.apps.core.models import Company, Department


class CompanyModelTest(TestCase):
    def test_str(self):
        company = Company.objects.create(name='Vespene')
        self.assertEqual('Vespene', str(company))


class DepartmentModelTest(TestCase):
    def setUp(self):
        company = Company.objects.create(name='Vespene')
        self.department = Department.objects.create(name='IT', company=company)

    def test_str(self):
        self.assertEqual('IT', str(self.department))
