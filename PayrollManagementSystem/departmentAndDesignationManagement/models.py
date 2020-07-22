from django.db import models
from companyRegistrationAndLoginApplication.models import Companies

# Create your models here.


class Department(models.Model):
    departmentId = models.AutoField(primary_key=True, unique=True)
    companyId = models.ForeignKey(Companies, default=None, on_delete=models.CASCADE)
    departmentName = models.CharField(max_length=250, unique=True)


class Designation(models.Model):
    designationId = models.AutoField(primary_key=True, unique=True)
    companyId = models.ForeignKey(Companies, default=None, on_delete=models.CASCADE)
    designationName = models.CharField(max_length=250, unique=True)
    departmentId = models.ForeignKey(Department, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.designationId


class HeadOfDepartment(models.Model):
    headOfDepartmentId = models.AutoField(primary_key=True, unique=True)
    companyId = models.ForeignKey(Companies, default=None, on_delete=models.CASCADE)
    headOfDepartmentName = models.CharField(max_length=250, unique=True)
    emailAddress = models.EmailField(max_length=250, unique=True)
    contactNumber = models.CharField(max_length=10, unique=True)
    departmentId = models.ForeignKey(Department, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.headOfDepartmentId
