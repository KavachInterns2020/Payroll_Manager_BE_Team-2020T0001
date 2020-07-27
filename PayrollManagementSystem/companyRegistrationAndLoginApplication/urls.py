from django.urls import path, include
from .views import LoginView,LogoutView,HolidayView,HolidayViewDetail

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('holiday/', HolidayView.as_view(), name='Holiday'),
    path('holiday/<int:id>', HolidayViewDetail.as_view(), name='HolidayViewDetail'),
    
]
