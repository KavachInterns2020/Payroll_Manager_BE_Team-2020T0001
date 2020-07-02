from rest_framework import viewsets
from . import models, serializers


class CompanyViewset(viewsets.ModelViewSet):
    queryset = models.Companies.objects.all()
    serializer_class = serializers.CompanySerializer
    lookup_field = 'companyId'


class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = 'userId'


class AdminViewset(viewsets.ModelViewSet):
 
    queryset = models.AdminUser.objects.all()
    serializer_class = serializers.AdminSerializer
    lookup_field = 'adminId'


class DepartmentViewset(viewsets.ModelViewSet):
 
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    lookup_field = 'departmentId'

class DesignationViewset(viewsets.ModelViewSet):
 
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    lookup_field = 'adminId'
