from django.urls import path, include
from .views import DepartmentView, DepartmentdetailView, HeadOfDepartmentView, HeadOfDepartmentDetailView
from . views import DesigantionView, DesignationDetailView

urlpatterns = [
    path('dept/', DepartmentView.as_view()),
    path('dept/<int:id>/', DepartmentdetailView.as_view()),
    path("hod/", HeadOfDepartmentView.as_view()),
    path("hod/<int:id>/", HeadOfDepartmentDetailView.as_view()),
    path("designation/", DesigantionView.as_view()),
    path("designation/<int:id>/", DesignationDetailView.as_view()),
]
