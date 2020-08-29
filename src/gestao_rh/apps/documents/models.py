from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255)
    owner = models.ForeignKey('employees.Employee',
                              on_delete=models.PROTECT)

    def __str__(self):
        return self.description
