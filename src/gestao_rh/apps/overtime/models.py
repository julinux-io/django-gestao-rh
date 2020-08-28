from django.db import models


class Overtime(models.Model):
    reason = models.CharField(max_length=80)
    starts = models.DateTimeField()
    ends = models.DateTimeField()

    def __str__(self):
        return self.reason
