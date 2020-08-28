from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
