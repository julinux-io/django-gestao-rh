from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def __str__(self):
        return self.name
