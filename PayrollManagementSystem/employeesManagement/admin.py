from django.contrib import admin
from .models import Employees, Address, BankAccountDetails

# Register your models here.
admin.site.register(Employees)
admin.site.register(Address)
admin.site.register(BankAccountDetails)
