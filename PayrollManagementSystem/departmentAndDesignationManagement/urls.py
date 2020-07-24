from django.urls import path, include
from .views import DepartmentView, DepartmentdetailView

urlpatterns = [
    path('dept/', DepartmentView.as_view()),
    path('dept/<int:id>/', DepartmentdetailView.as_view()),
    
]
