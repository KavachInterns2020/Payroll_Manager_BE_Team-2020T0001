from rest_framework import serializers
from .models import Companies


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ["companyId", "companyName", "companyAddress", "companyEmailAddress", "companyContactNumber",
                  "companyGSTNumber",
                  "companyType", "dateOfRegistration", "timeOfRegistration", "companyWebsite", "companyDetails"
                  ]

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields  = ['userId','userName','password','role'
                    ]
            




class AdminSerializer(serializers.ModelSerializer):

    class Meta :
        model = AdminUser
        fields  = ['adminId','companyId','adminName','Password'
                    ]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Department
        fields = ['departmentId','departmentName']


class DesignationSerializer(serializers.ModelSerializer):
    class Meta :
        model = Designation
        fields = ['designationId','departmentId','designationName']

