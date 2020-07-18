from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import models, serializers
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class DepartmentViewset(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.method == "POST":
            department_serializers = serializers.DepartmentSerializer(data=request.data)
            if department_serializers.is_valid():
                dept_name = department_serializers.validated_data['departmentName']
                company_id = request.company_id
                dept_model = models.Department(departmentName=dept_name, companyId=company_id)
                dept_model.save()
                department_serializers.save()
                return Response(department_serializers.data, status=status.HTTP_201_CREATED)
            return Response(department_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class DesigantionViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    permission_classes = [IsAuthenticated]
