from django.db import models
from django.urls import reverse


class Overtime(models.Model):
    reason = models.CharField(max_length=80)
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    starts = models.DateTimeField()
    ends = models.DateTimeField()

    @property
    def get_interval(self):
        return self.ends - self.starts

    def get_absolute_url(self):
        return reverse('employees-update', args=[self.employee.id])

    def __str__(self):
        return self.reason
