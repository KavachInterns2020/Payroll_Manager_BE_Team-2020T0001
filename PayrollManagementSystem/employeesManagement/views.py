from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Employees, Address, BankAccountDetails
from .serializers import EmployeesSerializers, AddressSerializers, BankAccountDetailsSerializers
# Create your views here.


class EmployeesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializers(employees, many=True)
        return Response(serializer.data)
