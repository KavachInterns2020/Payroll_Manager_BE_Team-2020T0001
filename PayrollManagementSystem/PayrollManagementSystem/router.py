from rest_framework import routers
from payroll.viewset import CompanyViewset


router = routers.DefaultRouter()
router.register("companies", CompanyViewset)

# https://127.0.0.1:8000/api/companies


router.register("user",UserViewset)

# http://127.0.0.1:8000/api/user/

router.register("admin",AdminViewset)

# http://127.0.0.1:8000/api/admin/


router.register("department",DepartmentViewset)

# http://127.0.0.1:8000/api/department/

router.register("designation",DesignationViewset)

# http://127.0.0.1:8000/api/designation