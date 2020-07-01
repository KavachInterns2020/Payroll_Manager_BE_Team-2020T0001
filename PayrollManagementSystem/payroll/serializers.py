from rest_framework import serializers
from .models import Companies


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ["companyId", "companyName", "companyAddress", "companyEmailAddress", "companyContactNumber",
                  "companyGSTNumber",
                  "companyType", "dateOfRegistration", "timeOfRegistration", "companyWebsite", "companyDetails"
                  ]
