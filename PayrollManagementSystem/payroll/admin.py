from django.contrib import admin
from .models import Companies


# Register your models here.
admin.site.register(Companies)


admin.site.register(User)

admin.site.register(AdminUser)

admin.site.register(Department)

admin.site.register(Designation)