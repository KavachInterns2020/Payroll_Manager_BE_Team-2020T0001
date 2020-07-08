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

    def __str__(self):
        return self.companyName


class AdminUser(models.Model):
    adminId = models.CharField(max_length=150, primary_key=True, unique=True)
    companyId = models.CharField(max_length=100)
    adminName = models.CharField(max_length=250)
    Password = models.CharField(max_length=250)

    def __str__(self):
        return self.adminName
