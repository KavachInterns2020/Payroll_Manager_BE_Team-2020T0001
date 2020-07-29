from .models import Employees, Address, BankAccountDetails
from rest_framework.serializers import ModelSerializer


class EmployeesSerializers(ModelSerializer):
    class Meta:
        model = Employees
        fields = [
            'employeeName', 'designation', 'department', 'password', 'companyId',
            'contactNumber', 'emailAddress', 'aadhaarNumber', 'panNumber'
        ]


class AddressSerializers(ModelSerializer):
    employeeId = EmployeesSerializers(many=True, read_only=True)

    class Meta:
        model = Address
        fields = [
            'employeeId', 'companyId', 'houseNumber', 'streetName', 'landmark', 'postalCode', 'city', 'state', 'country'
        ]


class BankAccountDetailsSerializers(ModelSerializer):
    employeeId = EmployeesSerializers(many=True, read_only=True)

    class Meta:
        model = BankAccountDetails
        fields = [
            'employeeId', 'companyId', 'bankName', 'branchName', 'branchAddress', 'ifscCode', 'accountNumber',
            'accountType', 'netBankingId'
        ]
