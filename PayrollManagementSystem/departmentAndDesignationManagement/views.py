from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import models, serializers

# Create your views here.

class DepartmentViewset(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = [IsAuthenticated]


class DesigantionViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    permission_classes = [IsAuthenticated]