from rest_framework import routers
from companyRegistrationAndLoginApplication.viewset import CompanyViewset


router = routers.DefaultRouter()
router.register("companies", CompanyViewset)

# https://127.0.0.1:8000/api/companies
