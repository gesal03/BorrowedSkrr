from django.urls import path, include
from . import views
from rest_framework import urls


urlpatterns = [
    #path('signup/', include('dj_rest_auth.registration.urls')),
    # path('signup/', views.UserCreate.as_view()),
    path('employee-signup/', views.EmpolyeeCreate.as_view()),
    path('student-signup/', views.StudentCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('employeeInfo/<int:pk>', views.EmployeeInfoRetrieveUpdateDestroyAPIView.as_view()),
    path('studentInfo/<int:pk>', views.StudentInfoRetrieveUpdateDestroyAPIView.as_view()),
]
