# Generated by Django 3.1.1 on 2020-09-20 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_auto_20200901_0447'),
        ('overtime', '0002_overtime_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtime',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='employees.employee'),
        ),
    ]
