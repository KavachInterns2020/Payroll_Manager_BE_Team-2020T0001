from rest_framework import serializers
from .models import Department, Designation, HeadOfDepartment
from companyRegistrationAndLoginApplication.models import AdminUser
from django.contrib.auth.models import User


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["departmentName", 'companyId']
    

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ['companyId', 'designationName', 'departmentId']


class HeadOfDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadOfDepartment
        fields = ['headOfDepartmentName', 'emailAddress', 'contactNumber', 'departmentId']
