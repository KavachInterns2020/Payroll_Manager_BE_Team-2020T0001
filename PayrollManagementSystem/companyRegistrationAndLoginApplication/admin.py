from django.contrib import admin
from .models import Companies, AdminUser

# admin credentials
# username -> admin
# email -> admin@payrollmanager.com
# password -> django

# Register your models here.
admin.site.register(Companies)
admin.site.register(AdminUser)

