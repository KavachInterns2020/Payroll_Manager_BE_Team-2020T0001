from rest_framework import routers
from companyRegistrationAndLoginApplication.viewset import CompanyViewset
from departmentAndDesignationManagement.views import DesigantionView


router = routers.DefaultRouter()
router.register("companies", CompanyViewset)
#router.register("department", DepartmentViewset)
router.register("designation", DesigantionView)

# https://127.0.0.1:8000/api/companies
# http://127.0.0.1:8000/api/department
# http://127.0.0.1:8000/api/designation
