# Generated by Django 3.0.7 on 2020-07-16 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employeesManagement', '0001_initial'),
        ('companyRegistrationAndLoginApplication', '0002_holidays_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='employeeId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='employeesManagement.Employees'),
        ),
        migrations.AddField(
            model_name='holidays',
            name='companyId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='companyRegistrationAndLoginApplication.Companies'),
        ),
    ]