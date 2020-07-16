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


from employeesManagement.models import Employees


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

    def __str__(self):
        return self.holidayName
