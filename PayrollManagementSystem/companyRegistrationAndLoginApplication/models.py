from django.db import models


# Create your models here.
class Companies(models.Model):
    companyId = models.AutoField(primary_key=True, unique=True)
    companyName = models.CharField(max_length=250)
    companyAddress = models.CharField(max_length=250)
    companyEmailAddress = models.EmailField(max_length=250, unique=True)
    companyContactNumber = models.CharField(max_length=10)
    companyGSTNumber = models.CharField(max_length=50, unique=True)
    companyType = models.CharField(max_length=150)
    dateOfRegistration = models.DateField(auto_now=True, auto_created=True)
    timeOfRegistration = models.TimeField(auto_now=True, auto_created=True)
    companyWebsite = models.URLField()
    companyDetails = models.CharField(max_length=500)


class AdminUser(models.Model):
    adminId = models.CharField(max_length=150, primary_key=True, unique=True)
    companyId = models.ForeignKey(Companies, default=None, on_delete=models.CASCADE)
    adminName = models.CharField(max_length=250)
    Password = models.CharField(max_length=250)

    def __str__(self):
        return self.adminId


class Department(models.Model):
    departmentId = models.AutoField(primary_key=True, unique=True)
    companyId = models.ForeignKey(Companies, default=None, on_delete=models.CASCADE)
    departmentName = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.departmentId


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

    def __str__(self):
        return self.employeeId


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


class Review(models.Model):
    employeeId = models.ForeignKey(Employees, default=None, on_delete=models.CASCADE)
    companyId = models.ForeignKey(Companies, default=None, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback = models.CharField(max_length=450)
    date = models.DateField(auto_now=True, auto_created=True)
    time = models.TimeField(auto_now=True, auto_created=True)
    month = models.CharField(max_length=50)
    year = models.IntegerField()


class Holidays(models.Model):
    holidayId = models.AutoField(primary_key=True, unique=True)
    companyId = models.ForeignKey(Companies, default=None, on_delete=models.CASCADE)
    holidayName = models.CharField(max_length=250)
    date = models.DateField()
    day = models.CharField(max_length=150)
    month = models.CharField(max_length=50)
    year = models.IntegerField()


