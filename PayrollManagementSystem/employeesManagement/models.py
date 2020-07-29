from django.db import models
from companyRegistrationAndLoginApplication.models import Companies
from departmentAndDesignationManagement.models import Department, Designation

# Create your models here.


class Employees(models.Model):
    employeeId = models.CharField(primary_key=True, unique=True, max_length=150)
    employeeName = models.CharField(max_length=200, blank=False)
    designation = models.ForeignKey(Designation, default=None, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, default=None, on_delete=models.CASCADE)
    password = models.CharField(max_length=250)
    companyId = models.ForeignKey(Companies, default=None, on_delete=models.CASCADE)
    contactNumber = models.CharField(max_length=10, unique=True)
    emailAddress = models.EmailField(max_length=250, unique=True)
    aadhaarNumber = models.CharField(max_length=20, unique=True)
    panNumber = models.CharField(max_length=20, unique=True)


class Address(models.Model):
    employeeId = models.ForeignKey(Employees, default=None, on_delete=models.CASCADE)
    companyId = models.ForeignKey(Companies, default=None, on_delete=models.CASCADE)
    houseNumber = models.CharField(max_length=10)
    streetName = models.CharField(max_length=250)
    landmark = models.CharField(max_length=250)
    postalCode = models.CharField(max_length=50)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)


class BankAccountDetails(models.Model):
    employeeId = models.ForeignKey(Employees, default=None, on_delete=models.CASCADE)
    companyId = models.ForeignKey(Companies, default=None, on_delete=models.CASCADE)
    bankName = models.CharField(max_length=250)
    branchName = models.CharField(max_length=250)
    branchAddress = models.CharField(max_length=250)
    ifscCode = models.CharField(max_length=50)
    accountNumber = models.CharField(max_length=100, unique=True, default=None)
    accountType = models.CharField(max_length=200)
    netBankingId = models.CharField(max_length=100, unique=True, default=None)
