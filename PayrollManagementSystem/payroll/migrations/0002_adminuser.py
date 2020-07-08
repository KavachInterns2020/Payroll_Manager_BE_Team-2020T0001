# Generated by Django 3.0.7 on 2020-07-08 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('adminId', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
                ('adminName', models.CharField(max_length=250)),
                ('Password', models.CharField(max_length=250)),
                ('companyId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='payroll.Companies')),
            ],
        ),
    ]
