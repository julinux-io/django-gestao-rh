from django.db import models
from django.urls import reverse


class Document(models.Model):
    description = models.CharField(max_length=255)
    filename = models.FileField(upload_to='documents')
    owner = models.ForeignKey('employees.Employee',
                              on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('employees-update', args=[self.owner.id])

    def __str__(self):
        return self.description
