from django.db import models


# Create your models here.
class Companies(models.Model):
    companyId = models.CharField(max_length=100, primary_key=True, unique=True)
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


class User(models.Model):
    Admin = 'Admin'
    Employee = 'Employee'
    roleChoices=[(Admin,'Admin'),
                    (Employee,'Employee')
    ]
    userId = models.AutoField(primary_key=True,unique=True)
    userName = models.CharField(max_length=250)
    password  = models.CharField(max_length=250)
    role  = models.CharField(max_length=250, choices=roleChoices,default=Employee)


    def __str__(self):
        return self.userId



class AdminUser(models.Model):
    adminId = models.AutoField(primary_key=True,unique=True)
    companyId =  models.ForeignKey(Companies, on_delete=models.CASCADE)
    adminName = models.CharField(max_length=250)
    Password = models.CharField(max_length=250)
    
    


    def __str__(self):
        return "%s" % (self.adminId)


class Department(models.Model):
    departmentId  = models.CharField(max_length=250,primary_key=True,unique=True)
    departmentName  = models.CharField(max_length=250)

    def __str__(self):
        return self.departmentId


class Designation(models.Model):
    designationId  = models.CharField(max_length=250,primary_key=True,unique=True)
    departmentId  = models.ForeignKey(Department, on_delete=models.CASCADE)
    designationName  = models.CharField(max_length=250)

    def __str__(self):
        return self.designationId

