from rest_framework import serializers
from .models import Companies, AdminUser
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from rest_framework import exceptions

import random
from .sendMail import sendmail


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ["companyName", "companyAddress", "companyEmailAddress", "companyContactNumber",
                  "companyGSTNumber",
                  "companyType", "dateOfRegistration", "timeOfRegistration", "companyWebsite", "companyDetails"
                  ]

    def create(self, validated_data):
        companies = Companies(
            companyName=self.validated_data['companyName'],
            companyAddress=self.validated_data['companyAddress'],
            companyEmailAddress=self.validated_data['companyEmailAddress'],
            companyContactNumber=self.validated_data['companyContactNumber'],
            companyGSTNumber=self.validated_data['companyGSTNumber'],
            companyType=self.validated_data['companyType'],
            companyWebsite=self.validated_data['companyWebsite'],
            companyDetails=self.validated_data['companyDetails']
        )
        companies.save()

        c_name = self.validated_data['companyName'].strip().split()
        admin_id = ""
        for i in c_name:
            admin_id += i[0]
        admin_id += "001"
        pwd = random.randint(100000, 999999)
        admin_model = AdminUser(adminId=admin_id,
                                companyId=Companies.objects.get(companyGSTNumber=self.validated_data['companyGSTNumber']),
                                adminName=self.validated_data['companyName']+"_admin", Password=pwd
                                )

        user =  Users.objects.create_user(username=admin_id, password=pwd, first_name=self.validated_data['companyName']+"_admin")
        user.save()
        # sendmail(to=validated_data["companyEmailAddress"], admin_id=admin_id, password=pwd)
        admin_model.save()
        return companies


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    msg = "User is Not Found"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Wrong Credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must Provide username and Password"
            raise exceptions.ValidationError(msg)
        return data

