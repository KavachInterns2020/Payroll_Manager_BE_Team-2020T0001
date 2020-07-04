from django.contrib import admin
from .models import Companies, AdminUser


# Register your models here.
admin.site.register(Companies)
admin.site.register(AdminUser)

