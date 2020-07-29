from django.urls import path
from .views import EmployeesView

urlpatterns = [
    path('emp', EmployeesView.as_view()),
]
