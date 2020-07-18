from rest_framework import serializers
from .models import Department, Designation
from companyRegistrationAndLoginApplication.models import AdminUser
from django.contrib.auth.models import User


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["departmentName"]

    # def create(self, validated_data):
    #     department = Department(
    #         departmentName=self.validated_data['departmentName'],
    #     )
    #
    #     department.save()
    

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ['designationId', 'companyId', 'departmentId', 'designationName']

    def create(self, validated_data):
        designation = Designation(
            departmentId=self.validated_data['departmentId'],
            designationName=self.validated_data['designationName'],
            companyId=self.validated_data['companyId'],
        )
