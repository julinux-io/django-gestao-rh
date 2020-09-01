# Generated by Django 3.1 on 2020-09-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200829_2221'),
        ('employees', '0006_employee_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='departments',
            field=models.ManyToManyField(blank=True, related_name='employee', to='core.Department'),
        ),
    ]